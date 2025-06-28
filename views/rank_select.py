import discord
from utils.language_database import languages
from utils.settings_store import get_language
from utils.autorole_roles import TIERS
from views.division_select import DivisionSelectView

class RankSelectView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=120)
        self.cog = cog
        self.add_item(self.TierDropdown(self))

    class TierDropdown(discord.ui.Select):
        def __init__(self, parent):
            self.parent = parent
            options = [discord.SelectOption(label=tier, value=tier) for tier in TIERS]
            super().__init__(
                placeholder="Wähle einen Hauptrang aus...",
                options=options,
                custom_id="tier_select"
            )

        async def callback(self, interaction: discord.Interaction):
            tier = self.values[0]
            divisions = [f"{tier} {i}" for i in range(1, 4)] if tier not in ["Unranked", "Radiant"] else [tier]
            await interaction.response.edit_message(
                embed=discord.Embed(
                    title=f"{tier} → Unterrang wählen",
                    description=languages["autoroles"]["choose_division"][get_language(interaction.guild.id)],
                    color=discord.Color.purple()
                ),
                view=DivisionSelectView(self.parent.cog, divisions)
            )
