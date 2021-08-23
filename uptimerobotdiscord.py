import discord
from discord.ext import tasks
from discord.ext import commands
from uptimerobotpy import UptimeRobot
from dotenv import load_dotenv
import os
import time

load_dotenv()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lastContent = 'Teste'
        self.up_robot = UptimeRobot(api_key=os.getenv("UPTIME_ROBOT_API_KEY"))
        self.monitors = self.up_robot.get_monitors()
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    
    async def on_message(self, message):
        if message.content.startswith('!status'):
            if (self.monitors['monitors'][0]['status'] == 2):
                await message.channel.send('O sistema encontra-se em estável e em funcionamento')
            if (self.monitors['monitors'][0]['status'] == 9):
                await message.channel.send('O sistema encontra-se em manutenção ou com instabalibilidades')
            
            
    @tasks.loop(seconds=10) 
    async def my_background_task(self):
        channel = self.get_channel(329397993424027650) 
        if(self.lastContent != self.monitors['monitors'][0]['status']):
            self.lastContent = self.monitors['monitors'][0]['status']
            if (self.monitors['monitors'][0]['status'] == 9):
                await channel.send('O sistema encontra-se em manutenção ou com instabalibilidades')
            else:
                await channel.send('O sistema encontra-se em funcionamento')
        else:
            print('Nada a mostar')
            print(self.lastContent)
            
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() 
    

client = MyClient()
client.run(os.getenv("DISCORD_API_KEY"))