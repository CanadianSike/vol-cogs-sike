from redbot.core import commands, app_commands 
import discord
from .carmodels_obj import ModelButtons


# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def model(self, ctx):
        """Command for users to input their car information"""
        await ctx.send("Please select your car model:", view=ModelButtons())


class CarAttributes():
    """Class for storing car attributes, will be used for carinfo."""