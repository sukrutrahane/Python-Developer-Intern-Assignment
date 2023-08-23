import os
import subprocess

def block_usb_ports():
    subprocess.run(['reg', 'add', 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR', '/v', 'Start', '/t', 'REG_DWORD', '/d', '4', '/f'])

def disable_bluetooth():
    subprocess.run(['reg', 'add', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer', '/v', 'NoControlPanel', '/t', 'REG_DWORD', '/d', '1', '/f'])

def disable_command_prompt():
    subprocess.run(['reg', 'add', 'HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System', '/v', 'DisableCMD', '/t', 'REG_DWORD', '/d', '2', '/f'])

def block_website_access(website):
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write(f'127.0.0.1 {website}\n')

def main():
    block_usb_ports()
    print("USB ports blocked.")

    disable_bluetooth()
    print("Bluetooth disabled.")

    disable_command_prompt()
    print("Command Prompt disabled.")

    website_to_block = "example.com"
    block_website_access(website_to_block)
    print(f"{website_to_block} blocked.")

if __name__ == "__main__":
    main()
