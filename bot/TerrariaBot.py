# Author: Jake Bringham

import discord
import subprocess as sp
import re
import os

class TerrariaClient(discord.Client): # Inheritance in Python

	def __init__(self, ops):
		super().__init__()
		self.ops = ops
	# This likely isn't perfect but it'll stop the normal user
	# Nitro users may be able to circumvent by naming themself as you
	def is_op(self, user):
		for op in self.ops:
			if str(user) == op:
				print(op + " == " + str(user));
				return True
			else:
				print(op + " != " + str(user));
		return False

	def get_server_status(self):
		output = sp.run(["screen", "-ls"], stdout=sp.PIPE)
		return re.search("terraria_server", str(output)) != None

	# Discord event fires when bot is online
	async def on_ready(self):
		print('Logged on as {0}.'.format(self.user))

	# Discord event fires when it can see a new message
	async def on_message(self, message):
		"""
		Attempts to parse a command from the message the bot received.
		"""
		
		print('Messages from {0.author}: {0.content}'.format(message))
		
		if not message.content.startswith("!terraria"):	
			return
	
		command = re.split("\s", message.content)
		
		
		if len(command) <= 1:
			await message.add_reaction("\u274C")
			return
		if command[1] == "status":
			await self.output_terraria_server_status(message.channel)
		elif command[1] == "help":
			await self.output_help(message.channel)
		elif command[1] == "start":
			await self.start_server(message.channel)
		elif command[1] == "save":
			self.run_server_command(command[1])					
		elif command[1] == "dawn":
			self.run_server_command(command[1])					
		elif command[1] == "noon":
			self.run_server_command(command[1])					
		elif command[1] == "dusk":
			self.run_server_command(command[1])					
		elif command[1] == "night":
			self.run_server_command("midnight")					
		elif command[1] == "exit":
			if self.is_op(message.author):
				self.run_server_command(command[1])
			else:
				await message.add_reaction("\U0001f6d1")
				return	
		else:
			await message.add_reaction("\u274C")
			return	
		await message.add_reaction("\u2705")

	async def output_terraria_server_status(self, channel):
		if self.get_server_status():
			await channel.send("The Terraria Server is **Online** :white_check_mark:")
		else:
			await channel.send("The Terraria Server is **Offline** :x:")

	def run_server_command(self, command):
		os.system('screen -S terraria_server -X stuff "' + command + '\n"')	

	async def output_help(self, channel):
		await channel.send((
		"Prefix your commands with **!terraria**\n"
		"\t*help*   - Outputs this help message\n"
		"\t*status* - Tells you whether or not the server is online\n"
		"\t*start*  - Starts the server if it is offline\n"
		"\t*save*   - Runs a save on the server\n"
		"\t*dawn*   - Sets the ingame time to Dawn (start of day)\n"
		"\t*noon*   - Sets the ingame time to Noon\n"
		"\t*dusk*   - Sets the ingame time to Dusk (start of night)\n"
		"\t*night*  - Sets the ingame time to midnight\n"
		))
	
	async def start_server(self, channel):
		if self.get_server_status():
			await channel.send("The Server is already **Online**")
		else:
			# Figure out way to do relative path instead
			os.system("/home/jake/game_servers/terraria/1405/start.sh")
			await channel.send("Starting server...")


ops = open("ops.txt", "r").read().splitlines()
client = TerrariaClient(ops)


for op in client.ops:
	print(op)

token = open("token.txt", "r")

client.run(token.read())






