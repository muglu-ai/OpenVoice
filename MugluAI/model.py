import numpy as np
import tensorflow as tf

# Define parameters
num_epochs = 50
batch_size = 64
seq_length = 100
learning_rate = 0.01
temperature = 1.0

# Data preprocessing
text = open('data.txt', 'r').read()
vocab = sorted(set(text))
char_to_idx = {char: idx for idx, char in enumerate(vocab)}
idx_to_char = np.array(vocab)
text_as_int = np.array([char_to_idx[c] for c in text])

# Create training examples and targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)

# Build the model
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim),
        tf.keras.layers.GRU(rnn_units,
                           return_sequences=True,
                           stateful=True,
                           recurrent_initializer='glorot_uniform',
                           batch_input_shape=(batch_size, None)),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model

model = build_model(vocab_size=len(vocab),
                    embedding_dim=256,
                    rnn_units=1024,
                    batch_size=batch_size)
                    
# Reshape the input data to match the expected 3D shape
dataset = dataset.map(lambda x, y: (tf.expand_dims(x, -1), y))

# Define loss function
def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

model.compile(optimizer='adam', loss=loss)

for epoch in range(num_epochs):
    print(f'Epoch {epoch + 1}/{num_epochs}')
    for batch_input, batch_target in dataset.take(len(dataset) // batch_size):
        model.fit(batch_input, batch_target, batch_size=batch_size, epochs=1, shuffle=False)
        model.reset_states()

# Function to generate text
def generate_text(model, start_string, temperature=1.0):
    num_generate = 1000
    input_eval = [char_to_idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)
    text_generated = []
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0) / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx_to_char[predicted_id])
    return (start_string + ''.join(text_generated))

# Generate text
generated_text = generate_text(model, start_string='The', temperature=0.5)
print(generated_text)