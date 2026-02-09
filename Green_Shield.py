import os
import time

# Colors for professional Terminal look
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
RESET = '\033[0m'

def secret_panel():
    os.system('clear')
    print(f"{RED}")
    print("      ####################################")
    print("      #    WELCOME TO SECRET ADMIN MODE  #")
    print("      #        DEVELOPER: AMMAR DZ       #")
    print("      ####################################")
    print(f"{GREEN}")
    print(" [99] Deep Network Injection")
    print(" [100] Bypass Security Layers")
    print(" [101] Encrypt Project Files")
    print(" [00] Return to Main Menu")
    print(f"{RESET}")
    input(" admin@green_shield ~# ")

def main_menu():
    os.system('clear')
    print(f"{GREEN}")
    print("  ██████╗ ██████╗ ███████╗███████╗███╗   ██╗")
    print(" ██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║")
    print(" ██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║")
    print(" ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║")
    print(" ╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║")
    print("  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝")
    print("       SHIELD ALGERIAN EDITION V2.0         ")
    print(f"{YELLOW}--------------------------------------------")
    print(f"{BLUE} [1] Phone System Scanner")
    print(f"{BLUE} [2] Website Vulnerability Check")
    print(f"{BLUE} [3] Network Security Test")
    print(f"{BLUE} [4] About Developer")
    print(f"{RED} [E] Exit")
    print(f"{YELLOW}--------------------------------------------")
    print(f"{RESET}")

def run():
    while True:
        main_menu()
        choice = input(f"{GREEN}Select Option (or enter secret key): {RESET}")

        if choice == "dz24": # Your secret key
            secret_panel()
        elif choice == "1":
            print(f"{YELLOW}\n[*] Scanning Phone System... Please wait...")
            time.sleep(2)
            print(f"{GREEN}[+] Scan Complete: No threats found.")
            input("\nPress Enter to continue...")
        elif choice == "2":
            print(f"{YELLOW}\n[*] Checking Website Security...")
            time.sleep(2)
            print(f"{GREEN}[+] Analysis finished.")
            input("\nPress Enter to continue...")
        elif choice == "3":
            print(f"{YELLOW}\n[*] Testing Network...")
            time.sleep(2)
            input("\nPress Enter to continue...")
        elif choice == "4":
            print(f"{BLUE}\nDeveloper: Ammar from Guelma")
            print("Status: Pro Programmer")
            input("\nPress Enter to continue...")
        elif choice.lower() == "e":
            print(f"{RED}Exiting Green Shield... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid Option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    run()
