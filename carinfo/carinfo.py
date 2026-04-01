import discord
from redbot.core import commands
from redbot.core.utils.views import SetApiModal
from discord import ui
import asyncio

from . import database_obj
from .database_obj import DatabaseSetup
from .database_obj import dbbuttons
from .carmodels_obj import UserCarInfo, CarBrands




# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot
        self.active_builds = { }

    # Command for users to input their car information. SEE: carmodels_obj.py
    @commands.command()
    async def carinfo(self, ctx):
        """Command for users to input their car information"""
        grab_user = UserCarInfo(ctx.author.id)
        view = CarBrands(car_obj=grab_user)
        await ctx.send(view=view) # Send message with buttons to select car brand and model

    # Command for users to display their car information. SEE:
    @commands.command()
    async def carlist(self, ctx):
        """Command for users to display their list of available cars"""
        cars = await database_obj.pull_car_info(None, ctx.author.id)

        if not cars:
            return await ctx.send("Your garage is empty. You should add some cars!")
        
        embed = discord.Embed(
            title=f"{ctx.author.display_name}'s Garage",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=ctx.auther.display_avatar.url)

        for car in cars:
            vendor, model, engine, tuned, revision = car
            status = "Tuned" if tuned else "Not Tuned"

            embed.add_field(
                name = f"{vendor} {model}",
                value = {status},
                inline = True
                )
        await ctx.send(embed=embed)
        #msg = "\n".join(car_info_arrangement)
        # await ctx.send(f"**Garage:**\n{msg}")
        


        

    
    # Command for setting up the database connection, Summons button to allow for Modal based input. SEE: database_obj.py
    @commands.command()
    async def db(self, ctx):
        """Command for setting up the database connection"""
        await ctx.send(view=dbbuttons(), ephemeral=True) # Send message with buttons to setup database connection and test connection using provided credentials