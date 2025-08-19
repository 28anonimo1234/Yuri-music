import discord
from discord.ext import commands
from discord import app_commands

def has_mod():
    def predicate(interaction: discord.Interaction) -> bool:
        return bool(interaction.user.guild_permissions.manage_messages)
    return app_commands.check(predicate)

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Apaga uma quantidade de mensagens deste canal.")
    @has_mod()
    async def clear(self, interaction: discord.Interaction, amount: int):
        if amount < 1 or amount > 500:
            return await interaction.response.send_message("Use um valor entre 1 e 500.", ephemeral=True)
        await interaction.response.defer(ephemeral=True, thinking=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"Apaguei {len(deleted)} mensagens.")

    @app_commands.command(name="kick", description="Expulsa um membro do servidor.")
    @has_mod()
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str | None = None):
        try:
            await member.kick(reason=reason or f"Por {interaction.user}")
            await interaction.response.send_message(f"{member.mention} foi expulso. 🛑")
        except discord.Forbidden:
            await interaction.response.send_message("Não tenho permissão para expulsar este usuário.", ephemeral=True)

    @app_commands.command(name="ban", description="Bane um membro do servidor.")
    @has_mod()
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str | None = None):
        try:
            await member.ban(reason=reason or f"Por {interaction.user}")
            await interaction.response.send_message(f"{member.mention} foi banido. 🚫")
        except discord.Forbidden:
            await interaction.response.send_message("Não tenho permissão para banir este usuário.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
