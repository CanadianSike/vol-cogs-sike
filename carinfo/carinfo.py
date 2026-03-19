from redbot.core import commands
from redbot.core.utils.views import SetApiModal
import discord
from discord import ui

from .database_obj import DatabaseSetup
from .database_obj import dbbuttons
from .carmodels_obj import CarBrands, MazdaCarList, ModelButtons
from .carmodels_obj import MazdaSuvList, ModelButtons
from .database_obj import DatabaseSetup


# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot

    # Command for users to input their car information. WIP.
    @commands.command()
    async def carinfo(self, ctx):
        """Command for users to input their car information"""
        await ctx.send("Please select your car model:", view=CarBrands())

    # Command for users to display their car information. WIP.
    @commands.command()
    async def mycar(self, ctx):
        """Command for users to display their car information"""
        # Pull car data from database and use embed for display.
        await ctx.send("NOT IMPLEMENTED YET")
    
    # Command for setting up the database connection, Summons button to allow for Modal based input. WIP
    @commands.command()
    async def db(self, ctx):
        """Command for setting up the database connection"""
        await ctx.send(view=dbbuttons())