# Problem Statement & System Requirements: ATM Simulator System

## 1. Overview
Automated Teller Machines (ATMs) are critical self-service banking terminals that process sensitive user financial data, manage account balances, and execute real-time transactions. Building a command-line ATM simulator helps demonstrate core concepts of **Object-Oriented Programming (OOP)**, state management, security checks, and defensive input validation.

---

## 2. Problem Statement
Traditional entry-level transaction systems often suffer from key design vulnerabilities, including lack of authentication safeguards, unhandled runtime exceptions during data entry, and inadequate tracking of intermediate state changes. 

The objective of this project is to build a reliable, interactive **ATM Simulator System** in Python that models real-world banking operations while maintaining data integrity, account security, and session isolation.

---

## 3. Scope of the System

### In-Scope Functionality
* **User Authentication:** 
  * Verification of user identity via card number and 4-digit PIN.
  * Account lockout mechanism triggered after 3 consecutive invalid PIN entries.
* **Account Management:**
  * Real-time balance inquiry.
  * Money deposit with non-zero and positive validation checks.
  * Money withdrawal subject to account balance constraints (overdraft prevention).
* **Security Operations:**
  * In-session PIN modification with confirmation matching and format validation.
* **Audit & Logging:**
  * Session-based transaction history recording itemized timestamps, transaction types (deposit/withdrawal), transaction amounts, and post-transaction balances.

### Out-of-Scope (Future Enhancements)
* Database persistence (e.g., SQLite or PostgreSQL connection across application restarts).
* Graphical User Interface (GUI) or web application frontend.
* Multi-account transfers between different cardholders.
* Hardware-level integration (e.g., cash dispenser motor control or physical card reader integration).

---

## 4. Functional Requirements

| ID | Module | Description |
| :--- | :--- | :--- |
| **FR-01** | Authentication | The system must prompt for card number and PIN before granting access to menu options. |
| **FR-02** | Lockout Policy | The system must restrict account access if an incorrect PIN is entered 3 consecutive times. |
| **FR-03** | Balance Inquiry | The system must display the precise floating-point balance of the authenticated account. |
| **FR-04** | Deposit | The system must accept positive deposits and immediately update the account balance. |
| **FR-05** | Withdrawal | The system must check for sufficient funds before completing a withdrawal and deduct the requested amount. |
| **FR-06** | Statement | The system must maintain an append-only transaction history log during the active session. |
| **FR-07** | PIN Change | The system must require validation of the existing PIN and double-confirmation of the new 4-digit PIN. |

---

## 5. Non-Functional Requirements

* **Reliability & Robustness:** The program must gracefully handle unexpected input types (e.g., alphabetic input where numerical values are expected) without crashing.
* **Usability:** The CLI interface must provide clear success/error messages and formatted table outputs for receipts and statements.
* **Maintainability:** Code structure must adhere to Object-Oriented principles, separating account-level business logic (`Account` class) from terminal operations (`ATMSimulator` class).

---

## 6. Technical Specifications

* **Language:** Python 3.7+
* **Dependencies:** Python Standard Library (`datetime`)
* **Interface:** Command-Line Interface (CLI)
