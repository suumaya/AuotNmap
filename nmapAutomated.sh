#! /bin/bash
target='192.168.100.16'


Echo ''
Echo ''

Echo ' ************************* Auto-Nmap Analyzer Started ************************* '
Echo ''
Echo ''
{
echo -ne '#####                     (33%)\r'
sleep 1
echo -ne '#############             (66%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'
Nmap ${target}

}
Echo ''
Echo ''

Echo ' ************************* Auto-Nmap Analyzer Done ************************* '
Echo ''
Echo ''
