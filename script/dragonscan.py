# coding: latin-1
#if you use this code give me credit @tuf_unkn0wn
#i do not give you permission to edit this script without my credit
#to ask questions or report a problem message me on instagram @tuf_unkn0wn
import os
import sys
import socks
import socket
import requests
#COLOR VARIABLES START#
#---------------------#
r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
Bl = '\033[30m'
O = '\033[33m'
p = '\033[35m'
BD = '\033[1m'
#-------------------#
#COLOR VARIABLES END#

if len(sys.argv) < 2:
	print """\033[31m
                ___====-_                                    _-====___
           _--^^^#####//                                      \\#####^^^--_
        _-^##########//                                        \\##########^-_
       -############//      ┌┬┐┬─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┐┌      \\############-
     _/############//        ││├┬┘├─┤│ ┬│ ││││└─┐│  ├─┤│││       \\#############_
    /#############((        ─┴┘┴└─┴ ┴└─┘└─┘┘└┘└─┘└─┘┴ ┴┘└┘        ))#############
   -###############\\                                            //###############-
  -#################\\                                          //#################-
 -###################\\                                        //###################-
_#/|##########/\######(                                        )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\                                        /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\|                                      |/#/  V   '  V  V  \|  '
   `   `  `      `   / |                                      | \   '      '  '   '
                                 \033[0m\033[1mHelp: dragonscan -h
\033[0m"""
	sys.exit (1)

if sys.argv[1] == "-h":
	print """
\033[31m
                ___====-_                                    _-====___
           _--^^^#####//                                      \\#####^^^--_
        _-^##########//                                        \\##########^-_
       -############//      ┌┬┐┬─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┐┌      \\############-
     _/############//        ││├┬┘├─┤│ ┬│ ││││└─┐│  ├─┤│││       \\#############_
    /#############((        ─┴┘┴└─┴ ┴└─┘└─┘┘└┘└─┘└─┘┴ ┴┘└┘        ))#############
   -###############\\                                            //###############-
  -#################\\                                          //#################-
 -###################\\                                        //###################-
_#/|##########/\######(                                        )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\                                        /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\|                                      |/#/  V   '  V  V  \|  '
   `   `  `      `   / |                                      | \   '      '  '   '\033[0m

\033[1mDRAGONSCAN HELP:\033[0m
  |\033[32mCOMMAND\033[0m|     |\033[32mUSAGE\033[0m|                        [\033[32mDESCRIPTION\033[0m]

    -pts,    [-pts target]                  simple nmap portscan

    -doc,    [-doc target]                  show document info of target with curl
 
    -nall,   [-nall target]                 nmap OS detection, version detection, script scanning, and traceroute scan

    -dnsbr,  [-dnsbr target]                nmap dns bruteforce

    -wti,    [-wti target]                  get a hosts ip address

    -oni,    [-oni target]                  check if a host is online (\033[33minclude http:// or https://\033[0m)

    -whois,  [-whois target]                who-is lookup

    -dnsup,  [-dnsup target]                dns-lookup

    -src,    [-src target]                  get a hosts source code

    -dd,     [-dd]                          scan for devices on your network

    -nd,     [-nd]                          scan for networks around you

    -becap,  [-becap]                       run the mitm tool bettercap
                                                                                                 
    -waf,    [-waf target]                  web application firewall scanner

    -dirb,   [-dirb target]                 run a directory bruteforce on a host (\033[33minclude http:// or https://\033[0m)

    -ssls,   [-ssls target]                 run a ssl scan

    -geoip,  [-geoip target]                find the location of a ip address
"""

if sys.argv[1] == "-pts":
	os.system("nmap {0}".format(sys.argv[2]))

if sys.argv[1] == "-doc":
	os.system("curl -I {0}".format(sys.argv[2]))

if sys.argv[1] == "-nall":
	os.system("nmap -A {0}".format(sys.argv[2]))

if sys.argv[1] == "-dnsbr":
	os.system("nmap --script dns-brute {0}".format(sys.argv[2]))

if sys.argv[1] == "-wti":
	ip = socket.gethostbyname(sys.argv[2])
	print G+"------------------------\033[0m"
	print N+"\033[1mHost:\033[32m ", sys.argv[2]
	print N+"\033[1mIP:\033[32m ", ip
	print G+"------------------------\033[0m"

if sys.argv[1] == "-dd":
	os.system("netdiscover")

if sys.argv[1] == "-oni":
	request = requests.get(sys.argv[2])
	http = request.status_code
	if http == 200:
		print("\t Server: [\033[32monline\033[0m]")
	else:
		print("\t Server: [\033[31moffline\033[0m]")
		exit()

if sys.argv[1] == "-whois":
	whois = requests.get("https://api.hackertarget.com/whois/?q=" + sys.argv[2]).content.decode("UTF-8")
	print(whois)

if sys.argv[1] == "-dnsup":
	os.system("curl https://api.hackertarget.com/dnslookup/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-nd":
	os.system("iwconfig")
	m = raw_input("Select Interface: ")
	os.system("airmon-ng start " + m)
	print Y+"WOULD YOU LIKE TO SAVE YOUR SCAN RESULTS?\033[0m"
	j = raw_input("[y/n]> ")
	if j == "y":
		os.system("airodump-ng -w /root/SCAN " + m)
		os.system("airmon-ng stop " + i)
		print Y+"! SCAN RESULTS SAVED IN /root/ DIRECTORY !\033[0m"
	if j == "n":
		os.system("airodump-ng " + m)
		os.system("airmon-ng stop " + i)

if sys.argv[1] == "-becap":
	os.system("bettercap")

if sys.argv[1] == "-src":
	print Y+"\nWould you like to save source code in a file?\n\033[0m"
	q = raw_input(R+"[y/n]:\033[0m ")
	if q == "n":
		an = 'curl {0}'.format(sys.argv[2])
		os.system(an)
	if q == "y":
		ay = 'curl {0} >> /root/{1}.txt'.format(sys.argv[2],sys.argv[2])
		os.system(ay)
		print Y+"\nfile saved > /root/{0}.txt\033[0m".format(sys.argv[2])

if sys.argv[1] == "-waf":
	os.system("wafw00f {0}".format(sys.argv[2]))

if sys.argv[1] == "-dirb":
	os.system("dirb {0}".format(sys.argv[2]))

if sys.argv[1] == "-ssls":
	os.system("sslscan {0}".format(sys.argv[2]))

if sys.argv[1] == "-geoip":
	print "\033[32m---------------------------------\033[0m\033[1m"
	os.system("curl https://api.hackertarget.com/geoip/?q={0}".format(sys.argv[2]))
	print "\n\033[0m\033[32m---------------------------------\033[0m"
