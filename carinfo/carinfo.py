import discord
from discord import ui, app_commands
from redbot.core import commands

import carmodels_obj
import database_obj
from .database_obj import dbbuttons, DatabaseSetup
from .carmodels_obj import UserCarInfo, CarBrands




# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot
        self.active_builds = { }

    # Command for users to input their car information. SEE: carmodels_obj.py
    @commands.command()
    async def caradd(self, ctx):
        """Command for users to input their car information"""
        grab_user = UserCarInfo(ctx.author.id)
        view = CarBrands(car_obj=grab_user)
        await ctx.send(view=view) # Send message with buttons to select car brand and model

    # Command for users to display their car information. SEE:
    @commands.command()
    async def carlist(self, ctx):
        """Command for users to display their list of available cars"""
        cars = await database_obj.pull_car_info(None, ctx.author.id) # Pull all car related info from DB that matches the user's ID

        if not cars: # If there is no cars under the user's ID in the DB tell them to add one.
            return await ctx.send("Your garage is empty. You should add some cars!")
        
        embed = discord.Embed( # Create embed for Garage display in chat.
            title=f"{ctx.author.display_name}'s Garage", # Embed title
            color=discord.Color.blue() # Embed colour
        )
        embed.set_thumbnail(url=ctx.author.display_avatar.url) # Pulls user current PFP and adds it into the embed

        for car in cars:
            vendor, model, engine, tuned, revision = car
            status =f"✅ Tuned [REV: {revision}]" if tuned else "❌ Not Tuned" # Checks is_tuned boolean in DB

            embed.add_field(
                name = f"{vendor} {model} {engine}", # Title row of each car in embed. 
                value = status,                      # Displays tune status and Revision under each car title.
                inline = False                       # Sets embed to be Vertical and not horizontal.
            )
        await ctx.send(embed=embed) 
    
    @commands.hybrid_command(name = "carrev", description = " Update the Tune Revision of your car!")
    @app_commands.describe(model_name = """The model of your car. Ex. "Mazda3".""", new_revision = """The new Revision Version. Ex. "V1.0, V2.1" """)
    async def carrev(self, ctx: commands.Context, model_name: str, new_revision: str):
        async with ctx.typing(): #THIS IS NEEDED FOR "/" COMMANDS TO WORK IN THIS CONTEXT
            try: 
                await database_obj.update_car_info(ctx.interaction, ctx.author.id, model_name, new_revision)
                await ctx.send(f"✅ Successfully updated **{model_name}** to revision **{new_revision}**!")
            except Exception as e:
                await ctx.senf(f"❌ Failed to update, Error:{e}")


    # Command for setting up the database connection, Summons button to allow for Modal based input. SEE: database_obj.py
    @commands.command()
    async def db(self, ctx):
        """Command for setting up the database connection"""
        await ctx.send(view=dbbuttons(), ephemeral=True) # Send message with buttons to setup database connection and test connection using provided credentials