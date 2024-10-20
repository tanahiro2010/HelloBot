import discord
class verify_button(discord.ui.View):
    def __init__(self, role_id: int):
        self.role_id = role_id
        super().__init__(timeout=None)

    @discord.ui.button(label='verify', style=discord.ButtonStyle.green)
    async def verify(self, button: discord.ui.Button, interaction: discord.Interaction.response):
        await interaction.response.defer()
        role = interaction.guild.get_role(self.role_id)
        if role is None:
            await interaction.followup.send(embed=discord.Embed(
                title="Error",
                description="Role not found",
                colour=discord.Color.red()
            ))
            return
        try:
            await interaction.user.add_roles(role)
        except discord.Forbidden:
            await interaction.followup.send(embed=discord.Embed(
                title="Error",
                description="This bot doesn't have permission to add you role",
                colour=discord.Color.red()
            ))
            return

        await interaction.followup.send(embed=discord.Embed(
            title="Success",
            description="Add <@&{}> to you",
            colour=discord.Color.green()
        ))
