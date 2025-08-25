import streamlit as st
from main import Bank

st.set_page_config(page_title="Banking System", layout="centered")
st.title("🏦 Simple Banking System")

menu = ["Create Account", "Deposit", "Withdraw", "View Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", max_chars=4, type="password")

    if st.button("Create Account"):
        if name and email and pin.isdigit() and len(pin) == 4:
            acc, msg = Bank.create_account(name, int(age), email, int(pin))
            st.success(msg)
            if acc:
                st.info(f"Your Account Number: {acc['accountNo']}")
        else:
            st.error("Fill all fields correctly!")

elif choice == "Deposit":
    st.header("Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        result = Bank.deposit(acc_no, int(pin), int(amount))
        st.success(result)

elif choice == "Withdraw":
    st.header("Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        result = Bank.withdraw(acc_no, int(pin), int(amount))
        st.success(result)

elif choice == "View Details":
    st.header("Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Get Details"):
        user = Bank.get_details(acc_no, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid credentials.")

elif choice == "Update Details":
    st.header("Update Your Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        result = Bank.update_user(acc_no, int(pin), name, email, new_pin)
        st.success(result)

elif choice == "Delete Account":
    st.header("Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        result = Bank.delete_account(acc_no, int(pin))
        st.success(result)
