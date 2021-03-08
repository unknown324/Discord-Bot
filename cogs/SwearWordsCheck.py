import discord
from discord.ext import commands
from pathlib import Path


def root() -> Path:
	return Path(__file__).parent.parent
class Security(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.counter = 0

	@commands.Cog.listener()
	async def on_message(self, msg):
		with open(str(root())+'\\words.txt', "r+") as f:
			wrd = f.readlines()
			for ow in wrd:
				words = ow.strip("\n")
				if words in msg.content:
					await msg.delete()
					await msg.channel.send(f"Warning!{msg.author.mention} don't use offensive words or you will be kicked from the server!")
					self.counter += 1
					if self.counter > 2:
						await msg.guild.kick(msg.author)
						await msg.channel.send(f"{msg.author} has been kicked from the server for using offensive words")
						self.counter = 0
	@commands.Cog.listener()
	async def error(self, err):
		if isinstance(err, commands.MissingMessage):
			pass

def setup(client):
	client.add_cog(Security(client))