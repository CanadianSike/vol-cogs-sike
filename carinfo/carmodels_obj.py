import discord
from discord import ui
import asyncio
from . import database_obj

class UserCarInfo:
    # Place holders for car info
    def __init__(self, user_id):
        self.user_id = user_id
        self.vendor = None
        self.model = None
        self.engine_size = None
        self.is_tuned = None
        self.tune_revision = None

#*************************************************************************************************
# This class will create a list of available car models.
#*************************************************************************************************
class CarBrands(discord.ui.View):
    def __init__(self, car_obj):
        super().__init__()
        self.car = car_obj

    @discord.ui.button(label="Mazda", style=discord.ButtonStyle.primary)
    async def mazda_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.car.vendor = "Mazda"
        next_option = MazdaList(self.car)
        await interaction.response.edit_message(view=next_option)

            

    @discord.ui.button(label="Toyota", style=discord.ButtonStyle.primary)
    async def toyota_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Sorry, eh", ephemeral=True)

#*************************************************************************************************
# This class will create a list of available Mazda Car models.
#*************************************************************************************************
class MazdaList(discord.ui.View):
    def __init__(self, car_obj):
        super().__init__()
        self.car = car_obj

    # Mazda Car Model Selection.
    @discord.ui.select(placeholder="Select your Model", options=[
        discord.SelectOption(label="Mazda 2", description="Subcompact sedan/hatchback"),
        discord.SelectOption(label="Mazda 3", description="Compact sedan/hatchback"),
        discord.SelectOption(label="Mazda 6", description="Midsize sedan"),
        discord.SelectOption(label="Miata", description="Sports car"),
        # Mazda SUV Model Selection.
        discord.SelectOption(label="CX-3", description="Subcompact SUV"),
        discord.SelectOption(label="CX-30", description="Compact SUV"),
        discord.SelectOption(label="CX-5", description="Midsize SUV"),
        discord.SelectOption(label="CX-50", description="Midsize SUV"),
        discord.SelectOption(label="CX-9", description="Full-size SUV"),
        discord.SelectOption(label="CX-90", description="Full-size SUV")])
    
    async def model_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.car.model = select.values[0] # Store selected model for later use
        await interaction.response.defer() # Defer response to allow for confirmation without sending multiple messages

    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="1.5L", description="1.5L engine option"),
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.car.engine_size = select.values[0] # Store selected engine for later use
        await interaction.response.defer() # Defer response to allow for confirmation without sending multiple messages

    # Back button to return to model selection view
    @discord.ui.button(label="Go back", style=discord.ButtonStyle.secondary) # Button to return to model selection view
    async def back_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        back_option = CarBrands(self.car)
        await interaction.response.edit_message(view=back_option) # Send user back to model selection view when back button is clicked SEE: ModelButtons class above

    # Confirm button to finalize selection and display chosen model and engine
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success) # Button to confirm selection and display chosen model and engine
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if hasattr(self.car, 'model') and hasattr(self.car, 'engine_size'):
            next_option = IsTunedButtons(self.car)
            await interaction.response.edit_message(content="Are you currently tuned?",view=next_option)
        else:
            await interaction.response.send_message("Please select both a model and an engine.", ephemeral=True)

#*************************************************************************************************
# This class will create buttons to ask if the user's car is tuned or not. This will be used to determine if the user needs to input their tune revision or not.
#*************************************************************************************************
class IsTunedButtons(discord.ui.View):
    def __init__(self, car_obj):
        super().__init__()
        self.car = car_obj

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
    async def yes_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.car.is_tuned = True
        next_option = TuneRevisionInput(self.car)
        await interaction.response.send_modal(next_option)
    
    @discord.ui.button(label="No", style=discord.ButtonStyle.danger)
    async def no_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.car.is_tuned = False
        self.car.tune_revision = "N/A"
        await interaction.response.defer(ephemeral=True)
        await database_obj.sync_car_info(interaction, self.car)
        await interaction.followup.send("Car data saved to DB")

class TuneRevisionInput(discord.ui.Modal, title="Tune Revision Input"):
    def __init__(self, car_obj):
        super().__init__()
        self.car = car_obj

    """Modal for inputting tune revision."""
    tune_revision = ui.TextInput(label="Tune Revision", placeholder="Enter your tune revision (e.g. v1.0, v1.1, etc.)", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        self.car.tune_revision = self.tune_revision.value
        await interaction.response.defer(ephemeral=True)
        await database_obj.sync_car_info(interaction, self.car)
        await interaction.followup.send("Car data is saved to DB")

        
