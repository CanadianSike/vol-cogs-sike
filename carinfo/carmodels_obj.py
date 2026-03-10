import discord



# View Class
class ModelButtons(discord.ui.View):
    # This class will create buttons for car model selection

    # Mazda 2 Button
    @discord.ui.button(label="Mazda 2", row=0, slot=0, style=discord.ButtonStyle.primary)
    async def mazda2_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda 3 Button
    @discord.ui.button(label="Mazda 3", slot=1, style=discord.ButtonStyle.primary)
    async def mazda3_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda 6 Button
    @discord.ui.button(label="Mazda 6", row=2, style=discord.ButtonStyle.primary)
    async def mazda6_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-5 Button
    @discord.ui.button(label="Mazda CX-5", row=3, style=discord.ButtonStyle.primary)
    async def mazda_cx5_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-9 Button
    @discord.ui.button(label="Mazda CX-9", row=4, style=discord.ButtonStyle.primary)
    async def mazda_cx9_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda MX-5 Button
