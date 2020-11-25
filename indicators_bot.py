import discord

d = { '0' : 'zero',
      '1' : 'one',
      '2' : 'two',
      '3' : 'three',
      '4' : 'four',
      '5' : 'five',
      '6' : 'six',
      '7' : 'seven',
      '8' : 'eight',
      '9' : 'nine'
      }

token = input('Token: ')

client = discord.Client()

@client.event
async def on_ready():
    print('Running as user {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!emojify') or message.content.startswith('!emojifier'):

        raw = message.content

        # Remove !command from beginning of message string
        if message.content.startswith('!emojify'):
            raw = raw[9:]
        elif message.content.startswith('!emojifier'):
            raw = raw[11:]

        if raw == "":
            embed=discord.Embed(title="Emojifier v1.0", description="Created by qCam\n\nUse `!emojifier -h`")
            await message.channel.send(embed=embed)
            await message.channel.send('https://cdn.discordapp.com/attachments/744483084568887320/781070974287740948/unknown.png')

        elif raw.startswith('-r'):
            raw = raw[3:] # removes '-r ' from beginning of string
            await message.channel.send('`' + emojify(raw) + '`')

        elif raw.startswith('-h'):
            embed=discord.Embed(title="Emojifier Help", description="Use `!emojifier` or `!emojify`")
            embed.add_field(name="!emojifier", value="Shows bot information.", inline=False)
            embed.add_field(name="!emojifier 'message'", value="Converts your message into emojis.", inline=False)
            embed.add_field(name="!emojifier -r 'message'", value="Same as regular conversion but in a copy-pastable format.", inline=False)
            embed.add_field(name="!emojifier -h", value="Shows this help embed.", inline=False)
            await message.channel.send(embed=embed)

        else:
            await message.channel.send(emojify(raw))

def emojify(s):
    output = ""
    for c in s:
        if c.isnumeric():
            output += ":" + d[c] + ": "
        elif c.isalpha():
            output += ":regional_indicator_" + c.lower() + ": "
        else:
            output += c + " "
    return output

client.run(token)