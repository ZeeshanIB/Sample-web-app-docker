#!/bin/bash

# Functions to display and change network settings
display_network_settings() {
  # Display current network settings
  ip addr show
  echo ""
  route -n
  echo ""
  cat /etc/resolv.conf
}

change_network_settings() {
  # Get interface name
  read -p "Enter interface name: " interface
  
  # Get IP address
  read -p "Enter IP address: " ip_address
  
  # Get netmask
  read -p "Enter netmask: " netmask
  
  # Get gateway
  read -p "Enter gateway: " gateway
  
  # Get DNS
  read -p "Enter DNS server: " dns
  
  # Set the IP address, netmask, and gateway for the interface
  ip addr add $ip_address/$netmask dev $interface
  ip route add default via $gateway dev $interface
  
  # Set the DNS server
  echo "nameserver $dns" > /etc/resolv.conf
}

# Function to restart networking
restart_networking() {
  systemctl restart NetworkManager
  
}

# Function to set the date and time
set_date_time() {
  # Get current date and time
  date_time=$(date)
  echo "Current date and time: $date_time"
  
  # Set new date and time
  read -p "Enter new date and time (format: YYYY-MM-DD HH:MM:SS): " new_date_time
  date -s "$new_date_time"
}

# Function to shutdown the system
shutdown_system() {
  shutdown -h now
}

# Function to reboot the system
reboot_system() {
  reboot
}

# Function to logout
logout() {
  pkill -KILL -u $USER
}

# Menu
while true; do
  # Display menu
  echo "Menu:"
  echo "1. View Network Settings"
  echo "2. Change Network Settings"
  echo "3. Restart Networking"
  echo "4. Set Date and Time"
  echo "5. Shutdown"
  echo "6. Reboot"
  echo "7. Logout"
  
  
  # Read user input
  read -p "Enter your choice: " choice
  
  # Perform the selected task
  case $choice in
    1) display_network_settings;;
    2) change_network_settings;;
    3) restart_networking;;
    4) set_date_time;;
    5) shutdown_system;;
    6) reboot_system;;
    7) logout;;
    
    *) echo "Invalid choice";;
  esac
done
