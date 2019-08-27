import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import time

with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)

class message(Cog_Extension):

    """訊息回復"""

    @commands.Cog.listener()
    async def on_message(self,msg):

        if msg.content == "蛤" and msg.author != self.bot.user: # 蛤
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            embed.set_footer(text="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            await msg.channel.send(f"蛤?")            
            await msg.channel.send(embed=embed)

        elif msg.content == "三小" and msg.author != self.bot.user: # 三小
            await msg.channel.send(f"小三啦!👿")

        elif msg.content == "幹" and msg.author != self.bot.user: # 幹
            await msg.channel.send(f"別罵髒話啦~")

        elif msg.content == "幹你娘" and msg.author != self.bot.user: # 幹你娘
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://i.imgur.com/ngAdXUq.gif")
            embed.set_footer(text="https://i.imgur.com/ngAdXUq.gif")                
            await msg.channel.send(embed=embed)

        elif msg.content == "嘿嘿嘿" and msg.author != self.bot.user: # 嘿嘿嘿
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://thumbs.gfycat.com/InexperiencedBruisedCaecilian-size_restricted.gif")
            embed.set_footer(text="https://thumbs.gfycat.com/InexperiencedBruisedCaecilian-size_restricted.gif")
            await msg.channel.send(f"母湯喔~")                            
            await msg.channel.send(embed=embed)

        elif msg.content == "早安" and msg.author != self.bot.user: # 早安
            ramdom_mes = random.choice(jdata_in[f'chat_mes_morning'])
            await msg.channel.send(f"{msg.author.mention}{ramdom_mes}")
               
        elif msg.content == "喔" and msg.author != self.bot.user: # 喔
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://meme.turn.tw/meme/451a9d0eefc8b546ec2f654b8b01022d.png")
            embed.set_footer(text="https://meme.turn.tw/meme/451a9d0eefc8b546ec2f654b8b01022d.png")
            await msg.channel.send(embed=embed)
        
        elif msg.content == "小孩子才做選擇" and msg.author != self.bot.user: # 小孩子才做選擇
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://meme.turn.tw/meme/2ab0b0594707277883792834100ba6cf.png")
            embed.set_footer(text="https://meme.turn.tw/meme/2ab0b0594707277883792834100ba6cf.png")            
            await msg.channel.send(f"我全都要.JPG")
            await msg.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(message(bot))  