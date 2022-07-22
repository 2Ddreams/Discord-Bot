import discord
import random
import time
from discord.ext import commands




TOKEN = "OTc5NzMxMjU5OTA1NDQxODMy.Gbnp6p.Q4xk3W5Y5IU0rq6MDz83wK2JdheAm8kldfVEyQ"

client = discord.Client()

heros = ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitilyn', 'camili', 'cassiopeia', "cho'gath", 'corki', 'darius', 'diana', 'mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvan iv', 'jax', 'jayce', 'jinx', "kai'sa", 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', "kha'zix", 'kindred', 'kled', "kog'maw", 'leblanc', 'lee sin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzaharm', 'maokai', 'master yi', 'miss fortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu and willump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', "rek'sai", 'rell', 'renata glasc', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', "vel'koz", 'vex', 'vi', 'viego', 'viktor', 'viadimir', 'volibear', 'warwick', 'wokong', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'zeri', 'ziggs', 'zilean', 'zoe', 'zyra']

def TextSpacer(lines):
    for i in range(lines):
        print("----------------------------------------------------------------")


text_spacer = "----------------------------------------------------------"

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"({username}) [{channel}]: {user_message} ")
    TextSpacer(1)



    if message.author == client.user:
        return


    if message.channel.name == "bot-test-ground":
        if user_message.lower() == "hello" or "hi":
            await message.channel.send(f"Hello {username}!")
        elif user_message.lower() == "bye":
            await message.channel.send(f"See you later {username}!")
        elif user_message.lower() == "what" and "do":
            await message.channel.send(f"Not much but you can see by using '?help'.")



# Anywhere
    if "!" in user_message.lower():
        command = user_message.lower().split(" ")[1]
        if command == "random":
            max_num = user_message.lower().split(" ")[2]
            #await message.channel.send(f"Debug: {index}")
            if max_num != "hero":
                num = user_message.lower().split(" ")[2]
                response = f"Random Number: [ {random.randrange(1, int(num)+1)} ]" 
                await message.channel.send(response)
            elif max_num == "hero":
                response = f"{random.choice(heros)}"
                await message.channel.send(f"Random Hero: [ {response} ]")
        elif command == "top":
            lane = user_message.lower().split(" ")[2]
            if lane == "top":
                await message.channel.send("https://u.gg/lol/top-lane-tier-list")
            elif lane == "mid":
                await message.channel.send("https://u.gg/lol/mid-lane-tier-list")
            elif lane == "jun":
                await message.channel.send("https://u.gg/lol/jungle-tier-list")
            elif lane == "bot":
                await message.channel.send("https://u.gg/lol/adc-tier-list")
            elif lane == "sup":
                await message.channel.send("https://u.gg/lol/support-tier-list")
            elif lane == "all":
                await message.channel.send("https://u.gg/lol/tier-list")
        elif command == "clear":
            await message.channel.send("Clearing... last 1000 messages")
            time.sleep(1)
            await message.channel.purge()
        elif command == "d-c":
            await message.channel.send("Deleting current channel...")
            time.sleep(2)
            await message.channel.delete()
        else:
            await message.channel.send("Invalid command check '?help' for help.")








    # Help 
    if user_message.lower() == "?help":
        await message.channel.send(f"LIST OF COMMANDS (Use '!' to execute a command)")
        await message.channel.send(f"{text_spacer}\n{text_spacer}")
        await message.channel.send(f"-----Random Collection-----")
        await message.channel.send(f"random (max num) - Generates a random number from 1 to your chosen max number.")
        await message.channel.send(f"random hero - Gives random hero in League.")
        await message.channel.send(f"{text_spacer}")
        await message.channel.send(f"-----Information Collection-----")
        await message.channel.send(f"(hero name) - Use in [character-information] channel to learn about the hero.")
        await message.channel.send(f"top (chosen lane) - Chose your lanes from (top, mid, jun, bot, sup) to learn about the best heros in each.")
        await message.channel.send(f"{text_spacer}")
        await message.channel.send(f"-----Admin-----")
        await message.channel.send(f"clear - Clears last 1000 messages.")
        await message.channel.send(f"d-c - Deletes current channel.")
        await message.channel.send(f"{text_spacer}")
        await message.channel.send(f"-----Others-----")
        await message.channel.send(f"Chat with the bot in [bot-test-ground] channel.")
        await message.channel.send(f"{text_spacer}\n{text_spacer}")
        

     


# Character Information Channel
    if message.channel.name == "character-information":
        

        if "!" in user_message.lower():
            hero = user_message.lower().lower().split(" ")[1]
            print(hero)
            if hero.strip() in heros:
                await message.channel.send(f"https://u.gg/lol/champions/{hero}/build")
            elif user_message.lower() == "!nunu and willump":
                await message.channel.send(f"https://u.gg/lol/champions/nunu-and-willump/build")
            elif user_message.lower() == "!xin zhao":
                await message.channel.send(f"https://u.gg/lol/champions/xin-zhao/build")
            elif user_message.lower() == "!twisted fate":
                await message.channel.send(f"https://u.gg/lol/champions/twisted-fate/build")
            else:
                await message.channel.send(f"Sorry, the hero you chose is not in the game :(")



    

    if user_message.lower() == "!music":
        await message.channel.send(f"https://www.youtube.com/watch?v=dQw4w9WgXcQ")






client.run(TOKEN)