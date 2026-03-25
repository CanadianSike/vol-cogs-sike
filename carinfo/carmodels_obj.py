import discord
from discord import ui
import asyncio
from . import database_obj


#*************************************************************************************************
user_car_attr = {}

#*************************************************************************************************

class CarBrands(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available car models.
#*************************************************************************************************
    @discord.ui.button(label="Mazda", style=discord.ButtonStyle.primary)
    async def mazda_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons(), ephemeral=True)
        user_car_attr[self.selected_brand] = "Mazda"
    @discord.ui.button(label="Toyota", style=discord.ButtonStyle.primary)
    async def toyota_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Sorry, eh", ephemeral=True)



class MazdaCarList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Mazda Car models.
#*************************************************************************************************

    # Mazda Car Model Selection.
    @discord.ui.select(placeholder="Select yourmodel", options=[
        discord.SelectOption(label="Mazda 2", description="Subcompact sedan/hatchback"),
        discord.SelectOption(label="Mazda 3", description="Compact sedan/hatchback"),
        discord.SelectOption(label="Mazda 6", description="Midsize sedan"),
        discord.SelectOption(label="Miata", description="Sports car")])
    async def model_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_model = select.values[0] # Store selected model for later use
        await interaction.response.defer() # Defer response to allow for confirmation without sending multiple messages

    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="1.5L", description="1.5L engine option"),
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_engine = select.values[0] # Store selected engine for later use
        await interaction.response.defer() # Defer response to allow for confirmation without sending multiple messages

    # Back button to return to model selection view
    @discord.ui.button(label="Go back", style=discord.ButtonStyle.secondary) # Button to return to model selection view
    async def back_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons()) # Send user back to model selection view when back button is clicked SEE: ModelButtons class above

    # Confirm button to finalize selection and display chosen model and engine
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success) # Button to confirm selection and display chosen model and engine
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if hasattr(self, 'selected_model') and hasattr(self, 'selected_engine'):
            await interaction.response.send_message(view=IsTunedButtons(), ephemeral=True)
        else:
            await interaction.response.send_message("Please select both a model and an engine.", ephemeral=True)




class MazdaSuvList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Mazda SUV models.
#*************************************************************************************************

    # Mazda SUV Model Selection.
    @discord.ui.select(placeholder="Select your SUV model", options=[
        discord.SelectOption(label="CX-3", description="Subcompact SUV"),
        discord.SelectOption(label="CX-30", description="Compact SUV"),
        discord.SelectOption(label="CX-5", description="Midsize SUV"),
        discord.SelectOption(label="CX-50", description="Midsize SUV"),
        discord.SelectOption(label="CX-9", description="Full-size SUV"),
        discord.SelectOption(label="CX-90", description="Full-size SUV")])
    async def suv_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_model = select.values[0] # Store selected model for later use
        await interaction.response.defer() # Defer response to allow for engine selection without sending multiple messages SEE: engine_select_callback below

    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def suv_engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_engine = select.values[0] # Store selected engine for later use
        await interaction.response.defer() # Defer response to allow for confirmation without sending multiple messages SEE: confirm_callback below

    # Back button to return to model selection view
    @discord.ui.button(label="Go back", style=discord.ButtonStyle.secondary) # Button to return to model selection view
    async def back_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons()) # Send user back to model selection view when back button is clicked SEE: ModelButtons class above

    # Confirm button to finalize selection and display chosen model and engine
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success)
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if hasattr(self, 'selected_model') and hasattr(self, 'selected_engine'):
            await interaction.response.send_message(view=IsTunedButtons(), ephemeral=True)
        else:
            await interaction.response.send_message("Please select both a model and an engine.", ephemeral=True)

class ToyotaCarList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Toyota Car models.
#*************************************************************************************************
    # Toyota Car Model Selection.
    @discord.ui.select(placeholder="Select your Toyota model", options=[
        discord.SelectOption(label="Corolla", description="Compact sedan/hatchback"),
        discord.SelectOption(label="Camry", description="Midsize sedan"),
        discord.SelectOption(label="Supra", description="Sports car")])
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]}!", ephemeral=True)

    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="1.6L Turbo", description="1.6L Turbo engine option"),
        discord.SelectOption(label="1.8L", description="1.8L engine option"),
        discord.SelectOption(label="2.0L", description="2.0L engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]} engine!", ephemeral=True)


class ModelButtons(discord.ui.View):
#*************************************************************************************************
# Buttons will be called to select car catagory. SUV/CAR/ETC
#*************************************************************************************************
# 
    @discord.ui.button(label="SUV", style=discord.ButtonStyle.primary)
    async def suv_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=MazdaSuvList(), ephemeral=True)

    # Mazda Sedan/Hatchback/Coupe Button
    @discord.ui.button(label="Sedan/Hatchback/Coupe", style=discord.ButtonStyle.primary)
    async def car_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=MazdaCarList(), ephemeral=True)

class IsTunedButtons(discord.ui.View):
#*************************************************************************************************
# This class will create buttons to ask if the user's car is tuned or not. This will be used to determine if the user needs to input their tune revision or not.
#*************************************************************************************************
# 
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
    async def yes_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(TuneRevisionInput())
    

    @discord.ui.button(label="No", style=discord.ButtonStyle.danger)
    async def no_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(ephemeral=True)

class TuneRevisionInput(discord.ui.Modal, title="Tune Revision Input"):
    """Modal for inputting tune revision."""
    tune_revision = ui.TextInput(label="Tune Revision", placeholder="Enter your tune revision (e.g. v1.0, v1.1, etc.)", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Your information has been saved!", ephemeral=True)
        await asyncio.sleep(1) # Sleep for a moment to ensure the first message is sent before sending the tune revision information
        user_id = interaction.user.id # Get user ID from interaction
        await interaction.followup.send(f"Your tune revision: {self.tune_revision.value} and user ID: {user_id}", ephemeral=True) #! Remove after testing
        await asyncio.sleep(1) # Sleep for a moment to ensure the previous message is sent before attempting to send the tune revision information to the database
        await interaction.followup.send(f"{user_id},{user_car_attr.selected_brand},{self.selected_model}, {self.selected_engine}, {self.tune_revision.value}")
        #await database_obj.user_info_to_database(user_id, self.selected_brand, self.selected_model, self.selected_engine, self.tune_revision.value) # Call the function to send user info to database
