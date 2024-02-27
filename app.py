import streamlit as st

def create_new_account():
    st.write("Creating a new bank account...")
    # Your code to handle creating a new account goes here

def connect_to_customer_rep():
    st.write("Connecting to customer representative...")
    # Your code to handle connecting to a customer representative goes here

def change_password():
    st.write("Changing password...")
    # Your code to handle changing the password goes here

def update_profile():
    st.write("Updating profile information...")
    # Your code to handle updating profile information goes here

def main():
    st.title("Bank Chatbot")

    choice = st.selectbox("What do you want to do?", ["", "Create a new account", "Connect to customer representative", "Change password", "Update profile information"])

    if choice == "Create a new account":
        create_new_account()
    elif choice == "Connect to customer representative":
        connect_to_customer_rep()
    elif choice == "Change password":
        change_password()
    elif choice == "Update profile information":
        update_profile()

if __name__ == "__main__":
    main()
