import socket
import termcolor

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored(f'[+] {port} port open', 'cyan'))
        sock.close()
    except:
        print(termcolor.colored(f'[-] {port} port closed', 'red'))

def scan(target, ports):
    t = target.split(',')
    for ip in t:
        print(termcolor.colored(f'Scanning {ip.strip()}...', 'green'))
        for p in range(1, int(ports) + 1):  
            scan_port(ip.strip(), p)

target = input("* Enter target(s) to scan (if you want multiple, split by ','): ")
port = input("* Enter how many ports you want to scan (e.g., 1-100): ")

scan(target, port)
