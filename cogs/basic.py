import discord
from discord.ext import commands
from discord import app_commands

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Eventos
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            await member.send(f"Bem-vindo, {member.name}! Você entrou em {member.guild.name} 😄")
        except Exception:
            pass
        role = discord.utils.get(member.guild.roles, name="Membro")
        if role:
            try:
                await member.add_roles(role, reason="Entrada no servidor")
            except discord.Forbidden:
                pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        ch = discord.utils.get(member.guild.text_channels, name="geral") or member.guild.system_channel
        if ch:
            try:
                await ch.send(f"{member.name} saiu do servidor. 👋")
            except Exception:
                pass

    # Comandos
    @app_commands.command(name="ping", description="Mostra a latência do bot.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @app_commands.command(name="hello", description="Receba um oi simpático.")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Oi, {interaction.user.mention}! 🌸")

async def setup(bot: commands.Bot):
    await bot.add_cog(Basic(bot))
