import discord

from redbot.core import commands, app_commands 

class carinfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    car_attributes = ["Model", "Year", "Trim", "Engine", "Transmission", "Drivetrain", "Mods"]
    model = ["Mazda 2", "Mazda 3", "Mazda 5", "Mazda 6", "Mazda CX-3", "Mazda CX-5", "Mazda CX-9", "Mazda CX-30", "Mazda-CX50", "Mazda-CX90" "Miata"]
    year = int == range(1990, 2025)
    trim = str
    engine = [1.5, 2.0, 2.2, 2.5, 3.3]
    transmission = ["Automatic", "Manual"]
    drivetrain = ["FWD", "RWD", "AWD"]


    def __init__(self, bot):
        self.bot = bot

    @app_commands.commands.command()
    @app_commands.guild_only()
    async def testsike(self, ctx):
        await interation.response.send_message("This is a test", ephemeral=True)


    @app_commands.commands.command()
    @app_commands.guild_only()
    async def carinfo(self, ctx):
        """Command for users to input their car information"""
        embed = discord.Embed(colour=discord.colour title="Your Mazda", description="Please fill out the following information about your car:", color=discord.Color.blue())
        