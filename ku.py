import time
import requests
import random
import urllib.parse
import os
import signal
import itertools
import json
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for color output in bash environments
init(autoreset=True)

# Global variable to control the main loop
running = True
encoded_data_list = []

# Handling persistent account storage
def save_accounts_to_file():
    with open('accounts.txt', 'w') as file:
        json.dump(encoded_data_list, file)

def load_accounts_from_file():
    global encoded_data_list
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', 'r') as file:
            encoded_data_list = json.load(file)

# Load accounts if available
load_accounts_from_file()

# Function to clear the terminal screen (works on both Termux and bash environments)
def clear_terminal():
    os.system('clear')

# Function to handle loading animations
def loading_animation():
    animations = [
        itertools.cycle(['|', '/', '-', '\\']),
        itertools.cycle(['.', '..', '...', '....']),
    ]
    
    current_animation = random.choice(animations)
    for _ in range(20):
        print(Fore.LIGHTBLACK_EX + f"\rWorking... {next(current_animation)}", end="")
        time.sleep(0.1)
    print("\r" + " " * 40, end="")  # Clear the line after the animation

# Signal handler for clean exit
def signal_handler(signum, frame):
    global running
    running = False
    print(Fore.LIGHTBLACK_EX + f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " +
          Fore.YELLOW + "Signal caught. Exiting safely...")

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

def welcome_message():
    clear_terminal()
    print(Fore.CYAN + "Welcome to Kucoin Tap Master 3000!")
    print(Fore.GREEN + "This script is optimized for Termux and bash environments.")
    print(Fore.GREEN + "Brought to you by the Virtusoses Team | Telegram: https://t.me/virtusoses")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.LIGHTCYAN_EX + "Initializing...\n")

# Function to display the total number of accounts
def display_accounts_summary(total_accounts):
    print(Fore.CYAN + "---------------------------------------------------")
    print(Fore.YELLOW + f"Total Accounts Loaded: {Fore.WHITE}{total_accounts}")
    print(Fore.CYAN + "---------------------------------------------------")
    print(Fore.GREEN + "Login successful! Let's start tapping those coins.")
    print(Fore.CYAN + "---------------------------------------------------")

# Function to prompt the user for account input
def prompt_encoded_data():
    print(Fore.YELLOW + "\nEnter your encoded user data:")
    print(Fore.LIGHTBLACK_EX + "Format: " + Fore.WHITE +
          "user=%7B%22id%22%3A6519343180%2C%22first_name%22%3A%22Jack%20Samuel%22%7D&auth_date=...&hash=...")
    data = input(Fore.GREEN + "Type the encoded string: ")
    return data

# Function to manage user accounts (add, view, delete)
def manage_accounts():
    while True:
        clear_terminal()
        print(Fore.CYAN + "Account Management")
        print(Fore.LIGHTBLACK_EX + "--------------------------------------------")
        print(Fore.GREEN + "[1] Add a new account")
        print(Fore.GREEN + "[2] View all accounts")
        print(Fore.GREEN + "[3] Delete an account")
        print(Fore.GREEN + "[4] Clear all accounts")
        print(Fore.CYAN + "[5] Start the script")
        print(Fore.RED + "[0] Exit")
        print(Fore.LIGHTBLACK_EX + "--------------------------------------------")

        choice = input(Fore.GREEN + "Your choice: ")

        if choice == "1":
            encoded_data = prompt_encoded_data()
            encoded_data_list.append(encoded_data)
            save_accounts_to_file()  # Save after adding
            print(Fore.LIGHTBLACK_EX + f"Account added! Total: {len(encoded_data_list)}")
            time.sleep(1)
        elif choice == "2":
            if encoded_data_list:
                print(Fore.LIGHTCYAN_EX + "Your Accounts:")
                for i, data in enumerate(encoded_data_list, 1):
                    print(Fore.LIGHTBLACK_EX + f"[{i}] {data}")
            else:
                print(Fore.RED + "No accounts added yet.")
            input(Fore.GREEN + "\nPress Enter to return to the menu...")
        elif choice == "3":
            if encoded_data_list:
                print(Fore.CYAN + "Choose an account to delete:")
                for i, data in enumerate(encoded_data_list, 1):
                    print(Fore.LIGHTBLACK_EX + f"[{i}] {data}")
                to_delete = input(Fore.RED + "Enter the number of the account to delete: ")
                try:
                    index = int(to_delete) - 1
                    if 0 <= index < len(encoded_data_list):
                        deleted = encoded_data_list.pop(index)
                        save_accounts_to_file()  # Save after deletion
                        print(Fore.GREEN + f"Deleted: {deleted}")
                    else:
                        print(Fore.RED + "That account number doesn't exist.")
                except ValueError:
                    print(Fore.RED + "Enter a valid number.")
            else:
                print(Fore.RED + "No accounts to delete.")
            time.sleep(1)
        elif choice == "4":
            if encoded_data_list:
                confirmation = input(Fore.RED + "Are you sure you want to delete all accounts? (yes/no): ").lower()
                if confirmation == "yes":
                    encoded_data_list.clear()
                    save_accounts_to_file()  # Save after clearing
                    print(Fore.GREEN + "All accounts cleared.")
                else:
                    print(Fore.YELLOW + "Operation cancelled.")
            else:
                print(Fore.RED + "No accounts to clear.")
            time.sleep(1)
        elif choice == "5":
            if encoded_data_list:
                break
            else:
                print(Fore.RED + "No accounts found. Add one first.")
                time.sleep(1)
        elif choice == "0":
            print(Fore.GREEN + "Goodbye!")
            exit(0)
        else:
            print(Fore.RED + "Invalid option. Try again.")
            time.sleep(1)

