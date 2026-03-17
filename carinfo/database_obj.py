import discord
from discord import ui
import psycopg2
from psycopg2 import pool
import redbot.core


# Class for database credentials and connection pool info. 
class DatabaseSetup(ui.Modal, title="Database Setup"):
    """Modal for setting up the database connection."""
    db_name = ui.TextInput(label="Database Name", placeholder="Database name", required=True)
    db_user = ui.TextInput(label="Database User", placeholder="Database username", required=True)
    db_password = ui.TextInput(label="Database Password", placeholder="Database password", required=True, style=discord.TextStyle.short)
    db_host = ui.TextInput(label="Database Host", placeholder="Database host (e.g., localhost/IP address)", required=True)
    db_port = ui.TextInput(label="Database Port", placeholder="Database port (e.g., 5432/8086)", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Database Name: {self.db_name.value}, Database User: {self.db_user.value}, Database Host: {self.db_host.value}, Database Port: {self.db_port.value}", ephemeral=True)