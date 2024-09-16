import os
import time
import platform
import requests
import logging
from datetime import datetime
import socket
from time import sleep
from bs4 import BeautifulSoup
import pytz  
import webbrowser
import subprocess

API_VERSION = 'v15.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/53736 (KHTML, like Gecko) Chrome/56.0.24.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def install_dependencies():
    required_modules = ['pytz', 'requests', 'beautifulsoup4']

    try:
        for module in required_modules:
            __import__(module)
    except ImportError:
        print("\033[1;32mInstalling required packages. Please wait...\033[0m")
        for module in required_modules:
            try:
                subprocess.run(['python', '-m', 'pip', 'install', module], check=True)
            except subprocess.CalledProcessError:
                print(f"\033[1;31mError installing {module}. Please install it manually.\033[0m")
        
        print("\033[1;32mPackages installed successfully!\033[0m")

install_dependencies()

# Colored text definitions
lion_color_text = "\033[38;2;193;154;107m"
brown_text = "\033[0;33m"
yellow_text = "\033[1;33m"
red_text = "\033[1;31m"
green_text = "\033[1;32m"
cyan_text = "\033[1;36m"
blue_text = "\033[1;34m"
magenta_text = "\033[1;35m"
pink_text = "\033[1;38;5;206m"
purple_text = "\033[1;38;5;90m"
golden_text = "\033[1;38;5;178m"
teal_text = "\033[1;38;5;30m"
orange_text = "\033[1;38;5;208m"
midnight_blue_text = "\033[1;38;5;17m"
khaki_text = "\033[1;38;5;185m"
coral_text = "\033[1;38;5;209m"
reset_text = "\033[0m"

# Loading messages
loading_messages = [
    f"{green_text}Loading the program. Please wait...{reset_text}",
    f"{lion_color_text}Configuring settings...{reset_text}",
    f"{yellow_text}Checking internet connection...{reset_text}",
    f"{green_text}Installing dependencies...{reset_text}",
    f"{orange_text}Preparing to send messages...{reset_text}"
]

# Print loading messages
for message in loading_messages:
    print(message)
    time.sleep(2)

# Welcome message with defined colors
welcome_message = f"""
\033[1;38;5;208mWELCOME TO THE ANAND MEHRA ADVANCED TOOL HUB!\033[0m
"""

welcome_text = "WELCOME TO THE ANAND MEHRA ADVANCED TOOL WORLD"

# Animate welcome text with colors
colors = [
    red_text, yellow_text, magenta_text, golden_text,
    blue_text, green_text, cyan_text, coral_text
]

for color in colors:
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
    print(f"{color}{welcome_text}{reset_text}")
    time.sleep(1)  # Adjust sleep time for animation speed

group_link = "https://chat.whatsapp.com/Jkhcw2HIESVL6p7hDNLiwh"
webbrowser.open(group_link)

