import discord
from discord.ext import commands
from discord import app_commands
from collections import defaultdict

class Advanced(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.levels = defaultdict(int)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return
        self.levels[message.author.id] += 1

    @app_commands.command(name="level", description="Mostra seu nível baseado em mensagens enviadas.")
    async def level(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        lvl = self.levels.get(user_id, 0) // 10
        await interaction.response.send_message(f"Seu nível atual é **{lvl}**.")

    @app_commands.command(name="economy", description="Mostra suas moedas fictícias.")
    async def economy(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        coins = self.levels.get(user_id, 0)
        await interaction.response.send_message(f"Você tem **{coins}** moedas!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Advanced(bot))
