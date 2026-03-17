import discord
from discord import ui
import psycopg2
from psycopg2 import pool
import redbot.core


# Class for database credentials and connection pool info. 
class DatabaseSetup(ui.Modal, title="Database Setup"):
    """Modal for setting up the database connection."""
    db_name = ui.Label(text="Database Name", component=ui.TextInput())
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Database Name: {self.db_name.value}", ephemeral=True)