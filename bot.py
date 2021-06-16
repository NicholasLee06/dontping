import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "<@!userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)
        # @! is for pc discord, @ is for device
        
    if "<@userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message Deleted", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)
        
    if "<@!userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)
       
    if "<@userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)

    if "<@userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)
        
    if "<@!userid>" in message.content:
        await message.delete();
        embedVar = discord.Embed(title="Small Reminder", description="Hi there! Pinging one of our staff member will not help you to get faster service. It could be more slower if you ping. Thanks for your understanding.", color=15158332)
        embedVar.add_field(name="Sent By", value=f"{message.author.name}", inline=False)
        embedVar.add_field(name="Message", value=f"{message.content}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/icons/848959495630487583/8b78e8494dbe8d643fa421f8863e379c.jpg")
        embedVar.set_footer(text="Powered by NicholasLee#3724", icon_url="https://cdn.discordapp.com/avatars/617713953367130123/ad543153617ad1c4f584691230e64d44.png?size=256")
        await message.channel.send(embed=embedVar)

client.run('token')
