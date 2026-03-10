import discord


class ModelButtons(discord.ui.Button): #Class for storing model buttons, will be used for car_attributes.
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def mazda2_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You selected Mazda 2!")