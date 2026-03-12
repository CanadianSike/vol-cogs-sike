import discord



# View Class
class ModelButtons(discord.ui.View):
    # This class will create buttons for car model selection

    # Mazda 2 Button
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def mazda2_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("You selected Mazda 2!", ephemeral=True)
    # Mazda 3 Button
    @discord.ui.button(label="Mazda 3", style=discord.ButtonStyle.primary)
    async def mazda3_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("You selected Mazda 3!", ephemeral=True)
 
