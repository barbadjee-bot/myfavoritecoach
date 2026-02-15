def qualitative_summary(scores: dict):
    strengths = [k for k, v in scores.items() if v >= 4]
    develop = [k for k, v in scores.items() if v == 3]
    priorities = [k for k, v in scores.items() if v <= 2]
    return strengths, develop, priorities

def v1_message(scores: dict) -> str:
    _, _, priorities = qualitative_summary(scores)
    if priorities:
        return "Concentre-toi sur 1 seule priorité pendant 2–4 semaines, puis refais le test."
    return "Profil équilibré : choisis un axe pour passer de 3→4."

def global_profile_analysis(flat_scores: dict) -> str:
    """
    Produit une analyse qualitative globale à partir d'un dict plat:
    {"1.1 Contrôle": 3, "2.2 Match": 4, ...}
    Renvoie un texte court (markdown) à afficher sous le radar global.
    """
    if not flat_scores:
        return "Aucun score disponible."

    # Stats simples
    values = list(flat_scores.values())
    avg = sum(values) / len(values)

    strengths = [k for k, v in flat_scores.items() if v >= 4]
    develop = [k for k, v in flat_scores.items() if v == 3]
    priorities = [k for k, v in flat_scores.items() if v <= 2]

    # Top 3 forces / priorités (par score puis alpha)
    strengths_sorted = sorted(strengths, key=lambda k: (-flat_scores[k], k))[:3]
    priorities_sorted = sorted(priorities, key=lambda k: (flat_scores[k], k))[:2]

    # "Signature" du profil selon la moyenne (volontairement doux, non jugeant)
    if avg >= 4.2:
        signature = "Profil très solide et déjà orienté performance."
    elif avg >= 3.6:
        signature = "Profil solide avec plusieurs points d’appui."
    elif avg >= 3.0:
        signature = "Profil en construction, avec une base déjà fonctionnelle."
    else:
        signature = "Profil en phase d’exploration : beaucoup de leviers rapides."

    # Construction du message
    lines = []
    lines.append(f"**Lecture globale :** {signature}")
    lines.append(f"**Niveau moyen (indicatif) :** {avg:.1f}/5")

    if strengths_sorted:
        lines.append("**Points d’appui :** " + ", ".join(f"**{s}**" for s in strengths_sorted) + ".")
    elif develop:
        lines.append("**Point d’appui actuel :** tu as plusieurs compétences **fonctionnelles (niveau 3)**.")

    if priorities_sorted:
        lines.append("**Levier prioritaire :** " + ", ".join(f"**{p}**" for p in priorities_sorted) + ".")
        lines.append("**Conseil V1 :** choisis **1 seul** levier pendant 2–4 semaines, puis refais le test.")
    else:
        # Si pas de ≤2, propose une montée 3→4
        if develop:
            target = develop[0]
            lines.append(f"**Levier pour passer un cap :** vise **{target}** pour passer de 3→4.")
        lines.append("**Conseil V1 :** consolide la régularité et mesure tes progrès (même de façon simple).")

    return "\n\n".join(lines)
