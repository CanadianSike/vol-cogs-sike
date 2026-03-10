import discord



# View Class
class ModelButtons(discord.ui.View):
    # This class will create buttons for car model selection

    # Mazda 2 Button
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda 3 Button
    @discord.ui.button(label="Mazda 3", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda 6 Button
    @discord.ui.button(label="Mazda 6", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-5 Button
    @discord.ui.button(label="Mazda CX-5", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-9 Button
    @discord.ui.button(label="Mazda CX-9", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda MX-5 Button
    @discord.ui.button(label="Mazda MX-5", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-30 Button
    @discord.ui.button(label="Mazda CX-30", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-50 Button
    @discord.ui.button(label="Mazda CX-50", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)
    # Mazda CX-90 Button
    @discord.ui.button(label="Mazda CX-90", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)