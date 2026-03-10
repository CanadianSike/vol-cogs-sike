import discord


class ModelButtons(discord.ui.Button): #Class for storing model buttons, will be used for car_attributes.
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)