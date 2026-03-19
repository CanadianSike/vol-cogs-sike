import discord
from discord import ui
import psycopg2
from psycopg2 import pool
import redbot.core

# Class for calling button to summon Modal. Allows for database input.
class dbbuttons(discord.ui.View):
    @discord.ui.button(label="Setup Database Connection", style=discord.ButtonStyle.primary)
    async def setupdb(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(DatabaseSetup())

# Class for database credentials and connection pool info. 
class DatabaseSetup(discord.ui.Modal, title="Database Setup"):
    """Modal for setting up the database connection."""
    db_name = ui.TextInput(label="Database Name", placeholder="Enter your database name", required=True)
    db_user = ui.TextInput(label="Database User", placeholder="Enter your database user", required=True)
    db_password = ui.TextInput(label="Database Password", placeholder="Enter your database password", required=True, style=discord.TextStyle.short)
    db_host = ui.TextInput(label="Database Host", placeholder="Enter your database host", required=True)
    db_port = ui.TextInput(label="Database Port", placeholder="Enter your database port", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Database Name: {self.db_name.value}, Database User: {self.db_user.value}", ephemeral=True)
