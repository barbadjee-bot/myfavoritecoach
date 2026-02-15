# src/ui.py
import streamlit as st
import re
from src.radar import radar_chart
from src.analysis import qualitative_summary, v1_message
from src.analysis import qualitative_summary, v1_message, global_profile_analysis


def render_questionnaire(questionnaire: dict):
    """
    Affiche le questionnaire bloc par bloc, dimension par dimension.
    Pour chaque dimension, propose un choix de niveau 1–5 via radio vertical,
    avec la description affichée sur la même ligne (format_func).

    Retourne:
      - responses: dict[bloc][dimension] = score (int)
      - texts: dict[bloc][dimension] = texte associé au score
    """
    responses, texts = {}, {}

    for bloc, dims in questionnaire.items():
        st.subheader(bloc)
        responses[bloc], texts[bloc] = {}, {}

        for dim_name, levels in dims.items():
            # Petite vérification pour éviter un bug silencieux
            for lvl in range(1, 6):
                if lvl not in levels:
                    raise ValueError(f"Dimension '{dim_name}' du bloc '{bloc}' n'a pas le niveau {lvl}.")

            with st.expander(dim_name, expanded=False):
                options = [1, 2, 3, 4, 5]

                def format_option(x: int) -> str:
                    # Affiche le bouton + la description sur une même ligne
                    return f"{x} — {levels[x]}"

                score = st.radio(
                    label="Choisis ton niveau",
                    options=options,
                    index=2,  # par défaut: 3
                    format_func=format_option,
                    key=f"{bloc}:{dim_name}",
                )

                responses[bloc][dim_name] = score
                texts[bloc][dim_name] = levels[score]

    return responses, texts

import re



def abbreviate_dimension_name(dim_name: str, max_label_len: int = 22) -> str:
    """
    Transforme:
      "Dimension 1.2 — La précision"
    en:
      "1.2 Précision"
    et tronque si trop long.
    """
    s = dim_name.strip()

    # Capture "Dimension 1.2 — La précision"
    m = re.match(r"(?i)^dimension\s*([0-9]+\.[0-9]+)\s*[-—]\s*(.+)$", s)
    if m:
        code = m.group(1)
        title = m.group(2).strip()
    else:
        # Si pas au format "Dimension x.y — ..."
        code = ""
        title = s

    # Nettoie quelques articles fréquents
    title = re.sub(r"(?i)^(le|la|les|l’|l')\s+", "", title).strip()

    label = f"{code} {title}".strip() if code else title

    # Tronquer si trop long (radar lisible)
    if len(label) > max_label_len:
        label = label[: max_label_len - 1] + "…"
    return label


def flatten_scores_abbrev(responses: dict) -> dict:
    """
    Fusionne tous les scores en un dict plat, en abrégé.
    Exemple: {"1.1 Contrôle": 3, "2.2 Intelligence de match": 4, ...}
    """
    flat = {}
    for bloc, dims in responses.items():
        for dim_name, score in dims.items():
            flat[abbreviate_dimension_name(dim_name)] = score
    return flat


def render_results(responses: dict, texts: dict):
    """
    Affiche 1 radar par bloc + une interprétation qualitative par bloc.
    """
    st.divider()
    st.header("Résultats")

    st.subheader("Radar global — Toutes dimensions")
    all_scores = flatten_scores_abbrev(responses)
    st.plotly_chart(
    radar_chart("Global — Toutes dimensions", all_scores),
    use_container_width=True)
    
    st.markdown("### Analyse globale du profil")
    st.markdown(global_profile_analysis(all_scores))

    st.divider()

    for bloc, scores in responses.items():
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.plotly_chart(radar_chart(bloc, scores), use_container_width=True)

        with col2:
            strengths, develop, priorities = qualitative_summary(scores)

            st.markdown("### Interprétation qualitative")

            if strengths:
                st.markdown("**Points d’appui (≥4)**")
                for s in strengths:
                    st.write(f"✅ {s}")

            if develop:
                st.markdown("**En développement (=3)**")
                for d in develop:
                    st.write(f"🟡 {d}")

            if priorities:
                st.markdown("**Priorités (≤2)**")
                for p in priorities:
                    st.write(f"🎯 {p}")

            st.markdown("### Suggestion (V1)")
            st.write(v1_message(scores))

        st.divider()

        
