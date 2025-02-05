# Password Strength Checker

A powerful tool to analyze password security and estimate the time required to crack it. This tool evaluates password strength based on length, character diversity, and complexity.

## Features
- Evaluates password strength as **Very Weak, Weak, Moderate, Strong, or Very Strong**.
- Estimates the time required to crack the password based on standard GPU attack speeds.
- Provides a **detailed analysis** of password composition when the `--verbose` flag is used.
- Uses **Rich Library** for an enhanced terminal output experience.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.6). You can check your Python version with:
```sh
python --version
```

### Clone the Repository
```sh
git clone https://github.com/Dawn-Fighter/password-strength-checker.git
cd password-strength-checker
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the script using the following command:
```sh
python password_checker.py
```

You can also pass arguments:
- **Check a password**
  ```sh
  python password_checker.py -p YourPassword123!
  ```
- **Verbose mode (detailed analysis)**
  ```sh
  python password_checker.py -p YourPassword123! -v
  ```
- **Quit the program**
  ```sh
  python password_checker.py -q
  ```

## Example Output
```
========================================
   WELCOME TO PASSWORD STRENGTH CHECKER   
========================================
   A powerful tool to analyze password security
========================================

Initializing... Please wait.

╔═════════════════════════════╗
║     Password Analysis       ║
╠═════════════════════════════╣
║ Password Strength    │ Strong  ║
║ Crack Time Estimate  │ 10 years║
╚═════════════════════════════╝
```

## Contributing
1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
[Your Name](https://github.com/Dawn-Fighter)

