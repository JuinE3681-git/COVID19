import discord
from bs4 import BeautifulSoup
import requests
import os

token = "token"

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == "=코로나":
        response = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=코로나')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        data1 = soup.find('div', class_='graph_view')
        data2 = data1.findAll('div', class_='box')
        data3 = data1.findAll('div', class_='box bottom')
        checked = data2[0].find('p', class_='txt').find('strong', class_='num').text
        checking = data2[2].find('p', class_='txt').find('strong', class_='num').text
        free = data3[0].find('p', class_='txt').find('strong', class_='num').text        
        die = data3[1].find('p', class_='txt').find('strong', class_='num').text
        wasup = soup.find('div', class_='csp_notice_info').find('p').find_all(text=True, recursive=True)
        #===============================
        coembed = discord.Embed(color=0xff0000, title='코로나19', description =f'{wasup[1]}' )
        coembed.add_field(name=":microbe:확진자", value=f'{checked}명', inline=True)
        coembed.add_field(name=":tada: 격리해제", value=f'{free}명', inline=True)
        coembed.add_field(name=":test_tube:검사중", value=f'{checking}명', inline=True)
        coembed.add_field(name=":no_mouth:사망자", value=f'{die}명', inline=True)
        coembed.set_footer(text="봇 코드 출처 : https://gist.github.com/SaidBySolo")
        await message.channel.send(embed = coembed)
@client.event
async def on_message(message):
    if message.content == "=도움":
        await message.channel.send('=도움과 =코로나 명령어가 있습니다')

access.token = os.environ["BOT_TOKEN"]
client.run(access_token)
