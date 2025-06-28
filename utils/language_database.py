# utils/language_database.py

languages = {
    # Fehlermeldungen & allgemeine Hinweise
    "errors": {
        "no_account": {
            "en": "❌ No linked account found. Use /link add to verify your Riot ID.",
            "de": "❌ Kein verknüpfter Account gefunden. Verwende /link add zur Verifizierung."
        },
        "invalid_tagline": {
            "en": "❌ Invalid tagline format. Use Name#Tag.",
            "de": "❌ Ungültiges Tagline-Format. Verwende Name#Tag."
        },
        "api_down": {
            "en": "❌ API error. Please try again later.",
            "de": "❌ API-Fehler. Bitte versuche es später erneut."
        },
        "rate_limited": {
            "en": "⏳ Rate limit reached. Please wait a moment.",
            "de": "⏳ Anfragelimit erreicht. Bitte einen Moment warten."
        },
        "not_admin": {
            "en": "❌ You need to be an administrator to use this command.",
            "de": "❌ Du musst Administrator sein, um diesen Befehl zu nutzen."
        }
    },

    # /stats command
    "stats": {
        "title": {
            "en": "{tagline}'s Stats",
            "de": "Statistiken von {tagline}"
        },
        "rank": {
            "en": "Rank",
            "de": "Rang"
        },
        "mmr_change": {
            "en": "MMR Change",
            "de": "MMR-Veränderung"
        }
    },

    # /game command
    "game": {
        "title": {
            "en": "Recent Matches for {tagline}",
            "de": "Letzte Spiele von {tagline}"
        },
        "agent": {
            "en": "Agent",
            "de": "Agent"
        },
        "kda": {
            "en": "K/D/A",
            "de": "K/D/A"
        },
        "kd": {
            "en": "KD",
            "de": "KD"
        },
        "hs": {
            "en": "HS%",
            "de": "HS%"
        },
        "no_data": {
            "en": "❌ No match data found.",
            "de": "❌ Keine Spieldaten gefunden."
        }
    },

    # /leaderboard command
    "leaderboard": {
        "title": {
            "en": "Server Leaderboard",
            "de": "Server-Bestenliste"
        },
        "anonymous": {
            "en": "Anonymous",
            "de": "Anonym"
        },
        "not_enough_data": {
            "en": "❌ No leaderboard data available yet.",
            "de": "❌ Noch keine Leaderboard-Daten verfügbar."
        }
    },

    # /settings command
    "settings": {
        "language_updated": {
            "en": "✅ Language updated to English.",
            "de": "✅ Sprache wurde auf Deutsch gesetzt."
        },
        "choose_language": {
            "en": "Choose the language you want the bot to use.",
            "de": "Wähle die Sprache, die der Bot verwenden soll."
        },
        "only_admin": {
            "en": "❌ Only server admins can change bot settings.",
            "de": "❌ Nur Server-Admins können Bot-Einstellungen ändern."
        }
    },

    # /autoroles command
    "autoroles": {
        "updated": {
            "en": "✅ Your rank role has been updated to **{role}**.",
            "de": "✅ Deine Rang-Rolle wurde aktualisiert auf **{role}**."
        },
        "removed_roles": {
            "en": "🧹 Removed old roles: {roles}",
            "de": "🧹 Entfernte alte Rollen: {roles}"
        },
        "invisible_success": {
            "en": "👻 {count} rank roles removed. You are now anonymous in the leaderboard.",
            "de": "👻 {count} Rang-Rollen entfernt. Du erscheinst nun anonym im Leaderboard."
        },
        "no_account": {
            "en": "❌ No linked account found. Use /link add first.",
            "de": "❌ Kein verknüpfter Account gefunden. Verwende zuerst /link add."
        },
        "rank_not_found": {
            "en": "❌ No rank found.",
            "de": "❌ Kein Rang gefunden."
        },
        "no_role_configured": {
            "en": "⚠️ No role configured for your rank `{rank}`.",
            "de": "⚠️ Für deinen Rang `{rank}` wurde keine Rolle konfiguriert."
        },
        "role_not_found": {
            "en": "❌ Configured role no longer exists.",
            "de": "❌ Die konfigurierte Rolle existiert nicht mehr."
        },
        "start_verification": {
            "en": "✉️ Start the verification using `/link add` and upload your screenshot.",
            "de": "✉️ Starte die Verifizierung mit `/link add` und lade deinen Screenshot hoch."
        },
        "setup_instruction": {
            "en": "Choose a VALORANT tier, then a division, and link a role.",
            "de": "Wähle ein VALORANT Tier, dann eine Division, und verknüpfe eine Rolle."
        },
        "user_panel_description": {
            "en": "Click **Add** to verify.\nUse **Update** to receive your current role.\n**Remove** deletes your linked account.\n**Invisibel** hides your rank role.",
            "de": "Klicke auf **Add**, um dich zu verifizieren.\nMit **Update** kannst du deine aktuelle Rolle erhalten.\n**Remove** löscht deinen verknüpften Account.\n**Invisibel** entfernt deine Rang-Rolle."
        },
        "message_created": {
            "en": "✅ Message created.",
            "de": "✅ Nachricht erstellt."
        },
        "rank_settings_title": {
            "en": "VALORANT Ranks",
            "de": "VALORANT Ränge"
        },
        "rank_settings_footer": {
            "en": "Select a tier to configure sub-divisions.",
            "de": "Wähle ein Tier aus, um Unterstufen zu konfigurieren."
        },
        "not_configured": {
            "en": "Not configured",
            "de": "Nicht konfiguriert"
        },
        "choose_division": {
            "en": "Choose a precise rank to assign a role:",
            "de": "Wähle einen genauen Rang, um eine Rolle zuzuweisen:"
        },
        "choose_role": {
            "en": "Choose a Discord role for this rank:",
            "de": "Wähle eine Discord-Rolle für diesen Rang:"
        }
    },

    # /link command
    "link": {
        "verification_started": {
            "en": "✉️ Verification started. Post the code in your party chat and upload a screenshot.",
            "de": "✉️ Verifizierung gestartet. Poste den Code in deinen Party-Chat und lade einen Screenshot hoch."
        },
        "verification_success": {
            "en": "✅ Successfully verified as `{tagline}`.",
            "de": "✅ Erfolgreich verifiziert als `{tagline}`."
        },
        "verification_failed": {
            "en": "❌ Verification failed. Code or Tagline not found or expired.",
            "de": "❌ Verifizierung fehlgeschlagen. Code oder Tagline nicht gefunden oder abgelaufen."
        },
        "link_removed": {
            "en": "🗑️ Your linked account has been removed.",
            "de": "🗑️ Dein verknüpfter Account wurde entfernt."
        },
        "no_link_found": {
            "en": "⚠️ No account linked to your Discord ID.",
            "de": "⚠️ Kein Account mit deinem Discord-Account verknüpft."
        },
        "linked_account_info": {
            "en": "Your Discord account is linked with: `{tagline}`",
            "de": "Dein Discord-Account ist verknüpft mit: `{tagline}`"
        }
    }
}
