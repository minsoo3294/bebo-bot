import discord
import asyncio
import random

client = discord.Client()

token = "

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 실행되었습니다.')
    game = discord.Game('b/command')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)

@client.event
async def on_message(message):
    if message.content == "!뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        await message.channel.send(d)

@client.event
async def on_message(message):

    if message.content == "b/command":
        embed = discord.Embed(title="Beat bot", description="Commands", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/894379677693653033/6985d097cea5161a137fc8ddd5d8d423.png?size=128")
        embed.add_field(name="!뽑기", value="'꽝' 또는 '당첨' 메시지가 각각 50% 확률로 나온다.",inline=True)
        embed.add_field(name="!바보", value="비트봇 바보 아니니까 하지마세요..... ㅠㅠ",inline=True)
        embed.add_field(name="!챗청 [메시지수]", value="[메시지수] 만큼 메시지를 삭제한다.(관리자만 사용 가능)",inline=True)
        await message.channel.send(embed=embed)

    if message.content == "!바보":
        ran = random.randint(3,4)
        if ran == 3:
            e = "너무해요...."
        if ran == 4:
            e = "너보단 ||농담인거 알죠?||"
        await message.channel.send(e)

    if message.content == "!뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        await message.channel.send(d)

    if message.content.startswith ("!챗청"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="이 소스는 바코드 #1741 님이 베포하셨습니다.", icon_url="https://cdn.discordapp.com/icons/540140573059973120/3b1f04031e82006d484759ddc7944524.png?size=96")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))


access_token = os.environ['BOT_TOKEN'


client.run(token)
