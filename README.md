# DiscordBot

This is my first attempt at making a Discord bot, so I wanted it to be pretty basic and easy to understand. I was new to coding bots even though I did have a basic idea of Python and as an aspiring data scientist this was suggested as a good beginer's project so I decided to do it :)

So first of all, thanks to FreeCodeCamp, the youtube gods of programming and computer science, I followed their easy to understand tutorial and improvised (slightlyyy) to get my bot up and running. You can watch the same [here](https://www.youtube.com/watch?v=SPTfmiYiuok). 

I also used Replit cloud platform for my bot (as suggested in the video), so here's the link to my [code](https://replit.com/@teamleoeaton/Motivate-bot#main.py)




 Motivate Bot replies with some encouraging words when it detects sad/depressing words in the chat. It also does a few other things just to spice things up a bit...
 
 
 
 
 
 
 ## **Here's a list of commands and what they can do:**
 
 1. **$inspire**: Provide an inspirational quote
    * As suggested in the tutorial, I used [ZenQuotes](https://zenquotes.io/) API to get the quotes and display them in random. You can use any API you want to, just make sure you read through their documentation to figure out how to use it.

 2. **$responding [true/false]**: This decides whether the bot replies with encouraging messages or not, i.e., you can even text with your friends without the intervention of the bot, if this is turned off.
    * I created a list of sad_words that the bot looks for and a starter list of encouraging replies for it to use, users can add more replies to this list as it is stored in a database.
    * If the bot detects a word from the sad words list, it will automatically reply with a random encourgement from the list created. 
    * Users can add or delete an encouragement, the commands are mentioned below.
 
 3. **$add [text]**: Users can add their custom words of encouragement using this command.
 
 4. **$del [index]**: Users can delete a specific encouragement present at the index they provide.
 
 5. **$list**: Provides with the list of encouragements available for the bot to use currently.
 
 6. **$playlists**: Provides links to my spotify playlists
    * I use a Rythm bot in my server and it annoys me to physically copy my spotify playlists links for rythm to play, so I decided to get help from Motivate Bot!
    * The bot provides me with the links to my favourite spotify playlists so I can just copy paste it easily without having to open spotify separately.
 
 7. **$help**: Provides link to this Read.me document so users can browse the list of commands







Since Replit is an online platform, our bots will go offline once we close the tabs, to avoid this we use Uptime Robot to keep our bot alive even when we have our Replit tabs closed. You just have to include the keep_alive.py file and import it in your main file, it incorporates Flask and does the job! 
The Uptime Robot automatically pings your bot to let it know it is in use and thus stops it from going offline.


These are the bots current functions, I hope to incorporate more in the future.

### Here are some useful links:

* [Discord home page](https://discord.com/) (Incase you don't have an account yet)
* [Replit Platform](https://repl.it) : It was pretty easy to use and FREE! Just sign up and you are ready to code!
* [Discord Developer page](https://discord.com/developers/applications): You can find the creation part of your bot here, follow the tutorial video for clarity
* [Uptime Robot](https://uptimerobot.com/login?rt=https://uptimerobot.com/): This is absolutely free and just needs signing up too

The code is currently under further devlopment since I'm hoping to improve it, but I hope you found this useful :)
   
 



