import discord
from discord.ext import commands
from discord import app_commands

class Integration(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Cria uma enquete simples com duas opções.")
    async def poll(self, interaction: discord.Interaction, pergunta: str, opcao1: str, opcao2: str):
        embed = discord.Embed(title="Enquete", description=pergunta)
        embed.add_field(name="1️⃣", value=opcao1, inline=False)
        embed.add_field(name="2️⃣", value=opcao2, inline=False)
        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await interaction.response.send_message("Enquete criada!", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Integration(bot))
