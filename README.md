🔐 Password Strength Checker
A powerful and interactive Password Strength Checker built with Python and Rich for a visually appealing terminal experience. This tool evaluates password security, estimates cracking time, and provides detailed analysis based on complexity criteria.

🚀 Features
✅ Stylish Metasploit-like terminal UI with colorful output
✅ Password strength classification: Very Weak, Weak, Moderate, Strong, Very Strong
✅ Estimated crack time based on brute-force attack speeds
✅ Detailed breakdown (length, uppercase, lowercase, digits, symbols)
✅ Looping mode for continuous password testing
✅ Verbose mode (-v) for in-depth analysis
✅ Quit option (-q) to exit the tool

🔧 Installation
Clone the repository:
bash
Copy
Edit
git clone https://github.com/Dawn-Fighter//password-strength-checker.git
cd password-strength-checker
Install dependencies:
bash
Copy
Edit
pip install rich
Run the tool:
bash
Copy
Edit
python password_checker.py
🎮 Usage
Run the tool and enter passwords interactively:

bash
Copy
Edit
python password_checker.py
Or provide a password directly:

bash
Copy
Edit
python password_checker.py -p "MySecureP@ss123"
Enable verbose mode for more details:

bash
Copy
Edit
python password_checker.py -p "MySecureP@ss123" -v
Quit the tool using:

bash
Copy
Edit
python password_checker.py -q
🛡️ Security Note
This tool is intended for personal security awareness and not for malicious use. Do not enter real passwords used for sensitive accounts.
