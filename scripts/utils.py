import os
from colorama import Fore, Style, init

init(autoreset=True)

class Logger:
    @staticmethod
    def info(message):
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} {message}")
    
    @staticmethod
    def success(message):
        print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")
    
    @staticmethod
    def error(message):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")
    
    @staticmethod
    def progress(message):
        print(f"{Fore.MAGENTA}[PROGRESS]{Style.RESET_ALL} {message}")
    
    @staticmethod
    def prompt(message):
        return input(f"{Fore.YELLOW}[PROMPT]{Style.RESET_ALL} {message}")

def validate_file_exists(file_path):
    if not os.path.exists(file_path):
        Logger.error(f"File not found: {file_path}")
        return False
    return True

def get_output_path(input_path, output_filename):
    input_dir = os.path.dirname(input_path)
    output_path = os.path.join(input_dir, output_filename)
    return output_path

def is_valid_choice(choice, max_options):
    try:
        choice_num = int(choice)
        return 1 <= choice_num <= max_options
    except ValueError:
        return False
