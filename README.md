# discord-uptimerobot

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


Bot para checar disponibilidade de serviços via API do uptime robot

## Instalação

```bash
pip install python-dotenv
```

## Uso

```python
import discord
from discord.ext import tasks
from discord.ext import commands
from uptimerobotpy import UptimeRobot
from dotenv import load_dotenv
import os
import time

# criar .env
UPTIME_ROBOT_API_KEY = 
DISCORD_API_KEY = 

# api key do uptime robot
self.up_robot = UptimeRobot(api_key=os.getenv("UPTIME_ROBOT_API_KEY"))

api key do discord
client.run(os.getenv("DISCORD_API_KEY"))

```

## Contribuição
Pull requests são bem-vindas. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de mudar.

