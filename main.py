import discord
import requests
import json
import os

client = discord.Client()

def get_dotawinlose(dota):
    response = requests.get("https://api.opendota.com/api/players/"+ dota[6:20] +"/wl")
    json_data = json.loads(response.text)
    player = " Win: " + str(json_data['win']) + " Lose: " + str(json_data["lose"])
    return(player)

def get_dotawinlose2(dota):
    response = requests.get("https://api.opendota.com/api/players/"+ dota[9:20] +"/wl")
    json_data = json.loads(response.text)
    total = json_data['win'] + json_data["lose"]
    player = ":star:Win: " + str(json_data['win']) + " \n:star:Lose: " + str(json_data["lose"]) + "\n:star:Total Games: " + str(total)
    return(player)

def get_dotaprofile(dota):
    response = requests.get("https://api.opendota.com/api/players/"+ dota[9:20])
    json_data = json.loads(response.text)
    profile = json_data['profile']
    playername = profile['personaname']
    profileurl = profile['profileurl']
    player ="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬~ஜ۩۞۩ஜ~▬▬▬▬▬▬▬­­­­­­­­­­▬▬▬▬▬▬▬▬▬▬▬ " + "\n:star:NAME: " + playername + "\n:star:SOLO MMR: " + str(json_data['solo_competitive_rank']) + "\n:star:PARTY MMR: " + str(json_data["competitive_rank"]) + '\n:star:STEAM PROFILE:' + profileurl
     
    return(player)
           

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return           
    if message.content.startswith('$profile'):
        try:
            player = get_dotaprofile(message.content)
            playerwinlose = get_dotawinlose2(message.content)
            await message.channel.send(player + '\n' + playerwinlose + '\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nkung hindi tama yung nabigay baka naka private yung account mo\nOne Knight Stand Bot - Make sure your account is public.')
            print('User use Command:'+ message.content)
        except:
            await message.channel.send(':tired_face:Steam Account not available!\n make sure yung account is open for public.')
            print('User use Command:'+ message.content)
client.run(os.getenv('TOKEN'))

