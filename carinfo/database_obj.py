import discord
from discord import ui
import psycopg2
import redbot.core
# Class for calling button to summon Modal. Allows for database input and connection testing.
class dbbuttons(discord.ui.View):
    @discord.ui.button(label="Setup Database Connection", style=discord.ButtonStyle.primary) # Button to summon DatabaseSetup Modal
    async def setupdb(self, interaction: discord.Interaction, button: discord.ui.Button): # Setup Database button callback
        await interaction.response.send_modal(DatabaseSetup()) # Call DatabaseSetup Modal when button is clicked
    @discord.ui.button(label='Test Connection', style=discord.ButtonStyle.secondary)# Button to test database connection using provided credentials
    async def testdb(self, interaction: discord.Interaction, button: discord.ui.Button): # Test Database button callback
        await interaction.response.send_message("Testing database connection...", ephemeral=True)
        try:
            # Attempt to connect to the database using the provided credentials
            connection = psycopg2.connect(
                dbname=DatabaseSetup.db_name.value, # Database name from Modal input
                user=DatabaseSetup.db_user.value, # Database username from Modal input
                password=DatabaseSetup.db_password.value, # Database password from Modal input
                host=DatabaseSetup.db_host.value, # Database host from Modal input
                port=DatabaseSetup.db_port.value # Database port from Modal input (typically 5432 for PostgreSQL)
            )
            cur = connection.cursor()
            cur.execute("SELECT version();")
            cur.execute()
            db_version = cur.fetchone()
            await interaction.followup.send(f"Connected to PostgreSQL database version: {db_version}", ephemeral=True)
            await interaction.followup.send(f"", ephemeral=True)
            connection.close()
            await interaction.followup.send("Database connection successful!", ephemeral=True)# If connection is successful, send success message
        except Exception as e:
            await interaction.followup.send(f"Error occurred while testing database connection: {e}", ephemeral=True)# If connection fails, send error message with error log
    @discord.ui.button(label="Query tables", style=discord.ButtonStyle.secondary) # Button to query database tables and display results
    async def querydb(self, interaction: discord.Interaction, button: discord.ui.Button): # Query Database button callback
        await interaction.response.send_message("Querying database tables...", ephemeral=True)
        try:
            # Attempt to connect to the database using the provided credentials
            connection = psycopg2.connect(
                dbname=DatabaseSetup.db_name.value, # Database name from Modal input
                user=DatabaseSetup.db_user.value, # Database username from Modal input
                password=DatabaseSetup.db_password.value, # Database password from Modal input
                host=DatabaseSetup.db_host.value, # Database host from Modal input
                port=DatabaseSetup.db_port.value # Database port from Modal input (typically 5432 for PostgreSQL)
            )
            cur = connection.cursor()
            cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';") # Query to get list of tables in the .public schema
            tables = cur.fetchall()
            if tables:
                table_list = "\n".join([table[0] for table in tables]) # Format table names into a string for display
                await interaction.followup.send(f"Tables in the database:\n{table_list}", ephemeral=True) # Send list of tables as a message
            else:
                await interaction.followup.send("No tables found in the database.", ephemeral=True) # If no tables are found, send message
            connection.close()
        except Exception as e:
            await interaction.followup.send(f"Error occurred while querying database: {e}", ephemeral=True) # If query fails, send error message with error log





# Class for database credentials and connection pool info. 
class DatabaseSetup(discord.ui.Modal, title="Database Setup"):
    """Modal for setting up the database connection."""
    db_name = ui.TextInput(label="Database Name", placeholder="Enter your database name", required=True) # DB name
    db_user = ui.TextInput(label="Database User", placeholder="Enter your database user", required=True) # DB user
    db_password = ui.TextInput(label="Database Password", placeholder="Enter your database password", required=True, style=discord.TextStyle.short) # DB password
    db_host = ui.TextInput(label="Database Host", placeholder="Enter your database host", required=True) # DB host IP/URL
    db_port = ui.TextInput(label="Database Port", placeholder="Enter your database port", required=True) # DB port, default is usually 5432 for PostgreSQL
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Database Name: {self.db_name.value}, Database User: {self.db_user.value}, Database Host: {self.db_host.value}, Database Port: {self.db_port.value}", ephemeral=True)


# Functionfor sending user info to database.
def UserInfoToDatabase(user_id, car_brand, car_model, engine_size, tune_revision):
    try:
    
        # Attempt to connect to the database using the provided credentials
        connection = psycopg2.connect(
        dbname=DatabaseSetup.db_name.value, # Database name from Modal input
        user=DatabaseSetup.db_user.value, # Database username from Modal input
        password=DatabaseSetup.db_password.value, # Database password from Modal input
        host=DatabaseSetup.db_host.value, # Database host from Modal input
        port=DatabaseSetup.db_port.value # Database port from Modal input (typically 5432 for PostgreSQL)
        )
        cur = connection.cursor()
        cur.execute('INSERT INTO %s (user_id, car_brand, car_model, engine_size, tune_revision) VALUES (%s, %s, %s, %s, %s)', (user_id, car_brand, car_model, engine_size, tune_revision)) # Example query to insert user info into database table

    except Exception as e:
        print(f"Error occurred while inserting user info into database: {e}") # If insertion fails, print error message with error log
    finally:
        if connection:
            connection.commit() # Commit changes to the database
            connection.close() # Close the database connection