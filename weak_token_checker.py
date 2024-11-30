import hashlib
from datetime import datetime
from itertools import permutations
from colorama import Fore, Back, Style, init

##################################################################################################################
# ASCII art banner
##################################################################################################################
def banner():
    print("""
          
░█░█░█▀▀░█▀█░█░█░░░█▀▀░█▀▀░█▀▄░█▀▀░░░▀█▀░█▀█░█▀█░█░█░█▀▀░█▀█░░░▀█▀░█▀▀░█▀▀░▀█▀░█▀▀░█▀▄
░█▄█░█▀▀░█▀█░█▀▄░░░█░░░▀▀█░█▀▄░█▀▀░░░░█░░█░█░█░█░█▀▄░█▀▀░█░█░░░░█░░█▀▀░▀▀█░░█░░█▀▀░█▀▄
░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀░░░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀ v.1.0
          """)


##################################################################################################################
# Generator for all potential possible combinations
##################################################################################################################
def generate_combinations(known_values):
    combinations = {}

    # Create common date formats
    now = datetime.now()
    dates = {}
    dates["date('YYYY-MM-DD')"] = now.strftime("%Y-%m-%d")
    dates["date('MM/DD/YYYY')"] = now.strftime("%m/%d/%Y")
    dates["date('DD/MM/YYYY')"] = now.strftime("%d/%m/%Y")
    dates["date('DD.MM.YYYY')"] = now.strftime("%d.%m.%Y")
    dates["date('YYYYMMDD')"]   = now.strftime("%Y%m%d")

    dates["date('YYYY-MM')"]    = now.strftime("%Y-%m")
    dates["date('YYYY/MM')"]    = now.strftime("%Y/%m")
    dates["date('MM/YYYY')"]    = now.strftime("%m/%Y")
    dates["date('YYYYMM')"]     = now.strftime("%Y%m")

    dates["date('YYYY')"]       = now.strftime("%Y")
    dates["date('MM')"]         = now.strftime("%m")
    dates["date('DD')"]         = now.strftime("%d")

    # Common seperators
    separators = ["", " ", ",", ";", "-", "/", "|", "$", ":", "::", "%", "_", "*", "#"]

    # Generate all permutations of all lengths from 2 to the total number of elements
    for date_format, date_str in dates.items():
        keys   = list(known_values.keys())
        values = list(known_values.values())

        # Add date
        keys.append(date_format)
        values.append(date_str)

        for r in range(1, len(keys) + 1):
            for perm_indices in permutations(range(len(keys)), r):
                for sep in separators:
                    combined_values = f"{sep}".join(values[i] for i in perm_indices)
                    format_desc = f"+'{sep}'+".join(keys[i] for i in perm_indices).replace("+''+", "+")
                    combinations[format_desc] = combined_values
    
    return combinations


##################################################################################################################
# Check function 
##################################################################################################################
def check_token(value, token):
    value_bytes = value.encode('utf-8')    
    
    # List of hashing algorithms supported by hashlib
    hash_algorithms = [ 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 
        'sha3_256', 'sha3_384', 'sha3_512', 'blake2b', 'blake2s', 'shake_128', 'shake_256' ]
    
    # Calculate each hash and test token
    for algorithm in hash_algorithms:
        if algorithm.startswith('shake'):  # shake requires a length parameter
            hash_value = getattr(hashlib, algorithm)(value_bytes).hexdigest(64)
        else:
            hash_value = getattr(hashlib, algorithm)(value_bytes).hexdigest()
        
        if hash_value == token:
            return algorithm
    
    return False

##################################################################################################################
# Main programm 
##################################################################################################################
if __name__ == "__main__":
    banner()
    known_values = {}
    questions = ["ID", "loginname", "email"]

    # Initialize colorama 
    init(autoreset=True) 

    # Get known values for the generator
    for q in questions:
        val = input(f"Enter user {Style.BRIGHT}{q}{Style.RESET_ALL} or leave blank for unknown value: ").strip()
        if val != "":
            known_values[q] = val

    # Get token value
    NEEDLE = input(f"Enter CSRF token: ").strip()
    print()

    # Generate combinations
    HAYSATCK = generate_combinations(known_values)

    # Test and print the results
    for format_desc, val in HAYSATCK.items():
        found = check_token(val, NEEDLE)
        if not found:
            print(f"[-] TESTING :: {format_desc:60} == {Fore.RED}FAIL!")
        else:
            print(f"{Style.BRIGHT}{Fore.GREEN}[+] TESTING :: {format_desc:60} == {found}({format_desc})")
            break

    print("DONE!")