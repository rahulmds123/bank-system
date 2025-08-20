import streamlit as st

# ---- Bankaccount1 class ----
class Bankaccount1:
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


# ---- SavingsAccount class ----
class SavingsAccount(Bankaccount1):
    def __init__(self, account_number, account_name, interest_rate):
        super().__init__(account_number, account_name)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        return interest


# ---- Streamlit UI ----
st.title("🏦 Simple Banking System")

# Select account type
account_type = st.radio("Choose Account Type", ["Bank Account", "Savings Account"])

if account_type == "Bank Account":
    acc_no = st.text_input("Enter Account Number", "123")
    acc_name = st.text_input("Enter Account Holder Name", "John Doe")

    # Initialize account in session state
    if "bank" not in st.session_state:
        st.session_state.bank = Bankaccount1(acc_no, acc_name)

    bank = st.session_state.bank

    st.subheader("Bank Account Operations")
    deposit_amount = st.number_input("Deposit Amount", min_value=0.0, step=100.0)
    if st.button("Deposit"):
        if bank.deposit(deposit_amount):
            st.success(f"Deposited {deposit_amount}")
        else:
            st.error("Invalid deposit amount")

    withdraw_amount = st.number_input("Withdraw Amount", min_value=0.0, step=100.0)
    if st.button("Withdraw"):
        if bank.withdraw(withdraw_amount):
            st.success(f"Withdrew {withdraw_amount}")
        else:
            st.error("Insufficient funds")

    st.info(f"💰 Current Balance: {bank.get_balance()}")

else:
    acc_no = st.text_input("Enter Account Number", "456")
    acc_name = st.text_input("Enter Account Holder Name", "Jane Doe")
    interest_rate = st.number_input("Interest Rate (%)", min_value=1.0, max_value=20.0, value=5.0)

    # Initialize savings account
    if "savings" not in st.session_state:
        st.session_state.savings = SavingsAccount(acc_no, acc_name, interest_rate)

    savings = st.session_state.savings

    st.subheader("Savings Account Operations")
    deposit_amount = st.number_input("Deposit Amount", min_value=0.0, step=100.0, key="savings_deposit")
    if st.button("Deposit", key="savings_deposit_btn"):
        if savings.deposit(deposit_amount):
            st.success(f"Deposited {deposit_amount}")
        else:
            st.error("Invalid deposit amount")

    withdraw_amount = st.number_input("Withdraw Amount", min_value=0.0, step=100.0, key="savings_withdraw")
    if st.button("Withdraw", key="savings_withdraw_btn"):
        if savings.withdraw(withdraw_amount):
            st.success(f"Withdrew {withdraw_amount}")
        else:
            st.error("Insufficient funds")

    if st.button("Add Interest"):
        interest = savings.add_interest()
        st.success(f"Interest added: {interest}")

    st.info(f"💰 Current Savings Balance: {savings.get_balance()}")
