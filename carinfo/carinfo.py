from redbot.core import commands, app_commands 
import discord
from .carmodels_obj import MazdaCarList, MazdaModelButtons
from .carmodels_obj import MazdaModelList


# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def car(self, ctx):
        """Command for users to input their car information"""
        await ctx.send("Please select your car model:", view=MazdaModelButtons())

    @commands.command()
    async def mazdalist(self, ctx):
        """Command for users to view the list of available Mazda models"""
        await ctx.send("Here are the available Mazda models:", view=MazdaCarList())

class CarAttributes():
    """Class for storing car attributes, will be used for carinfo."""