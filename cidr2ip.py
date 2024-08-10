import ipaddress
import os
import sys

# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cidr_to_ip_list(cidr):
    try:
        ip_net = ipaddress.ip_network(cidr.strip(), strict=False)
        return [str(ip) for ip in ip_net]
    except ValueError as e:
        print(f"{Colors.FAIL}Error: {e}{Colors.ENDC}")
        return []

def save_ips_to_file(ip_list, filename):
    with open(filename, 'w') as file:
        for ip in ip_list:
            file.write(ip + '\n')

def append_ips_to_file(ip_list, filename):
    with open(filename, 'a') as file:
        for ip in ip_list:
            file.write(ip + '\n')

def print_banner():
    banner = f"""
{Colors.OKBLUE}▒█▀▀█ ▀█▀ ▒█▀▀▄ ▒█▀▀█ 　 █▀█ 　 ▀█▀ ▒█▀▀█ 
▒█░░░ ▒█░ ▒█░▒█ ▒█▄▄▀ 　 ░▄▀ 　 ▒█░ ▒█▄▄█ 
▒█▄▄█ ▄█▄ ▒█▄▄▀ ▒█░▒█ 　 █▄▄ 　 ▄█▄ ▒█░░░

                                                                                   ᴮʸ ⁻ ᴬʸᵃⁿ ᴿᵃʲᵒᵒᵗ{Colors.ENDC}
    """
    print(banner)

def validate_cidr(cidr):
    try:
        ipaddress.ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False

def main():
    print_banner()
    print(f"{Colors.OKGREEN}Welcome to the CIDR to IP Converter{Colors.ENDC}")
    
    total_ip_count = 0
    
    while True:
        print("\nMenu:")
        print(f"{Colors.OKBLUE}1. Input a single CIDR{Colors.ENDC}")
        print(f"{Colors.OKBLUE}2. Input multiple CIDRs{Colors.ENDC}")
        choice = input("Choose an option (1 or 2): ").strip()
        
        if choice == '1':
            cidr = input(f"{Colors.WARNING}Enter a CIDR (e.g., 192.168.1.0/24): {Colors.ENDC}").strip()
            if not validate_cidr(cidr):
                print(f"{Colors.FAIL}Invalid CIDR format. Please try again.{Colors.ENDC}")
                continue
            ip_list = cidr_to_ip_list(cidr)
            total_ip_count += len(ip_list)
            filename = input(f"{Colors.WARNING}Enter the filename to save IP addresses (e.g., ip_addresses.txt): {Colors.ENDC}").strip()
            save_ips_to_file(ip_list, filename)
            print(f"{Colors.OKGREEN}IP addresses for {cidr} saved to {filename}{Colors.ENDC}")
            break
        
        elif choice == '2':
            input_method = input(f"{Colors.WARNING}Do you want to input CIDRs manually or provide a file? (manual/file): {Colors.ENDC}").strip().lower()
            
            if input_method == 'manual':
                cidrs = input(f"{Colors.WARNING}Enter CIDR(s) separated by a comma (e.g., 192.168.1.0/24,10.0.0.0/8): {Colors.ENDC}").split(',')
                cidrs = [cidr.strip() for cidr in cidrs]
            
            elif input_method == 'file':
                file_path = input(f"{Colors.WARNING}Enter the path to the text file containing CIDRs: {Colors.ENDC}").strip()
                if not os.path.isfile(file_path):
                    print(f"{Colors.FAIL}Error: The file {file_path} was not found.{Colors.ENDC}")
                    continue
                with open(file_path, 'r') as file:
                    cidrs = [line.strip() for line in file if line.strip()]
            
            else:
                print(f"{Colors.FAIL}Invalid input method. Please run the program again and choose either 'manual' or 'file'.{Colors.ENDC}")
                continue

            save_option = input(f"{Colors.WARNING}Do you want to save the results to the same file or different files? (same/different): {Colors.ENDC}").strip().lower()
            
            if save_option == 'same':
                filename = input(f"{Colors.WARNING}Enter the filename to save all IP addresses (e.g., ip_addresses.txt): {Colors.ENDC}").strip()
                if os.path.isfile(filename):
                    confirm = input(f"{Colors.WARNING}File {filename} already exists. Do you want to overwrite it? (yes/no): {Colors.ENDC}").strip().lower()
                    if confirm != 'yes':
                        print(f"{Colors.INFO}Operation aborted.{Colors.ENDC}")
                        continue
                
                with open(filename, 'w') as file:
                    file.write("")  # Clear file content
                
                for cidr in cidrs:
                    if not validate_cidr(cidr):
                        print(f"{Colors.FAIL}Skipping invalid CIDR: {cidr}{Colors.ENDC}")
                        continue
                    ip_list = cidr_to_ip_list(cidr)
                    total_ip_count += len(ip_list)
                    append_ips_to_file(ip_list, filename)
                    print(f"{Colors.OKGREEN}Processed {cidr}. IP addresses appended to {filename}.{Colors.ENDC}")
                
                print(f"{Colors.OKGREEN}All IP addresses saved to {filename}{Colors.ENDC}")
            
            elif save_option == 'different':
                for cidr in cidrs:
                    if not validate_cidr(cidr):
                        print(f"{Colors.FAIL}Skipping invalid CIDR: {cidr}{Colors.ENDC}")
                        continue
                    ip_list = cidr_to_ip_list(cidr)
                    total_ip_count += len(ip_list)
                    filename = input(f"{Colors.WARNING}Enter the filename to save IP addresses for {cidr} (e.g., ip_addresses_{cidr.replace('/', '_')}.txt): {Colors.ENDC}").strip()
                    save_ips_to_file(ip_list, filename)
                    print(f"{Colors.OKGREEN}IP addresses for {cidr} saved to {filename}{Colors.ENDC}")
            
            else:
                print(f"{Colors.FAIL}Invalid option. Please run the program again and choose either 'same' or 'different'.{Colors.ENDC}")
                continue
        
        else:
            print(f"{Colors.FAIL}Invalid choice. Please run the program again and choose either 1 or 2.{Colors.ENDC}")
            continue
        
        break
    
    # Display the total number of IP addresses saved
    print(f"{Colors.OKGREEN}Total number of IP addresses saved: {total_ip_count}{Colors.ENDC}")

if __name__ == "__main__":
    main()
