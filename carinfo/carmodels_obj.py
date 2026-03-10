import discord



# View Class
class ModelButtons(discord.ui.View):
    @discord.ui.button(label="Mazda 2", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {button.label}!", ephemeral=True)