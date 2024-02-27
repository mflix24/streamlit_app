import streamlit as st
import random
import string

def generate_random_alphanumeric(length):
    alphanumeric = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric) for _ in range(length))

# def create_new_account():
#     st.write("Creating a new bank account...")
#     random_account_number = generate_random_alphanumeric(12)
#     st.write(f"Your new account number is: {random_account_number}")


def create_new_account():
    st.write("Creating a new bank account...")

    user_id = st.text_input("Enter User ID:")
    email_address = st.text_input("Enter Email Address:")
    phone_number = st.text_input("Enter Phone Number:")
    present_address = st.text_input("Enter Present Address:")

    if st.button("Generate Account"):
        random_account_number = generate_random_alphanumeric(12)
        st.write(f"Your new account number is: {random_account_number}")
        st.write(f"User ID: {user_id}")
        st.write(f"Email Address: {email_address}")
        st.write(f"Phone Number: {phone_number}")
        st.write(f"Present Address: {present_address}")


# def connect_to_customer_rep():
#     st.write("Connecting to customer representative...")
#     st.write("Welcome To The World of AI")

def generate_good_vibes():
    good_vibe_sentences = [
        "Our bank values your trust and prioritizes your financial security.",
        "Experience hassle-free banking with our user-friendly online services.",
        "We are committed to providing excellent customer service at all times.",
        "Your satisfaction is our top priority, and we strive for continuous improvement.",
        "Explore our innovative financial solutions designed to meet your unique needs.",
        "Join a community of satisfied customers who have chosen us for their banking needs.",
        "Enjoy the convenience of 24/7 access to your accounts with our online banking platform.",
        "Rest assured, your personal information is handled with the utmost care and security.",
        "Discover the benefits of our competitive interest rates and financial products.",
        "Thank you for choosing us as your trusted banking partner!"
    ]
    return random.sample(good_vibe_sentences, 5)


def connect_to_customer_rep():
    st.write("Connecting to customer representative...")
    st.write("Welcome To The World of AI")

    st.write("Here are some good vibes about our bank policy:")
    good_vibes = generate_good_vibes()
    for vibe in good_vibes:
        st.write(f"- {vibe}")


# def change_password():
#     st.write("Changing password...")
#     old_password = "OldPassword"
#     new_password = "NewPassword"
#     st.write(f"Old password: {old_password}")
#     st.write(f"New password: {new_password}")
#     st.write(f"Repeat new password: {new_password}")


def change_password():
    st.write("Changing password...")

    old_password = st.text_input("Enter Old Password:", type="password")
    new_password = st.text_input("Enter New Password:", type="password")
    confirmation_password = st.text_input("Repeat New Password:", type="password")

    if st.button("Change Password"):
        if new_password == confirmation_password:
            st.write("Password changed successfully!")
            st.write(f"Old password: {old_password}")
            st.write(f"New password: {new_password}")
            st.write(f"Confirmation password: {confirmation_password}")
        else:
            st.error("New Password and Confirmation Password do not match. Please try again.")



# def update_profile():
#     st.write("Updating profile information...")
#     name = "Name"
#     phone_number = "PhoneNo"
#     home_address = "HomeAddress"
#     st.write(f"Name: {name}")
#     st.write(f"Phone Number: {phone_number}")
#     st.write(f"Home Address: {home_address}")


def update_profile():
    st.write("Updating profile information...")

    surname = st.text_input("Enter Surname:")
    name = st.text_input("Enter Name:")
    phone_number = st.text_input("Enter Phone Number:")
    present_address = st.text_input("Enter Present Address:")

    if st.button("Update Profile"):
        st.write(f"Family Name: {surname}")
        st.write(f"Name: {name}")
        st.write(f"Phone Number: {phone_number}")
        st.write(f"Present Address: {present_address}")



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
