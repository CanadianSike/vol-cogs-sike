import discord



# View Class
class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)  # Set timeout for the view

# Button Class
class ModelButtons():
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)