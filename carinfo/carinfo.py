from redbot.core import commands, app_commands 
import discord


# Classname should be CamelCase and the same spelling as the folder
class CarInfo(commands.Cog):
    """Cog for keeping track of mods and tune revision(s) per user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def model(self, ctx):
        """Command for users to input their car information"""
        await ctx.send("Please select your car model:", view=ModelButtons())

    class ModelButtons(discord.ui.View): #Class for storing model buttons, will be used for car_attributes.
    
        # Mazda 2 Button
        @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)  
        # Mazda 3 Button
        @discord.ui.button(label="Mazda 3", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda 5 Button
        @discord.ui.button(label="Mazda 5", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):   
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda 6 Button
        @discord.ui.button(label="Mazda 6", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-3 Button
        @discord.ui.button(label="Mazda CX-3", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-5 Button
        @discord.ui.button(label="Mazda CX-5", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-9 Button
        @discord.ui.button(label="Mazda CX-9", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-30 Button
        @discord.ui.button(label="Mazda CX-30", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-50 Button
        @discord.ui.button(label="Mazda CX-50", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)
        # Mazda CX-90 Button
        @discord.ui.button(label="Mazda CX-90", style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(content=f"You selected {button.label}", view=self)

class CarAttributes():
    """Class for storing car attributes, will be used for carinfo."""