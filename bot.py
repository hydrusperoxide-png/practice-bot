import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# track messages per channel
message_count = {}

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 🟢 RESPOND WHEN PINGED
    if client.user in message.mentions:
        responses = [
            "names Silverine i work Hydrus Multi Arms Industries  ",
            "don't blame me for the munitions exploding got it.",
            "Yes? got any complaints? i heard none from the crews of the Ryher class.",
            "don't call me if its not that important or else.",
            "dont ask me how the current council works"
        ]
        await message.channel.send(random.choice(responses))
        return  # stops double-triggering

    # 🟡 PASSIVE MESSAGE SYSTEM (per channel)
    channel_id = message.channel.id

    if channel_id not in message_count:
        message_count[channel_id] = 0

    message_count[channel_id] += 1

    if message_count[channel_id] % 5 == 0:
        responses = [
            "i am in your room did you forgot to lock the door?",
            "did you know there are total of 20 destroyed hydrusian warships on the orion straight?",
            "should i remind you that the levsa 1890 lever action sucks against no lander combat.",
            "the Hydrusian Combined Arms council has more casualties than No Lander militia fighters.",
            "i sent more people in the hospital than the battlefield."
        ]

        await message.channel.send(random.choice(responses))

client.run(os.getenv("DISCORD_TOKEN"))
