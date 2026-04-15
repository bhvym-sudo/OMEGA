import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

sys.path.insert(0, os.path.dirname(__file__))

from scripts import csv_to_xlsx, xlsx_to_csv, json_to_csv
from scripts.utils import Logger, validate_file_exists, get_output_path, is_valid_choice

BANNER = r"""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                        OMEGA                              ║
║                                                           ║
║           Transform Your Files With Ease                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""

CONVERSION_MAP = {
    ("csv", "xlsx"): csv_to_xlsx.convert,
    ("xlsx", "csv"): xlsx_to_csv.convert,
    ("json", "csv"): json_to_csv.convert,
}

CONVERSION_OPTIONS = [
    ("CSV", "XLSX"),
    ("XLSX", "CSV"),
    ("JSON", "CSV"),
]

def display_banner():
    print(f"{Fore.CYAN}{BANNER}{Style.RESET_ALL}")

def display_conversion_menu():
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Supported Conversions:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    for idx, (from_fmt, to_fmt) in enumerate(CONVERSION_OPTIONS, 1):
        print(f"{Fore.YELLOW}{idx}.{Style.RESET_ALL} {from_fmt} → {to_fmt}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

def get_user_choice():
    while True:
        choice = Logger.prompt("Select conversion (enter number): ").strip()
        if is_valid_choice(choice, len(CONVERSION_OPTIONS)):
            return int(choice) - 1
        Logger.error("Invalid selection. Please try again.")

def get_input_file_path():
    while True:
        file_path = Logger.prompt("Enter input file path: ").strip().strip('"')
        if validate_file_exists(file_path):
            return file_path

def get_output_filename():
    while True:
        filename = Logger.prompt("Enter output filename (with extension): ").strip()
        if filename:
            return filename
        Logger.error("Filename cannot be empty.")

def perform_conversion(conversion_idx):
    from_fmt, to_fmt = CONVERSION_OPTIONS[conversion_idx]
    
    Logger.info(f"You selected: {from_fmt} → {to_fmt}")
    print()
    
    input_path = get_input_file_path()
    Logger.progress(f"Input file selected: {input_path}")
    print()
    
    output_filename = get_output_filename()
    output_path = get_output_path(input_path, output_filename)
    Logger.progress(f"Output filename: {output_filename}")
    print()
    
    Logger.info(f"Starting conversion process...")
    print()
    
    conversion_func = CONVERSION_MAP[(from_fmt.lower(), to_fmt.lower())]
    result = conversion_func(input_path, output_path)
    
    print()
    return result

def run_again():
    choice = Logger.prompt("Do another conversion? (yes/no): ").strip().lower()
    return choice in ['yes', 'y']

def main():
    display_banner()
    
    while True:
        display_conversion_menu()
        conversion_idx = get_user_choice()
        
        success = perform_conversion(conversion_idx)
        
        if success:
            if not run_again():
                Logger.success("Thank you for using OMEGA!")
                break
        else:
            retry = Logger.prompt("Try again? (yes/no): ").strip().lower()
            if retry not in ['yes', 'y']:
                Logger.info("Exiting...")
                break

if __name__ == "__main__":
    main()
