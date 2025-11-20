from colorama import Fore, Style, init
init(autoreset=True)

class Color:
    HEADER = Fore.CYAN + Style.BRIGHT
    OK = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.YELLOW + Style.BRIGHT
    ERROR = Fore.RED + Style.BRIGHT
    INFO = Fore.BLUE + Style.BRIGHT
    RESET = Style.RESET_ALL
