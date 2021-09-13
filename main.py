import os
import discord
import requests
import json 
import random 
from replit import db
from keep_alive import keep_alive


# Create instance of a client
client= discord.Client()



# List of sad words
sad_words = ["so done","give up","bored","sad","depressed","tired","fail","depressing","sleepless"]

# List of starter responses for encouragements
starter_encouragements= ["Don't give up homie!",
"Hold on!",
"Now let's lighten up a little...",
"Here's some Life Juice, now down it!",
"Woah! Stop right there! Now smile :)"]

# List of commands for the bot
Commands = {"$responding (TRUE/FALSE)":"Decides whether the bot responds to you or not",
"$add (text)":"Adds your custom encouragement",
"$del (number)": "Deletes encouragement at sepcified index",
"$inspire":"Shows an inspirational quote",
"$playlists":"Provides links to my spotify playlists"
}


    

# Check if we are responding to messages
if "responding" not in db.keys():
  db["responding"] = True

# To get a random quote on command
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

# To update starter_encouragements in database
def update_encouragements(encouraging_message):
  # Adding to list of encouragements if it already exists in database
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements

  # If not, creating a list of encouragements in database
  else:
    db["encouragements"] = [encouraging_message]

# To delete an encouraging message
def delete_encourgement(index):
   encouragements = db["encouragements"]

   
   if len(encouragements)>index:
    
     del encouragements[index]
     db["encouragements"] = encouragements 


# To register an event
@client.event

# Event when Bot ready to work
async def on_ready():
  print("Lezz do this! {0.user}".format(client))

# Bot senses a message 
@client.event
async def on_message(message):
  # Ignore if message from bot itself
  if message.author == client.user:
    return
  
  msg = message.content

  # Check if message starts with our command 
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  # Check before responding  
  if db["responding"]:
    # Making user added encouragements available as response
    options = starter_encouragements
    if "encouragements" in db.keys():
      options.extend(db["encouragements"])

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  
  # To add custom encouragements
  if msg.startswith("$add"):
    # To get message after $add 
    encouraging_message = msg.split("$add ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouragement added!")

  # To delete encouragements
  if msg.startswith("$del"):
    # Create empty list incase no encouragements exist in database
    encouragements=[]

    # Check if encouragements already exists in database
    if "encouragements" in db.keys():
      # Get index from message
      index = int(msg.split("$del",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  #To see hte list of encouragements
  if msg.startswith("$list"):
    encouragements=[]
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  # To decide if bot should respond or not
  if msg.startswith("$responding"):
    value= msg.split("$responding ",1)[1]

    if value.lower()=="true":
      db["responding"]= True
      await message.channel.send("Responding is on")
    else:
      db["responding"]= False
      await message.channel.send("Responding is off")
  
  # To display list of Commands and functions
  if msg.startswith("$help"):
    
   # Displaying the list of commands
    for key,value in Commands.items():
      await message.channel.send(key)
      await message.channel.send(value)
  
  # Playing music
  if msg.startswith("$playlists"):

      
    Playlists = {"MC Vibes":"https://open.spotify.com/playlist/2YCFeWGLRl15M5AecOn9ux?si=2bf56a79b5fe4166",
    "What love feels like":"https://open.spotify.com/playlist/1X23gcbDb9B5WDUUEEt4DS?si=f1a78095331d4ae3",
    "Gloom Clouds":"https://open.spotify.com/playlist/5KMh5qxgPEF9bh3k1HdLXX?si=9c64ca9dd8a14622",
    "Desire":"https://open.spotify.com/playlist/2iTA0GOh2NaABmgsomcPEg?si=67d12ae6fe3548ee"}
    
    for names in Playlists.items():
      await message.channel.send(names)
    
#Run webserver
keep_alive()  
# To run the bot, use secret from sidebar coz replit is public
client.run(os.environ['TOKEN'])

