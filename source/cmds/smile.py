import discord # 導入discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import datetime
import json

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #互動設定檔
    jdata_bot = json.load(jfile_bot)
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #機器人設定檔
    jdata_bot = json.load(jfile_bot)

"""開機訊息"""
bot_m = '[Bot]'

"""顏色"""
blue_text = "in\033[34m"
white_text = "\033[0m"

class smile(Cog_Extension):
    """其他功能"""

    @commands.Cog.listener() #加入伺服器
    async def on_guild_join(self,guild):
        """時間設定"""
        time_stamp = datetime.datetime.now()
        time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')

        embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=0xffd300)
        embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed.add_field(name="目前版本", value=jdata_bot['Version'], inline=True)
        embed.add_field(name="機器人作者", value="minexo79", inline=False)
        embed.add_field(name="指令幫助", value=jdata_bot['help'], inline=True)
        embed.set_footer(text="SmileGuy Discord Bot")
        channel = self.bot.get_channel(guild._system_channel_id) # 抓取預設聊天室ID
        print(bot_m,"joined at",guild.name,blue_text,time_m,white_text) #抓取伺服器名稱並且印在CLR上面
        await channel.send(embed=embed) #聊天室顯示加入訊息

    @commands.command() #ping查詢
    async def ping(self,ctx):
        embed = discord.Embed(color=0xffd300)
        embed.add_field(name="我目前的延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.set_footer(text="SmileGuy Discord Bot")
        await ctx.send(embed=embed)
    
    @commands.command() #關於
    async def about(self,ctx):
        embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=0xffd300)
        embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed.add_field(name="目前版本", value=jdata_bot['Version'], inline=True)
        embed.add_field(name="機器人作者", value="minexo79", inline=False)
        embed.add_field(name="指令幫助", value=jdata_bot['help'], inline=True)
        embed.set_footer(text="SmileGuy Discord Bot")
        await ctx.send(embed=embed) #聊天室顯示訊息
    
    @commands.command(pass_context = True) #HELP
    async def help(self,ctx):
        embed=discord.Embed(color=0xffd300)
        embed.set_author(name="😀😀我可用的功能：😆😆")
        embed.add_field(name="!photo", value="發送梗圖", inline=False)
        embed.add_field(name="!addphoto <網址>", value="增加梗圖", inline=True)
        embed.add_field(name="!delphoto <網址>", value="刪除梗圖", inline=True)
        embed.add_field(name="!photolist <網址>", value="查詢現有梗圖", inline=True)
        embed.add_field(name="!wea <英文地名>", value="天氣查詢", inline=False)        
        embed.add_field(name="!help", value="可用指令查詢", inline=False)
        embed.add_field(name="!about", value="關於此機器人", inline=True)
        embed.add_field(name="!ping", value="查詢延遲", inline=True)
        embed.add_field(name="其他功能", value="訊息回復(ex: 蛤)", inline=True)
        embed.set_footer(text="SmileGuy Discord Bot")
        await ctx.send(embed=embed) #聊天室顯示訊息      

def setup(bot):
    bot.add_cog(smile(bot))  