def dynamic_loading_message():
    loading_symbols = "|/-\\"
    for _ in range(20):
        for symbol in loading_symbols:
            print(f"{golden_text}\rPlease wait, conversation is loading {symbol}{reset_text}", end='', flush=True)
            time.sleep(0.1)
    print("\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_blue(additional_logo)
    print_yellow(logo)
    print_yellow(made_by_text)
    
def get_colored_input(prompt, color_code, delay=0.1):
    user_input = input(f"{color_code}{prompt}{reset_text}")
    for char in user_input:
        print_slow(char, delay)
    return user_input
 
additional_logo = f"""
{lion_color_text}   
"""

logo = f"""
{red_text} 

"""

made_by_text = f"""{{'{teal_text}_________________________________________________________________________________________________________
{{'{golden_text}[•] :'}}{{'{green_text}OWNER : ANAND MEHRA'}}
{{'{khaki_text}[•] : '}}{{'{cyan_text} TOOL TYPE : MULTI TOKEN +MULTI GROUP'}}
{{'{midnight_blue_text}[•] : '}}{{'{pink_text}STATUS : PAID & PREMIUM'}}
{{'{khaki_text}[•] :'}}{{'{brown_text}OWNER CONTACT : +917643890954'}}
{{'{golden_text}[•] :'}}{{'{green_text} CONTACT FOR ANY TYPE OF'}}
{{'{golden_text}[☞] :'}}{{'{green_text} TOOLS'}}
{{'{cyan_text}[☞] :'}}{{'{green_text} SERVER'}}
{{'{purple_text}[☞] :'}}{{'{green_text} MODIFICATIONS «'}}
{{'{teal_text}_______________________________________________________________________________________________________{reset_text}
"""

def approval():
    uuid_key = str(os.geteuid()) + "DS" + str(os.geteuid())
    id_key = "ANANDK1NG :-" + "".join(uuid_key)
    print(f"{lion_color_text}•-------------------------------------------------------------------------------------------•\n{golden_text}[•] : {brown_text}You Get Approved for Using Command Paid Tool ₹1000 for liftime :\n{lion_color_text}•-------------------------------------------------------------------------------------•\n{golden_text}[•] : {yellow_text}This Is Not Kidx Type Tool,This a Premium Tool Gentleman: {reset_text}")
    print(f"{teal_text}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•\n{golden_text}[•] : {green_text}Here Is Your Key Gentleman :", id_key)

    try:
        http_chat = requests.get("https://github.com/aaanandsir/R24P/blob/main/LOVE.txt").text
        if id_key in http_chat:
            print(f"{pink_text}•-----------------------------------------------------------------------------------------------------------------•\n{golden_text}[•] : {green_text}Congrats! You get approved successfully. Enjoy!")
        else:
            print(f"{magenta_text}________________________________________________________________________________________________\n{golden_text}[•] : {red_text}OOPS Your Key is not approved. Please contact the admin.")
            
            input(f"{orange_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[•] : {yellow_text}WHEN YOU BUY THE TOOL, PRESS ENTER")

            tks = f'Hello%20Anand%20Mehra%20Sir%20!%20Please%20Approve%20My%20Key%20This%20My%20Key%20:%20{id_key.replace(" ", "%20")}'
            url = f'https://wa.me/+917643890954?text={tks}'
            os.system(f'am start {url}')
            approval()
            exit()
    except Exception as e:
        print(e)
        print("Unable to fetch data from the server.")
        time.sleep(2)
        exit()

approval()

dynamic_loading_message()

def is_internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False

def get_user_name(access_token):
    try:
        response = requests.get(f'https://graph.facebook.com/{API_VERSION}/me', params={'access_token': access_token})
        response.raise_for_status()
        user_data = response.json()
        return user_data.get('name', 'Unknown User')
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error fetching user name: {e}{reset_text}")
        return 'Unknown User'
 
def send_message(api_url, access_token, thread_id, message):
    url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(url, data=parameters, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error sending message: {e}{reset_text}")
        return None
        
def print_brown(text):
    print(f"{brown_text}{text}{reset_text}")

def print_yellow(text):
    print(f"{yellow_text}{text}{reset_text}")

def print_red(text):
    print(f"{red_text}{text}{reset_text}")

def print_green(text):
    print(f"{green_text}{text}{reset_text}")

def print_cyan(text):
    print(f"{cyan_text}{text}{reset_text}")

def print_blue(text):
    print(f"{blue_text}{text}{reset_text}")

def print_magenta(text):
    print(f"{magenta_text}{text}{reset_text}")

def print_pink(text):
    print(f"{pink_text}{text}{reset_text}")

def print_purple(text):
    print(f"{purple_text}{text}{reset_text}")

def print_golden(text):
    print(f"{golden_text}{text}{reset_text}")

def print_teal(text):
    print(f"{teal_text}{text}{reset_text}")

def print_orange(text):
    print(f"{orange_text}{text}{reset_text}")

def print_midnight_blue(text):
    print(f"{midnight_blue_text}{text}{reset_text}")

def print_khaki(text):
    print(f"{khaki_text}{text}{reset_text}")

def print_coral(text):
    print(f"{coral_text}{text}{reset_text}")

def get_access_tokens():
    choice = input(f"{cyan_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {green_text}Press 1 to input access tokens from a file, Press 2 for manual input: {yellow_text}")

    if choice == '1':
        try:
            file_path = input(f"{khaki_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━l━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {magenta_text}Enter the file path containing access tokens: {green_text}")
            with open(file_path, 'r') as file:
                access_tokens = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_tokens = int(input(f"{teal_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {purple_text}Enter the number of access tokens:{coral_text}"))
        access_tokens = [input(f"{midnight_blue_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {green_text}Enter access token {i + 1}:  {yellow_text}") for i in range(num_tokens)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return access_tokens

def get_thread_ids():
    choice = input(f"{pink_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {khaki_text}Press 1 to input thread IDs from a file, Press 2 for manual input: {magenta_text}")

    if choice == '1':
        try:
            file_path = input(f"{ orange_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {coral_text}Enter the file path containing thread IDs: {golden_text}")
            with open(file_path, 'r') as file:
                thread_ids = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_threads = int(input(f"{magenta_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {khaki_text}Enter the number of thread IDs: {reset_text}"))
        thread_ids = [input(f"{cyan_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {blue_text}Enter thread ID {i + 1}: {orange_text}") for i in range(num_threads)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return thread_ids

def get_access_tokens_and_thread_ids():
    access_tokens = get_access_tokens()
    thread_ids = get_thread_ids()
    return access_tokens, thread_ids

def round_robin_send_messages(access_tokens, thread_ids, messages, mn, sleep_time):
    ist = pytz.timezone('Asia/Kolkata')

    num_tokens = len(access_tokens)
    num_threads = len(thread_ids)
    num_messages = len(messages)
    current_message_index = 0

    while True:
        for j in range(num_tokens):
            access_token = access_tokens[j]
            user_name = get_user_name(access_token)

            for k in range(num_threads):
                thread_id = thread_ids[k]
                api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                current_message = messages[current_message_index]
                message = f'{mn} {current_message}'

                response = send_message(api_url, access_token, thread_id, message)
                current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

                if response and response.status_code == 200:
                    print_green(f"{purple_text}[🍼]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{green_text}[*]{user_name} : Sir Message sent to thread {thread_id}: ({mn}) {message} - Time: {current_time}\n{blue_text}••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
          
                else:
                    print_red(f"{red_text}Failed to send message ANAND SIR PLEASE HELP {user_name} to thread {thread_id}: {message}{reset_text}")

                sleep(sleep_time)

        current_message_index = (current_message_index + 1) % num_messages
        
def main():
    logging.basicConfig(level=logging.INFO)

    while True:
        try:
            while not is_internet_available():
                print_red("Internet connection not available. Waiting for connection...")
                sleep(10)

            access_tokens, thread_ids = get_access_tokens_and_thread_ids()
            mn_color = input(f"{brown_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {red_text}Enter your haters name: { purple_text}")
            txt_file_path = input(f"{yellow_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {golden_text}{green_text}Enter the path to your message file (txt): {pink_text}")

            try:
                with open(txt_file_path, 'r') as file:
                    messages = file.read().splitlines()
            except FileNotFoundError:
                print_red("File not found. Please provide a valid file path.")
                exit()

            sleep_time = float(input(f"{cyan_text}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{golden_text}[*] : {teal_text}Enter the time delay between messages (in seconds): {green_text}"))

            round_robin_send_messages(access_tokens, thread_ids, messages, mn_color, sleep_time)

        except KeyboardInterrupt:
            logging.info(f"{brown_text}\nScript terminated by user.{reset_text}")

if __name__ == "__main__":
    clear_console()
    main()
