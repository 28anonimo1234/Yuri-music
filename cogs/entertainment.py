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
    @app_commands.command(name="flip", description="Jogue uma moeda.")
    async def flip(self, interaction: discord.Interaction):
        result = random.choice(["Cara", "Coroa"])
        await interaction.response.send_message(f"🪙 Resultado: **{result}**")

    @app_commands.command(name="8ball", description="Pergunte algo para a bola mágica 8.")
    async def eight_ball(self, interaction: discord.Interaction, question: str):
        responses = [
            "Sim.", "Não.", "Talvez.", "Definitivamente sim.", "Definitivamente não.",
            "Pergunte novamente mais tarde.", "Não posso prever agora.", "Concentre-se e pergunte novamente."
        ]
        await interaction.response.send_message(f"🎱 {random.choice(responses)}")

    @app_commands.command(name="rps", description="Jogue pedra, papel ou tesoura contra o bot.")
    async def rps(self, interaction: discord.Interaction, escolha: str):
        escolhas = ["pedra", "papel", "tesoura"]
        escolha = escolha.lower()
        if escolha not in escolhas:
            return await interaction.response.send_message("Escolha pedra, papel ou tesoura.", ephemeral=True)
        bot_escolha = random.choice(escolhas)
        if escolha == bot_escolha:
            resultado = "Empate!"
        elif (escolha == "pedra" and bot_escolha == "tesoura") or \
             (escolha == "papel" and bot_escolha == "pedra") or \
             (escolha == "tesoura" and bot_escolha == "papel"):
            resultado = "Você venceu!"
        else:
            resultado = "Você perdeu!"
        await interaction.response.send_message(f"Você escolheu **{escolha}**. O bot escolheu **{bot_escolha}**. {resultado}")
