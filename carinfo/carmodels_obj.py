import discord



# View Class
class MazdaModelButtons(discord.ui.View):
#*************************************************************************************************
# This class will create buttons for Mazda model selection(s).
#*************************************************************************************************
##### Sedan/Hatchback/Miata Models #####

    # Mazda 2 Button
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def mazda2_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda 2!", ephemeral=True)
    # Mazda 3 Button
    @discord.ui.button(label="Mazda 3", style=discord.ButtonStyle.primary)
    async def mazda3_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda 3!", ephemeral=True)
    # Mazda 6 Button
    @discord.ui.button(label="Mazda 6", style=discord.ButtonStyle.primary)
    async def mazda6_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda 6!", ephemeral=True)
    # Mazda MX-5 Button
    @discord.ui.button(label="Mazda MX-5", style=discord.ButtonStyle.primary)
    async def mazda_mx5_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda MX-5!", ephemeral=True)

##### SUV Models #####  
    
    # Mazda CX-5 Button
    @discord.ui.button(label="Mazda CX-5", style=discord.ButtonStyle.primary)
    async def mazda_cx5_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-5!", ephemeral=True)
    # Mazda CX-9 Button
    @discord.ui.button(label="Mazda CX-9", style=discord.ButtonStyle.primary)
    async def mazda_cx9_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-9!", ephemeral=True)
    # Mazda CX-30 Button
    @discord.ui.button(label="Mazda CX-30", style=discord.ButtonStyle.primary)
    async def mazda_cx30_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-30!", ephemeral=True)
    # Mazda CX-50 Button
    @discord.ui.button(label="Mazda CX-50", style=discord.ButtonStyle.primary)
    async def mazda_cx50_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-50!", ephemeral=True)
    # Mazda CX-90 Button
    @discord.ui.button(label="Mazda CX-90", style=discord.ButtonStyle.primary)
    async def mazda_cx90_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-90!", ephemeral=True)







class MazdaModelList(discord.ui.View):
#*************************************************************************************************
# This class will create a list of available Mazda models.
#*************************************************************************************************
    @discord.ui.select(placeholder="Select a Mazda model", options=[
        discord.SelectOption(label="Mazda 2", description="Subcompact sedan/hatchback"),
        discord.SelectOption(label="Mazda 3", description="Compact sedan/hatchback")])
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]}!", ephemeral=True)
    @discord.ui.select(placeholder="Select engine size", options=[
        discord.SelectOption(label="2.0L", description="2.0L engine option"),
        discord.SelectOption(label="2.5L", description="2.5L engine option")])
    async def engine_select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected {select.values[0]} engine!", ephemeral=True)