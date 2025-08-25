import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            print("Database file not found. Starting fresh.")
    except Exception as err:
        print(f"An error occurred while loading data: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __generate_account_no(cls):
        parts = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(parts)
        return ''.join(parts)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return None, "You must be 18+ and use a 4-digit PIN."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": cls.__generate_account_no(),
            "balance": 0
        }

        cls.data.append(account)
        cls.__update()
        return account, "Account created successfully."

    @classmethod
    def find_user(cls, acc_no, pin):
        return next((u for u in cls.data if u["accountNo"] == acc_no and u["pin"] == pin), None)

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return "Invalid credentials."
        if not (0 < amount <= 99999):
            return "Amount must be between 1 and 99,999."

        user["balance"] += amount
        cls.__update()
        return "Deposit successful."

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return "Invalid credentials."
        if user["balance"] < amount:
            return "Insufficient funds."

        user["balance"] -= amount
        cls.__update()
        return "Withdrawal successful."

    @classmethod
    def get_details(cls, acc_no, pin):
        user = cls.find_user(acc_no, pin)
        return user

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        user = cls.find_user(acc_no, pin)
        if not user:
            return "Invalid credentials."

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            user["pin"] = int(new_pin)

        cls.__update()
        return "Details updated."

    @classmethod
    def delete_account(cls, acc_no, pin):
        user = cls.find_user(acc_no, pin)
        if not user:
            return "Invalid credentials."

        cls.data.remove(user)
        cls.__update()
        return "Account deleted."
