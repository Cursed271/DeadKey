# ----- License -------------------------------------------------- # 

#  DeadKey - DeadKey simulates keylogging attacks to test EDR systems, enabling users to strengthen their defense strategies.
#  Copyright (c) 2025 - Steven Pereira aka Cursed.

#  This software is an open-source cybersecurity tool developed for
#  penetration testing, threat modeling, and security research. It   
#  is licensed under the MIT License, allowing free use, modification, 
#  and distribution under the following conditions:
#
#  You MUST include this copyright notice in all copies.
#  You MAY use this software for personal or educational purposes ONLY.
#  This software is provided "AS IS," WITHOUT WARRANTY of any kind. 
#  You MAY NOT use this software for any illegal or unauthorized activity.

#  DISCLAIMER:
#  This tool is intended for **educational or ethical testing** purposes only.
#  Unauthorized or malicious use of this software against systems without 
#  proper authorization is strictly prohibited and may violate laws and regulations.
#  The author assumes no liability for misuse or damage caused by this tool.

#  🔗 License: MIT License
#  🔗 Repository: https://github.com/Cursed271
#  🔗 Author: Steven Pereira (@Cursed271)

# ----- Libraries ------------------------------------------------ #

import os
import socket
import threading
from datetime import datetime
from rich.console import Console

# ----- Global Declaration --------------------------------------- #

PORT = 2701
HOST = "127.0.0.1"
console = Console()
LOG = "deadkey_logs.txt"

# ----- Client Connection ---------------------------------------- #

def handle_client(conn, addr):
	console.print(f"[bold green][+] Connection established from {addr}...")
	with conn, open(LOG, "a") as logfile:
		while True:
			try:
				data = conn.recv(1024)
				if not data:
					break
				message = data.decode("utf-8")
				timestamped = f"{datetime.now()} - {addr} - {message}"
				console.print(f"[#C6ECE3]{timestamped}")
				logfile.write(timestamped + "\n")
				logfile.flush()
			except ConnectionResetError:
				console.print(f"[red][!] Connection closed from {addr}...")
			except KeyboardInterrupt:
				console.print(f"[red][!] Ctrl+C detected. Shutting down C2 server...")
			except Exception as e:
				console.print(f"[red][!] Error: {e}")
	console.print(f"[red][!] Connection closed from {addr}...")

# ----- C2 Server Initiation ------------------------------------- #

def key_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOST, PORT))
	server.listen()
	console.print(f"[#C6ECE3][+] DeadKey listening on {HOST}:{PORT}")
	while True:
		conn, addr = server.accept()
		client_thread = threading.Thread(target=handle_client, args=(conn, addr))
		client_thread.start()

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
	key_server()
	console.print("[#C6ECE3]+--------------------------------------------------------------+")

# ----- End ------------------------------------------------------ #