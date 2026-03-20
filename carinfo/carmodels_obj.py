import discord



class CarBrands(discord.ui.View):
    @discord.ui.button(label="Mazda", style=discord.ButtonStyle.primary)
    async def mazda_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons())
    @discord.ui.button(label="Toyota", style=discord.ButtonStyle.primary)
    async def toyota_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons())



class ModelButtons(discord.ui.View):
#*************************************************************************************************
# Buttons will be called to select car catagory. SUV/CAR/ETC
#*************************************************************************************************
# 

    @discord.ui.button(label="SUV", style=discord.ButtonStyle.primary)
    async def suv_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=MazdaSuvList())

    # Mazda Sedan/Hatchback/Coupe Button
    @discord.ui.button(label="Sedan/Hatchback/Coupe", style=discord.ButtonStyle.primary)
    async def car_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=MazdaCarList())





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
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_model = select.values[0] # Store selected model for later use
        await interaction.response.defer()
    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="1.5L", description="1.5L engine option"),
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_engine = select.values[0] # Store selected engine for later use
        await interaction.response.defer()

    @discord.ui.button(label="Go back", style=discord.ButtonStyle.secondary)
    async def back_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons())
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success)
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if hasattr(self, 'selected_model') and hasattr(self, 'selected_engine'):
            await interaction.response.send_message(f"Car selection confirmed: {self.selected_model} with {self.selected_engine} engine.", ephemeral=True)
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
        await interaction.response.defer()
    # Engine Size Selection.
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def suv_engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.selected_model = select.values[0] # Store selected model for later use
        await interaction.response.defer()
    @discord.ui.button(label="Go back", style=discord.ButtonStyle.secondary)
    async def back_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(view=ModelButtons())
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.success)
    async def confirm_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if hasattr(self, 'selected_model') and hasattr(self, 'selected_engine'):
            await interaction.response.send_message(f"Car selection confirmed: {self.selected_model} with {self.selected_engine} engine.", ephemeral=True)
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