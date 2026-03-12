import discord



# View Class
class ModelButtons(discord.ui.View):
    # This class will create buttons for car model selection

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
    # Mazda CX-5 Button
    @discord.ui.button(label="Mazda CX-5", style=discord.ButtonStyle.primary)
    async def mazda_cx5_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-5!", ephemeral=True)
    # Mazda CX-9 Button
    @discord.ui.button(label="Mazda CX-9", style=discord.ButtonStyle.primary)
    async def mazda_cx9_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda CX-9!", ephemeral=True)
 
