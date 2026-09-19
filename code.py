import datetime


class Account:

    def __init__(self, card_number, pin, name, balance=0.0):
        self.card_number = card_number
        self.pin = pin
        self.name = name
        self.balance = float(balance)
        self.transaction_history = []

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def log_transaction(self, tx_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(
            {
                "timestamp": timestamp,
                "type": tx_type,
                "amount": amount,
                "balance_after": self.balance,
            }
        )

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than $0."

        self.balance += amount
        self.log_transaction("Deposit", amount)
        return True, f"Successfully deposited ${amount:.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than $0."
        if amount > self.balance:
            return False, "Insufficient funds."

        self.balance -= amount
        self.log_transaction("Withdrawal", amount)
        return True, f"Successfully withdrew ${amount:.2f}."

    def change_pin(self, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit():
            return False, "PIN must be exactly 4 digits."

        self.pin = new_pin
        return True, "PIN updated successfully."


class ATMSimulator:

    def __init__(self):
        # Sample bank database holding registered accounts
        self.accounts = {
            "1001": Account(
                "1001", "1234", "Alex Morgan", balance=1500.50
            ),
            "1002": Account(
                "1002", "4321", "Sam Taylor", balance=500.00
            ),
        }
        self.current_account = None

    def authenticate_user(self):
        print("\n" + "=" * 40)
        print("         WELCOME TO GLOBAL BANK ATM      ")
        print("=" * 40)

        card_number = input("Enter Card Number (e.g., 1001): ").strip()
        account = self.accounts.get(card_number)

        if not account:
            print("Error: Invalid Card Number.")
            return False

        attempts = 3
        while attempts > 0:
            pin = input("Enter 4-Digit PIN: ").strip()
            if account.verify_pin(pin):
                self.current_account = account
                print(f"\nAuthentication successful! Welcome, {account.name}.")
                return True

            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. Attempts remaining: {attempts}")

        print("Account locked due to 3 failed PIN attempts.")
        return False

    def display_menu(self):
        print("\n" + "-" * 30)
        print("          MAIN MENU          ")
        print("-" * 30)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Change PIN")
        print("6. Exit / Remove Card")
        print("-" * 30)

    def handle_balance_inquiry(self):
        balance = self.current_account.check_balance()
        print(f"\n[BALANCE]: Your current balance is: ${balance:.2f}")

    def handle_deposit(self):
        try:
            amount = float(input("\nEnter amount to deposit: $"))
            success, message = self.current_account.deposit(amount)
            print(f"[{'SUCCESS' if success else 'ERROR'}]: {message}")
            if success:
                print(
                    f"New Balance: ${self.current_account.check_balance():.2f}"
                )
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def handle_withdrawal(self):
        try:
            amount = float(input("\nEnter amount to withdraw: $"))
            success, message = self.current_account.withdraw(amount)
            print(f"[{'SUCCESS' if success else 'ERROR'}]: {message}")
            if success:
                print(
                    f"New Balance: ${self.current_account.check_balance():.2f}"
                )
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def handle_history(self):
        history = self.current_account.transaction_history
        if not history:
            print("\n[HISTORY]: No transactions recorded during this session.")
            return

        print("\n" + "=" * 55)
        print("                  TRANSACTION STATEMENT                   ")
        print("=" * 55)
        print(
            f"{'Timestamp':<20} | {'Type':<12} | {'Amount ($)':<10} | {'Balance ($)':<10}"
        )
        print("-" * 55)
        for tx in history:
            print(
                f"{tx['timestamp']:<20} | {tx['type']:<12} | {tx['amount']:<10.2f} | {tx['balance_after']:<10.2f}"
            )
        print("=" * 55)

    def handle_change_pin(self):
        current_pin = input("\nEnter current PIN: ").strip()
        if not self.current_account.verify_pin(current_pin):
            print("Error: Current PIN verification failed.")
            return

        new_pin = input("Enter new 4-digit PIN: ").strip()
        confirm_pin = input("Confirm new 4-digit PIN: ").strip()

        if new_pin != confirm_pin:
            print("Error: New PINs do not match.")
            return

        success, message = self.current_account.change_pin(new_pin)
        print(f"[{'SUCCESS' if success else 'ERROR'}]: {message}")

    def start(self):
        if not self.authenticate_user():
            return

        while True:
            self.display_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                self.handle_balance_inquiry()
            elif choice == "2":
                self.handle_deposit()
            elif choice == "3":
                self.handle_withdrawal()
            elif choice == "4":
                self.handle_history()
            elif choice == "5":
                self.handle_change_pin()
            elif choice == "6":
                print(
                    f"\nThank you for using Global Bank, {self.current_account.name}. Don't forget your card!"
                )
                self.current_account = None
                break
            else:
                print("Invalid choice. Please select an option between 1 and 6.")


if __name__ == "__main__":
    atm = ATMSimulator()
    atm.start()
