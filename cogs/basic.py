import discord
from discord.ext import commands
from discord import app_commands
import discord.ui

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

    @app_commands.command(name="menu", description="Mostra o menu do bot")
    async def menu(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Menu do Bot",
            description="Aqui estão os comandos disponíveis. Clique nos botões abaixo para ver por categoria:\n\n🎵 Música\n🛠️ Básicos\n🎉 Entretenimento\n⚡ Avançado",
            color=0x00ff00
        )
        embed.set_image(url="https://i.imgur.com/fNvTiAg.jpeg")  # Imagem de banner para o menu
        view = MenuView()
        await interaction.response.send_message(embed=embed, view=view)

class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Música", style=discord.ButtonStyle.primary)
    async def music_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Menu do Bot - Música",
            description="🎵 **Comandos de Música:**\n/play - Toca uma música\n/pause - Pausa a música\n/resume - Continua a música\n/stop - Para e limpa a fila\n/skip - Pula a música\n/queue - Mostra a fila\n/disconnect - Desconecta do canal",
            color=0x00ff00
        )
        embed.set_image(url="https://i.imgur.com/fNvTiAg.jpeg")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Básicos", style=discord.ButtonStyle.secondary)
    async def basic_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Menu do Bot - Básicos",
            description="🛠️ **Comandos Básicos:**\n/ping - Latência do bot\n/hello - Oi simpático\n/menu - Este menu",
            color=0x00ff00
        )
        embed.set_image(url="https://i.imgur.com/fNvTiAg.jpeg")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Entretenimento", style=discord.ButtonStyle.success)
    async def entertainment_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Menu do Bot - Entretenimento",
            description="🎉 **Comandos de Entretenimento:**\n/quote - Citação aleatória\n/dice - Rola um dado\n/flip - Joga moeda\n/8ball - Bola 8 mágica\n/rps - Pedra, papel, tesoura",
            color=0x00ff00
        )
        embed.set_image(url="https://i.imgur.com/fNvTiAg.jpeg")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Avançado", style=discord.ButtonStyle.danger)
    async def advanced_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Menu do Bot - Avançado",
            description="⚡ **Comandos Avançados:**\n/level - Mostra seu nível\n/economy - Mostra suas moedas",
            color=0x00ff00
        )
        embed.set_image(url="https://i.imgur.com/4M7IWXT.png")
        await interaction.response.edit_message(embed=embed, view=self)

async def setup(bot: commands.Bot):
    await bot.add_cog(Basic(bot))

# depois criar o banner
