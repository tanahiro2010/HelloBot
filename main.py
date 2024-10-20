import json
import discord
import discord.app_commands as commands
from func.log import *
from assets.verify import *

logger = Logger()


def load(file: str) -> json or None:
    return json.loads(open(file).read())


def save(file: str, data: json or None) -> None:
    open(file, 'w').write(json.dumps(data))
    return


def load_permission():
    return load('./permission.json')


def save_permission(permission: json or None) -> None:
    save('./permission.json', permission)
    return



config = load('./config.json')
token = config['token']

intents = discord.Intents.all()
client = discord.ext.commands.Bot(command_prefix="!", intents=discord.Intents.all())
tree = commands.CommandTree(client)

@client.event
async def on_ready() -> None:
    logger.log('Logged in as ' + client.user.name)
    return

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return

    logger.log(
        '\nMessage--\nFROM_GUILD_NAME: {}\nFROM_GUILD_ID: {}\nFROM_GUILD_URL: {}\nFROM_CHANNEL_NAME: {}\nFROM_CHANNEL_ID: {}\nFROM_USER_NAME: {}\nFROM_USER_ID: {}\nMessage: {}\n--END'.format(
            message.guild.name,
            message.guild.id,
            await message.channel.create_invite(),
            message.channel.name,
            message.channel.id,
            message.author.name,
            message.author.id,
            message.content
        )
    )

    return

@client.event
async def on_guild_join(guild: discord.Guild) -> None:
    role = await guild.create_role(
        name="HelloUser",
        color=discord.Color.blurple(),
    )
    permission_data = load_permission()
    permission_data[guild.id] = role.id
    save_permission(permission_data)
    await guild.owner.add_roles(role)

    return

@tree.command(name='verify', description='create board to add role')
@commands.describe(role="付与するロール")
async def verify_command(role: discord.Role, interaction: discord.Interaction):
    await interaction.response.defer()
    permission_data = load_permission()
    admin_role_id = permission_data[str(interaction.guild.id)]
    admin_role = interaction.guild.get_role(admin_role_id)
    hasPermission = False
    for role in interaction.user.roles:
        if role.id == admin_role.id:
            hasPermission = True
            break

    if hasPermission:
        embed = discord.Embed(
            title="Verify",
            description="認証します",
            color=discord.Color.blue()
        )
        board = verify_button(role.id)
        await interaction.followup.send(embed=embed, view=board)
    else:
        embed = discord.Embed(
            title="Error",
            description="You don't have permission to run this command",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=embed, view=verify_button)

    return

client.run(token)
