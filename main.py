import os
import asyncio
import logging
import discord
from discord.ext import commands


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bot_music")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info("Conectado como %s (id=%s)", bot.user, bot.user.id)
    try:
        synced = await bot.tree.sync()
        logger.info("Slash commands sincronizados: %d", len(synced))
    except Exception as e:
        logger.exception("Erro ao sincronizar app_commands: %s", e)

async def load_extensions():
    for ext in ("cogs.basic", "cogs.moderation", "cogs.entertainment", "cogs.integration", "cogs.advanced"):
        try:
            await bot.load_extension(ext)
            logger.info("Extensão carregada: %s", ext)
        except Exception as e:
            logger.exception("Falha ao carregar %s: %s", ext, e)

async def main():
   
    await load_extensions()
    token = ("MTQwNzEzNjA3Nzg5Mzg2NTUyMA.GEFr40.eLTu2l-idYpTXj4H6AiVo0fZPrCh4fF87JM40M")
    if not token:
        raise RuntimeError("Variável de ambiente DISCORD_TOKEN não definida. Configure seu token com DISCORD_TOKEN.")
    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot finalizado pelo usuário.")
