import discord 
from openai import OpenAI
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$jarvis'):
            # Extract the message after '$jarvis '
            user_question = message.content[7:].strip()  
            
            if not user_question:
                await message.channel.send("Please ask me something after $jarvis!")
                return
            
            try:
                openai_client = OpenAI(api_key="OPEN_API_KEY")
                response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": user_question}]
                )
                
                ai_response = response.choices[0].message.content
                await message.channel.send(ai_response)
                
            except Exception as e:
                print(f"Error: {e}")
                await message.channel.send("Sorry, I encountered an error while processing your request.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('DISCORD_BOT_TOKEN')

