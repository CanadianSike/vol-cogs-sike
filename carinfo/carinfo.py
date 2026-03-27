from redbot.core import commands
from redbot.core.utils.views import SetApiModal
import discord
from discord import ui

from .database_obj import DatabaseSetup
from .database_obj import dbbuttons
from .carmodels_obj import UserCarInfo, CarBrands



# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot
        self.garage ={ }

    # Command for users to input their car information. SEE: carmodels_obj.py
    @commands.command()
    async def carinfo(self, ctx):
        """Command for users to input their car information"""
        new_car = UserCarInfo(ctx.author.id)
        view = CarBrands(car_obj=new_car)
        await ctx.send("Please input your car information:", view=view) # Send message with buttons to select car brand and model

    # Command for users to display their car information. SEE:
    @commands.command()
    async def mycar(self, ctx):
        """Command for users to display their car information"""
        # Pull car data from database and use embed for display.
        await ctx.send("NOT IMPLEMENTED YET")
    
    # Command for setting up the database connection, Summons button to allow for Modal based input. SEE: database_obj.py
    @commands.command()
    async def db(self, ctx):
        """Command for setting up the database connection"""
        await ctx.send(view=dbbuttons(), ephemeral=True) # Send message with buttons to setup database connection and test connection using provided credentials