# Function to decode account data
def decode_data(encoded_data):
    params = dict(item.split('=') for item in encoded_data.split('&'))
    decoded_user = urllib.parse.unquote(params['user'])
    decoded_start_param = urllib.parse.unquote(params['start_param'])
    return {
        "decoded_user": decoded_user,
        "decoded_start_param": decoded_start_param,
        "hash": params['hash'],
        "auth_date": params['auth_date'],
        "chat_type": params['chat_type'],
        "chat_instance": params['chat_instance']
    }

# Function to login with Kucoin API
def login(decoded_data):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/login?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }
    
    body = {
        "inviterUserId": "5496274031",
        "extInfo": {
            "hash": decoded_data['hash'],
            "auth_date": decoded_data['auth_date'],
            "via": "miniApp",
            "user": decoded_data['decoded_user'],
            "chat_type": decoded_data['chat_type'],
            "chat_instance": decoded_data['chat_instance'],
            "start_param": decoded_data['decoded_start_param']
        }
    }

    session = requests.Session()
    response = session.post(url, headers=headers, json=body)
    cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in session.cookies])             
    return cookie

# Function to retrieve data from Kucoin API
def data(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "cookie": cookie
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data", {}).get("availableAmount")
    molecule = data.get("data", {}).get("feedPreview", {}).get("molecule")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.GREEN + f"Current Balance: {balance}")
    return molecule

# Function to perform taps on Kucoin API
def tap(cookie, molecule):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/gold/increase?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": cookie
    }

    total_increment = 0

    while total_increment < 3000 and running:
        increment = random.randint(55, 60)
        form_data = {
            'increment': str(increment),
            'molecule': str(molecule)
        }

        try:
            response = requests.post(url, headers=headers, data=form_data)
            total_increment += increment
            
            print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                  Fore.GREEN + f"Tapped: {increment} | Total Tapped: {total_increment}/3000")
            
            loading_animation()  # Simple loading animation
            
        except requests.exceptions.RequestException:
            print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                  Fore.RED + "Network issues! Retrying...")
            time.sleep(5)

# Function to get the updated balance
def new_balance(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "cookie": cookie
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data", {}).get("availableAmount")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.GREEN + f"New Balance: {balance}")

# Main function to drive the program
def main():
    global running
    welcome_message()
    manage_accounts()
    total_accounts = len(encoded_data_list)
    
    try:
        while running:
            clear_terminal()
            display_accounts_summary(total_accounts)
        
            for index, encoded_data in enumerate(encoded_data_list, start=1):
                if not running:
                    break
                print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                      Fore.GREEN + f"Processing Account {index}")
                try:
                    decoded_data = decode_data(encoded_data)
                    cookie = login(decoded_data)
                    molecule = data(cookie)
                    tap(cookie, molecule)
                    new_balance(cookie)
                except Exception as e:
                    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                          Fore.RED + f"Error with Account {index}: {str(e)}")
            
            if running:
                print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                      Fore.YELLOW + "Taking a 2-minute break before the next cycle...")
                for _ in range(120):
                    if not running:
                        break
                    time.sleep(1)
    except Exception as e:
        print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
              Fore.RED + f"Something went wrong: {str(e)}")
    finally:
        print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
              Fore.GREEN + "Logged out successfully.")

if __name__ == "__main__":
    main()
