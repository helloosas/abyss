import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")

bot.load_extension("selam_cog")

bot.run("MTA4NTkxMzUzOTE4MjYwNDMyOA.G09k_0.hjDlnCG07ih129k3e3O0cdq3IVex-eOhhkD6YA")
