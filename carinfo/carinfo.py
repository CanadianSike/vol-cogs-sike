from redbot.core import commands, app_commands 
import discord
import psycopg2

from .database_obj import DatabaseSetup
from .carmodels_obj import MazdaCarList, ModelButtons
from .carmodels_obj import MazdaSuvList, ModelButtons


# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def carinfo(self, ctx):
        """Command for users to input their car information"""
        await ctx.send("Please select your car model:", view=ModelButtons())

    @commands.command()
    async def mycar(self, ctx):
        """Command for users to display their car information"""
        # Pull car data from database and use embed for display.
        await ctx.send("NOT IMPLEMENTED YET")
        
    @commands.command()
    async def database(self, ctx):
        await ctx.send(DatabaseSetup())


