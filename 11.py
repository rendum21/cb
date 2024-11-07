import socket

def dns_lookup():
    print("DNS Lookup Tool")
    print("Enter '1' to look up IP for a URL")
    print("Enter '2' to look up URL for an IP address")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        url = input("Enter the URL (e.g., example.com): ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address of {url} is {ip_address}")
        except socket.gaierror:
            print("Invalid URL or unable to resolve IP.")
    elif choice == '2':
        ip_address = input("Enter the IP address (e.g., 93.184.216.34): ")
        try:
            host_name = socket.gethostbyaddr(ip_address)[0]
            print(f"The URL for IP address {ip_address} is {host_name}")
        except socket.herror:
            print("Invalid IP address or unable to resolve URL.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    dns_lookup()
