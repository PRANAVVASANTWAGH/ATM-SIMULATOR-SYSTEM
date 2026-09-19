# ATM Simulator System 🏦

A robust, Object-Oriented Command-Line Interface (CLI) ATM simulation application written in Python. This project models core banking transactions including card authentication, secure PIN changes, deposits, withdrawals, and real-time transaction statements.

---

## 🌟 Key Features

- **🔐 Security & Authentication:** Requires valid card numbers and PIN verification with a 3-attempt lockout system.
- **💰 Account Operations:** Real-time checking of balances, instant deposits, and account withdrawals with safety boundary checks.
- **📜 Transaction Logging:** Generates formatted statements complete with system timestamps and ending balances.
- **🔑 Customization:** Enables users to safely update their 4-digit PIN within the active session.
- **🛡️ Error Handling:** Prevents invalid string inputs, negative transactions, or account overdrafts.

---

## 🛠️ Demo Credentials

Use any of these pre-configured accounts to test the application:

| Card Number | Initial PIN | Account Holder | Starting Balance |
| :--- | :--- | :--- | :--- |
| `1001` | `1234` | Alex Morgan | $1,500.50 |
| `1002` | `4321` | Sam Taylor | $500.00 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher installed on your machine.

### Installation & Execution

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/atm-simulator-system.git](https://github.com/YOUR_USERNAME/atm-simulator-system.git)
   cd atm-simulator-system
