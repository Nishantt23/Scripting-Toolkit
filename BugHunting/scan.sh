#!/bin/bash

#Nmap Scan
#echo "[+] Scanning for Open Ports and Services ..."
#rustscan -a $1 -p 135,139,80,445 -- -sC -sV -oN portscan

#Directory Bruteforcing
echo "[+] Scanning for Hidden Directories, Files ..."
gobuster dir -u $1 -w /usr/share/dirb/wordlists/common.txt -t 100 --timeout 60s -q -o directories
 
echo "Done!"
