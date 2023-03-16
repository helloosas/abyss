import discord
from discord.ext import commands
from random import choice

class SelamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            print(str(message.author) + ": " + str(message.content))
        except Exception:
            print(str(message.author) + ":")

        if "sa" in message.clean_content.lower():
            await message.channel.send(choice(["ALEYKÜM SELAM", "as", "as kardeşim"]))

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(SelamCog(bot))
