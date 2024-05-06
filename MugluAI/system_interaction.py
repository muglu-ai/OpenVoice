import os
import streamlit as st

# Define the Streamlit app
def main():
    st.title("OS Interaction App")

    # Get current working directory
    current_dir = os.getcwd()
    st.write("Current directory:", current_dir)

    # List files and directories in current directory
    st.write("Contents of current directory:")
    for item in os.listdir(current_dir):
        st.write(item)

    # Create a new directory
    new_dir_name = st.text_input("Enter name for new directory:")
    if st.button("Create Directory"):
        new_dir = os.path.join(current_dir, new_dir_name)
        os.mkdir(new_dir)
        st.write("Created new directory:", new_dir)

    # Change directory
    change_dir = st.selectbox("Change directory?", ["No", "Yes"])
    if change_dir == "Yes":
        new_dir_path = st.text_input("Enter path for new directory:")
        try:
            os.chdir(new_dir_path)
            st.write("Changed directory to:", new_dir_path)
        except FileNotFoundError:
            st.write("Directory not found:", new_dir_path)

    # List files and directories in the current directory
    st.write("Contents of current directory:")
    for item in os.listdir(os.getcwd()):
        st.write(item)

    # Remove directory
    remove_dir_name = st.text_input("Enter name of directory to remove:")
    if st.button("Remove Directory"):
        remove_dir = os.path.join(current_dir, remove_dir_name)
        try:
            os.rmdir(remove_dir)
            st.write("Removed directory:", remove_dir)
        except FileNotFoundError:
            st.write("Directory not found:", remove_dir)

# Run the Streamlit app
if __name__ == "__main__":
    main()
