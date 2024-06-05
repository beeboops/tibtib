from re import sub
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=':', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("hallo")

color_roles = (
    1045804983813144618,
    1045805119041712158,
    1045805228441747487,
    1045805334008184864,
    1045808503203307580,
    1045808635911098418,
    1045808901242748978,
    1045808998391218218,
    1045809973575303199,
    1045810117158899802,
    1045810117158899802,
    1045810250093187083,
    1045810342229442611,
    1045811473307422750,
    1045811586054488134,
    1045811685446922251,
    1045811758524285039,
    1045812290835972156,
    1045812411912945724,
    1045812569039970345,
    1045813456894431282,
    1045813563379429438,
    1045813657340215406,
    1045814437455605833,
    1045814569827835996,
    1045814663297896548,
    1045814716498456596,
    1045816662512906301,
    1045816773909434428,
    1045816837411176558,
    1045816897465229354,
    1045812510835613787,
    1045813722188361849
)

booster_role = (1036915288983224341)

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        # Check if booster role was removed
        if 1036915288983224341 in [role.id for role in before.roles] and 1036915288983224341 not in [role.id for role in after.roles]:
            # Iterate through color roles to find the one to remove
            for role_id in color_roles:
                if 1036915288983224341 in [role.id for role in before.roles]:
                    role = discord.utils.get(after.guild.roles, id=role_id)  # Find the role object
                    if role:
                        await after.remove_roles(role)  # Remove the role from the member

sub_role = (1137072315214073867)

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        # Check if booster role was removed
        if 1137072315214073867 in [role.id for role in before.roles] and 1137072315214073867 not in [role.id for role in after.roles]:
            # Iterate through color roles to find the one to remove
            for role_id in color_roles:
                if 1137072315214073867 in [role.id for role in before.roles]:
                    role = discord.utils.get(after.guild.roles, id=role_id)  # Find the role object
                    if role:
                        await after.remove_roles(role)  # Remove the role from the member

test_role = (1247723825940922399)

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        # Check if booster role was removed
        if test_role in [role.id for role in before.roles] and test_role not in [role.id for role in after.roles]:
            # Iterate through color roles to find the one to remove
            for role_id in color_roles:
                if test_role in [role.id for role in before.roles]:
                    role = discord.utils.get(after.guild.roles, id=role_id)  # Find the role object
                    if role:
                        await after.remove_roles(role)  # Remove the role from the member


keep_alive()
bot.run(os.getenv('token'))
