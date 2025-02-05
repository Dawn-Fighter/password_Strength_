import argparse
import getpass
import time
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import print
from time import sleep

def display_intro():
    console = Console()
    intro_text = Text()
    intro_text.append("\n========================================\n", style="bold yellow")
    intro_text.append("   WELCOME TO PASSWORD STRENGTH CHECKER   \n",style="bold magneta")
    intro_text.append("======================================== \n", style="bold yellow")
    intro_text.append("   A powerful tool to analyze password security \n",style="bold magneta")
    intro_text.append("=======================================\n\n")
    
    console.print(intro_text)
    sleep(1)
    print("[bold cyan]Initializing... Please wait.[/bold cyan]")
    sleep(2)

def check_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6:
        return "Very Weak"
    elif length < 8:
        return "Weak"
    elif length < 12:
        return "Moderate" if score >= 2 else "Weak"
    elif length < 16:
        return "Strong" if score >= 3 else "Moderate"
    else:
        return "Very Strong" if score == 4 else "Strong"

def estimate_crack_time(password: str) -> str:
    char_sets = {
        'digits': 10, 'lowercase': 26, 'uppercase': 26, 'symbols': 32
    }
    
    charset_size = sum(size for name, size in char_sets.items() if any(c in "0123456789" if name == 'digits' else
                                                                      "abcdefghijklmnopqrstuvwxyz" if name == 'lowercase' else
                                                                      "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if name == 'uppercase' else
                                                                      "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password))
    
    guesses_per_second = 10**9  # Standard GPU attack speed
    total_combinations = charset_size ** len(password)
    seconds_to_crack = total_combinations / guesses_per_second
    
    time_units = [("years", 31536000), ("days", 86400), ("hours", 3600), ("minutes", 60), ("seconds", 1)]
    for unit, factor in time_units:
        if seconds_to_crack >= factor:
            return f"Estimated time to crack: {seconds_to_crack / factor:.2f} {unit}"
    return "Crackable instantly!"

def main():
    console = Console()
    while True:
        display_intro()
        parser = argparse.ArgumentParser(description='Password Strength Checker')
        parser.add_argument('-p', '--password', type=str, help='Password to check')
        parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed analysis')
        parser.add_argument('-q', '--quit', action='store_true', help='Exit the tool')
        args = parser.parse_args()

        # Option to quit the program
        if args.quit:
            print("[bold red]Exiting Password Strength Checker... Goodbye![/bold red]")
            break
        
        password = args.password if args.password else getpass.getpass("Enter your password: ")

        strength = check_strength(password)
        crack_time = estimate_crack_time(password)
        
        result_table = Table(title="Password Analysis", style="bold cyan")
        result_table.add_column("Metric", style="bold yellow")
        result_table.add_column("Value", style="bold white")
        result_table.add_row("Password Strength", strength)
        result_table.add_row("Crack Time Estimate", crack_time)
        
        console.print(result_table)
        
        if args.verbose:
            verbose_table = Table(title="Detailed Analysis", style="bold cyan")
            verbose_table.add_column("Criteria", style="bold yellow")
            verbose_table.add_column("Status", style="bold white")
            verbose_table.add_row("Length", str(len(password)))
            verbose_table.add_row("Contains Uppercase", "Yes" if any(c.isupper() for c in password) else "No")
            verbose_table.add_row("Contains Lowercase", "Yes" if any(c.islower() for c in password) else "No")
            verbose_table.add_row("Contains Digit", "Yes" if any(c.isdigit() for c in password) else "No")
            verbose_table.add_row("Contains Symbol", "Yes" if any(not c.isalnum() for c in password) else "No")
            
            console.print(verbose_table)
        
        sleep(1)
        user_choice = input("Would you like to check another password? (y/n): ").lower()
        if user_choice != 'y':
            print("[bold red]Exiting Password Strength Checker... Goodbye![/bold red]")
            break

if __name__ == '__main__':
    main()
