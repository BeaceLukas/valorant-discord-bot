# utils/language_database.py

languages = {
    # Fehlermeldungen & allgemeine Hinweise
    "errors": {
        "no_account": {
            "en": "❌ No linked account found. Use /link add to verify your Riot ID."
        },
        "invalid_tagline": {
            "en": "❌ Invalid tagline format. Use Name#Tag."
        },
        "api_down": {
            "en": "❌ API error. Please try again later."
        },
        "rate_limited": {
            "en": "⏳ Rate limit reached. Please wait a moment."
        },
        "not_admin": {
            "en": "❌ You need to be an administrator to use this command."
        }
    },

    # /stats command
    "stats": {
        "title": {
            "en": "{tagline}'s Stats"
        },
        "rank": {
            "en": "Rank"
        },
        "mmr_change": {
            "en": "MMR Change"
        }
    },

    # /game command
    "game": {
        "title": {
            "en": "Recent Matches for {tagline}"
        },
        "agent": {
            "en": "Agent"
        },
        "kda": {
            "en": "K/D/A"
        },
        "kd": {
            "en": "KD"
        },
        "hs": {
            "en": "HS%"
        },
        "no_data": {
            "en": "❌ No match data found."
        }
    },

    # /leaderboard command
    "leaderboard": {
        "title": {
            "en": "Server Leaderboard"
        },
        "anonymous": {
            "en": "Anonymous"
        },
        "not_enough_data": {
            "en": "❌ No leaderboard data available yet."
        }
    },

    # /settings command
    "settings": {
        "language_updated": {
            "en": "✅ Language updated to English."
        },
        "choose_language": {
            "en": "Choose the language you want the bot to use."
        },
        "only_admin": {
            "en": "❌ Only server admins can change bot settings."
        }
    },

    # /autoroles command
    "autoroles": {
        "updated": {
            "en": "✅ Your rank role has been updated to **{role}**."
        },
        "removed_roles": {
            "en": "🧹 Removed old roles: {roles}"
        },
        "invisible_success": {
            "en": "👻 {count} rank roles removed. You are now anonymous in the leaderboard."
        },
        "no_account": {
            "en": "❌ No linked account found. Use /link add first."
        },
        "rank_not_found": {
            "en": "❌ No rank found."
        },
        "no_role_configured": {
            "en": "⚠️ No role configured for your rank `{rank}`."
        },
        "role_not_found": {
            "en": "❌ Configured role no longer exists."
        },
        "start_verification": {
            "en": "✉️ Start the verification using `/link add` and upload your screenshot."
        },
        "setup_instruction": {
            "en": "Choose a VALORANT tier, then a division, and link a role."
        },
        "user_panel_description": {
            "en": "Click **Add** to verify.\nUse **Update** to receive your current role.\n**Remove** deletes your linked account.\n**Invisibel** hides your rank role."
        },
        "message_created": {
            "en": "✅ Message created."
        },
        "rank_settings_title": {
            "en": "VALORANT Ranks"
        },
        "rank_settings_footer": {
            "en": "Select a tier to configure sub-divisions."
        },
        "not_configured": {
            "en": "Not configured"
        },
        "choose_division": {
            "en": "Choose a precise rank to assign a role:"
        },
        "choose_role": {
            "en": "Choose a Discord role for this rank:"
        }
    },

    # /link command
    "link": {
        "verification_started": {
            "en": "✉️ Verification started. Post the code in your party chat and upload a screenshot."
        },
        "verification_success": {
            "en": "✅ Successfully verified as `{tagline}`."
        },
        "verification_failed": {
            "en": "❌ Verification failed. Code or Tagline not found or expired."
        },
        "link_removed": {
            "en": "🗑️ Your linked account has been removed."
        },
        "no_link_found": {
            "en": "⚠️ No account linked to your Discord ID."
        },
        "linked_account_info": {
            "en": "Your Discord account is linked with: `{tagline}`"
        }
    }
}
