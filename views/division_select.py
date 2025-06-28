import discord
from views.role_assign import RoleAssignView
from utils.language_database import languages
from utils.settings_store import get_language

class DivisionSelectView(discord.ui.View):
    def __init__(self, cog, divisions):
        super().__init__(timeout=120)
        self.cog = cog
        self.divisions = divisions
        self.add_item(self.DivisionDropdown(self))

    class DivisionDropdown(discord.ui.Select):
        def __init__(self, parent):
            self.parent = parent
            options = [discord.SelectOption(label=div, value=div) for div in parent.divisions]
            super().__init__(
                placeholder="Wähle einen Rang mit Stufe aus...",
                options=options,
                custom_id="division_select"
            )

        async def callback(self, interaction: discord.Interaction):
            lang = get_language(interaction.guild.id)
            await interaction.response.edit_message(
                embed=discord.Embed(
                    title=f"{self.values[0]} → Rolle zuweisen",
                    description=languages["autoroles"]["choose_role"][lang],
                    color=discord.Color.purple()
                ),
                view=RoleAssignView(self.parent.cog, self.values[0])
            )
