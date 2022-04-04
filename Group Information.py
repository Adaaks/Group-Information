
try:
	import time
	import requests
	import os
	os.system('cls')
	from colorama import init, Fore, Back, Style
	init()
except ImportError:
	print("[ERROR] Failed to import some modules, install the required modules listed:\n- requests\n- colorama\n\nThese can be installed via going to the cmd, and typing pip install (moduleName)")
	time.sleep(5)
	quit()
def begin():

	print(Fore.CYAN + "\n-------------------------\n\nGroup Information\n\n[1] = Group ID Search\n[2] = Group Name Search\n")
	try:
		method = int(input(Fore.WHITE + "Method: "))
	except:
		print(f'{Fore.RED}[ERROR] You must input either 1 or 2!')
		time.sleep(1)
		begin()

	if method == 1:

		def my1():

			try:
				group = int(input(Fore.WHITE +"Enter Group ID: "))
			except:
				print(f'{Fore.RED}[ERROR] Please input only numbers - not characters!')
				time.sleep(1)
				begin()

			print("")
			print(Fore.CYAN +"-------------------------\n")

			r = requests.get("https://groups.roblox.com/v1/groups/"+str(group))
			request = r.json()

			getcreation = requests.get(f"https://groups.roblox.com/v2/groups?groupIds={group}")
			try:

				getcreation2 = getcreation.json()
				creationdate = getcreation2['data'][0]['created']
			except:
				print(f'{Fore.RED}[ERROR] Group not found!')
				time.sleep(1)
				begin()

			try:
				ownerid5 = request['owner']['userId']
				username = request['owner']['username']
				displayname = request['owner']['displayName']
				fulluser = f'{displayname} (@{username})'
			except:
				fulluser = "Nobody"
				ownerid5 = "0"

			name = request['name']
			members = request['memberCount']
			entry = request['publicEntryAllowed']
			try:
				shout = request['shout']['body']
			except:
				shout = "None"
			if not shout:
				shout = "None"

			if entry == True:
				entry = "Public"
			else:
				entry = "Private"

			print(f'{Fore.GREEN}Owner: {Fore.YELLOW}{fulluser}')
			print(f'{Fore.GREEN}Owner ID: {Fore.YELLOW}{ownerid5}\n')
			print(f'{Fore.GREEN}Group: {Fore.YELLOW}{name}')
			print(f'{Fore.GREEN}Group ID: {Fore.YELLOW}{group}')
			print(f'{Fore.GREEN}Members: {Fore.YELLOW}{members}')
			print(f'{Fore.GREEN}Shout: {Fore.YELLOW}{shout}')
			print(f'{Fore.GREEN}Entry: {Fore.YELLOW}{entry}')
			print(f'{Fore.GREEN}Created: {Fore.YELLOW}{creationdate}')
			begin()
		my1()

	if method == 2:

		def my2():

			namesearch = str(input(Fore.WHITE + "Enter Group Name: "))
			print("")
			print(Fore.CYAN + "-------------------------\n")
			
			namebase = requests.get(f"https://groups.roblox.com/v1/groups/search/lookup?groupName={namesearch}")
			getnames = namebase.json()
			try:
				selected = getnames['data'][0]['id']
			except IndexError:
				print(f'{Fore.RED}[ERROR] Group not found!')
				begin()
			
			getcreation = requests.get(f"https://groups.roblox.com/v2/groups?groupIds={selected}")
			getcreation2 = getcreation.json()
			creationdate = getcreation2['data'][0]['created']
			r = requests.get("https://groups.roblox.com/v1/groups/"+str(selected))
			request = r.json()
			
			try:
				ownerid1 = request['owner']['userId']
				username = request['owner']['username']
				displayname = request['owner']['displayName']
				fulluser = f'{displayname} (@{username})'
			except:
				fulluser = "Nobody"
				ownerid1 = "0"

			name = request['name']
			members = request['memberCount']
			entry = request['publicEntryAllowed']
			try:
				shout = request['shout']['body']
			except:
				shout = "None"
			if not shout:
				shout = "None"

			if entry == True:
				entry = "Public"
			else:
				entry = "Private"

			print(f'{Fore.GREEN}Owner: {Fore.YELLOW}{fulluser}')
			print(f'{Fore.GREEN}Owner ID: {Fore.YELLOW}{ownerid1}\n')
			
			print(f'{Fore.GREEN}Group: {Fore.YELLOW}{name}')
			print(f'{Fore.GREEN}Group ID: {Fore.YELLOW}{selected}')
			print(f'{Fore.GREEN}Members: {Fore.YELLOW}{members}')
			print(f'{Fore.GREEN}Shout: {Fore.YELLOW}{shout}')
			print(f'{Fore.GREEN}Entry: {Fore.YELLOW}{entry}')
			print(f'{Fore.GREEN}Created: {Fore.YELLOW}{creationdate}')
			begin()
		my2()

	else:
		print(f'{Fore.RED}[ERROR] You must input either 1 or 2!')
		time.sleep(1)
		begin()
begin()
	
