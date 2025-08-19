import random
import discord
from discord.ext import commands
from discord import app_commands

QUOTES = [
    "A vida é 10% o que acontece a você e 90% como você reage.",
    "Faça o teu melhor, na condição que você tem, enquanto você não tem condições melhores para fazer melhor ainda.",
    "A persistência é o caminho do êxito.",
    "Você é mais forte do que imagina."
]

class Entertainment(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="quote", description="Receba uma citação aleatória.")
    async def quote(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(QUOTES))

    @app_commands.command(name="dice", description="Rola um dado de N lados (padrão 6).")
    async def dice(self, interaction: discord.Interaction, sides: int = 6):
        if sides < 2 or sides > 1000:
            return await interaction.response.send_message("Escolha entre 2 e 1000 lados.", ephemeral=True)
        await interaction.response.send_message(f"🎲 Você rolou: **{random.randint(1, sides)}**")

async def setup(bot: commands.Bot):
    await bot.add_cog(Entertainment(bot))
