import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ البوت شغّال: {bot.user}")

@bot.command()
async def فحص(ctx, uid: str):
    await ctx.send(f"جارٍ فحص UID: {uid} ...")
    
    if uid.startswith("1"):
        await ctx.send("الحساب سليم.")
    elif uid.startswith("9"):
        await ctx.send("الحساب ربما يكون محظور.")
    else:
        await ctx.send("UID غير معروف أو غير صحيح.")

bot.run("MTM3NDM5NDczNDEwOTI2NjAwMQ.Gl7Df2.YfaxWDyW0pMvtdWq5WxGeXu7p8flC0QKjMrfn0")
