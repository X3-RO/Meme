import os
import random
import requests
import subprocess
import uuid
import time
from datetime import datetime

# Function to clear the terminal
def clear():
    os.system('clear')

# Function to simulate 'clear' behavior
def back():
    login()

# Simplified login function
def login():
    try:
        token = open('.token.txt', 'r').read()
        response = requests.get(f'https://graph.facebook.com/me?access_token={token}')
        if response.status_code == 200:
            public_menu()
        else:
            print("Login failed.")
    except requests.exceptions.RequestException:
        print("Connection error.")
        clear()

# Refactored device info gathering
def get_device_info():
    device_info = {
        'android_version': subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').strip(),
        'model': subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip(),
        'build': subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').strip(),
        'manufacturer': subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').strip(),
        'brand': subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').strip(),
        'cpu_abilist': subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').strip(),
        'density': subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').strip(),
    }
    return device_info

# Generate random user agents for the request
def generate_user_agents():
    user_agents = []
    for _ in range(5000):
        a1 = f'[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randint(20, 49)}{random.randint(11, 99)};FBBV/{random.randint(11111111, 77777777)};'
        a2 = f'[FBAN/Orca-Android;FBAV/{random.randint(199, 399)}.0.0.{random.randint(1, 9)}.{random.randint(99, 199)};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{random.randint(111111111, 999999999)};FBCR/'
        user_agents.append(a1 + a2)
    return user_agents

# Sample placeholder function for displaying public menu
def public_menu():
    print("Welcome to the public menu.")

# Running the program
if __name__ == "__main__":
    device_info = get_device_info()
    print(f"Device Info: {device_info}")
    
    user_agents = generate_user_agents()
    print(f"Generated {len(user_agents)} user agents.")
    
    login()
