import discord
from discord.ext import commands

Token = 'add your token in to here'  #### toknaka lera dane

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='g!', intents=discord.Intents.all())


@bot.event
async def on_ready():
  activity = discord.Activity(name='g!command | AboOo',
                              type=discord.ActivityType.playing)
  await bot.change_presence(activity=activity)
  print(f'Logged in as {bot.user.name}')


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)

  embed = discord.Embed(title='Member Banned',
                        description=f'{member.mention} has been banned.',
                        color=discord.Color.green())
  embed.add_field(name='Reason', value=reason)

  await ctx.send(embed=embed)


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)

  embed = discord.Embed(title='Member Kicked',
                        description=f'{member.mention} has been kicked.',
                        color=discord.Color.green())
  embed.add_field(name='Reason', value=reason)

  await ctx.send(embed=embed)


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def clear(ctx, amount=5):
  await ctx.message.delete()  # Delete the command message

  deleted = await ctx.channel.purge(limit=amount)

  embed = discord.Embed(
    title='Chat Cleared',
    description=f'{len(deleted)} messages have been cleared.',
    color=discord.Color.green())

  await ctx.send(embed=embed, delete_after=5)


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def lock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  await channel.set_permissions(ctx.guild.default_role, send_messages=False)

  embed = discord.Embed(title='Channel Locked',
                        description=f'{channel.mention} has been locked.',
                        color=discord.Color.green())

  await ctx.send(embed=embed)


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  await channel.set_permissions(ctx.guild.default_role, send_messages=True)

  embed = discord.Embed(title='Channel Unlocked',
                        description=f'{channel.mention} has been unlocked.',
                        color=discord.Color.green())

  await ctx.send(embed=embed)


@bot.command()
async def command(ctx):
  embed = discord.Embed(title='GuardianBot commands',
                        description='List of available commands:',
                        color=discord.Color.green())
  embed.add_field(name='`g!ban`', value='Ban a member from the server.')
  embed.add_field(name='`g!kick`', value='Kick a member from the server.')
  embed.add_field(name='`g!clear`',
                  value='Clear a specified number of messages.')
  embed.add_field(
    name='`g!lock`',
    value='Lock a channel to prevent members from sending messages.')
  embed.add_field(name='`g!unlock`',
                  value='Unlock a previously locked channel.')
  embed.set_image(
    url=
    'https://cdn.discordapp.com/attachments/907672228383035454/1109832038883794964/help_command.png'
  )

  await ctx.send(embed=embed)


@bot.command()
async def rules(ctx):
  embed = discord.Embed(title='بەخێر بێن بۆ سێرڤەری Lucky Ibo',
                        description='یاساکانی سێرڤەر',
                        color=discord.Color.green())
  embed.add_field(name='`رێزگرتن`', value='رێزگرتن لە سەروو هەموو شتێکەوەیە')
  embed.add_field(name='`قسەی نەشیاو`',
                  value='قسەی نەشیاو و دانانی وێنە و ڤیدیۆی نەشیاو قەدەغەیە.')
  embed.add_field(name='`بەکارهێنانی بۆت`',
                  value='بەکارهێنانی بۆت لە ڤۆیس و چاتە گشتییەکان قەدەغەیە')
  embed.add_field(
    name='`باسکردنی سیاسەت`',
    value='باسکردنی سیاسەت و شارچییەتی بە هەموو شێوەیەك قەدەغەیە')
  embed.add_field(name='` رۆڵ بە دەست`',
                  value='تەداخول کردنی کاری رۆڵ بە دەست و کەسانی تر قەدەغەیە')
  embed.add_field(name='`دانانی لینك `',
                  value='دانانی رێکلام و لینك لە چاتی گشتی قەدەغەیە')
  embed.set_image(url='https://i.gifer.com/VofE.gif')
  await ctx.send(embed=embed)


bot.run(Token)
