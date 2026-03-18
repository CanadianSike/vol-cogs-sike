import discord
from discord import ui
import psycopg2
from psycopg2 import pool
import redbot.core


# Class for database credentials and connection pool info. 
class DatabaseSetup(discord.ui.Modal, title="Database Setup"):
    """Modal for setting up the database connection."""
    db_name = ui.TextInput(label="Database Name", placeholder="Enter your database name", required=True)
    db_user = ui.TextInput(label="Database User", placeholder="Enter your database user", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Database Name: {self.db_name.value}, Database User: {self.db_user.value}", ephemeral=True)

