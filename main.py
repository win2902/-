import discord
from discord.ext import commands
import asyncio
import scrip as sc
import scrip_main as sc_m

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

TOKEN = 'TOKEN'

@bot.listen()
async def on_message(message):
    ctx = await bot.get_context(message)
    script_name = sc_m.script_name
    script_list = message.content.split()
    for x in script_list:
        if x in script_name:
            if message.content.startswith(x):
                answer = message.content.split()
                print(answer)
                cast = Document(answer)
                await cast.script_live(ctx)

class Document:
    def __init__(self, answer):
        self.bot = answer
    async def script_live(self, ctx):
        BUTTONS = ["◀️", "⏹", "▶️"]
        per_script = sc.S2남
        urls = per_script
        urls_index = len(urls)
        print(urls_index)
        index = 0

        msg_solo = urls[index]
        if urls_index == 1:
            await ctx.channel.send(msg_solo)

        else:
            msg = await ctx.send(urls[index])
            for b in BUTTONS:
                await msg.add_reaction(b)

            while True:
                try:
                    react, user = await bot.wait_for("reaction_add", check=lambda r,
                    u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
                    await msg.remove_reaction(react.emoji, user)

                except asyncio.TimeoutError:
                    return await msg.delete()

                else:
                    if react.emoji == BUTTONS[0] and index > 0:
                        index -= 1
                    elif react.emoji == BUTTONS[1]:
                        return await msg.delete()
                    elif react.emoji == BUTTONS[2] and index < len(urls) - 1:
                        index += 1
                    await msg.edit(content=urls[index])

bot.run(TOKEN)
