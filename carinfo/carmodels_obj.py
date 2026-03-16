import discord



# View Class
class MazdaModelButtons(discord.ui.View):
#*************************************************************************************************
# This class will create buttons for Mazda model selection(s).
#*************************************************************************************************
# 
    # Mazda SUV Button
    @discord.ui.button(label="SUV", style=discord.ButtonStyle.primary)
    async def mazda2_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected SUV!", ephemeral=True, view=MazdaSuvList())

    # Mazda Sedan/Hatchback/Coupe Button
    @discord.ui.button(label="Sedan/Hatchback/Coupe", style=discord.ButtonStyle.primary)
    async def mazda3_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Sedan/Hatchback/Coupe!", ephemeral=True, view=MazdaCarList())
        






class MazdaCarList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Mazda Car models.
#*************************************************************************************************
    @discord.ui.select(placeholder="Select yourmodel", options=[
        discord.SelectOption(label="Mazda 2", description="Subcompact sedan/hatchback"),
        discord.SelectOption(label="Mazda 3", description="Compact sedan/hatchback"),
        discord.SelectOption(label="Mazda 6", description="Midsize sedan"),
        discord.SelectOption(label="Miata", description="Sports car")])
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]}!", ephemeral=True)

    
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="1.5L", description="1.5L engine option"),
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]} engine!", ephemeral=True)

class MazdaSuvList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Mazda SUV models.
#*************************************************************************************************
    @discord.ui.select(placeholder="Select your SUV model", options=[
        discord.SelectOption(label="CX-3", description="Subcompact SUV"),
        discord.SelectOption(label="CX-30", description="Compact SUV"),
        discord.SelectOption(label="CX-5", description="Midsize SUV"),
        discord.SelectOption(label="CX-50", description="Midsize SUV"),
        discord.SelectOption(label="CX-9", description="Full-size SUV"),
        discord.SelectOption(label="CX-90", description="Full-size SUV")])
    async def suv_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]} SUV model!", ephemeral=True)

    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option"),
        discord.SelectOption(label="2.5L Turbo", description="2.5L Turbo engine option")])
    async def suv_engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]} engine for your SUV!", ephemeral=True)