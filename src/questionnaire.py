# src/questionnaire.py

QUESTIONNAIRE = {
    "Bloc 1 — Habileté technique": {
        "Dimension 1.1 — Le contrôle": {
            1: "Contrôle fragile — Je perds souvent la balle au contrôle. Je ne suis pas à l’aise lors des déplacements de balle.",
            2: "Contrôle irrégulier — Je contrôle correctement dans des situations simples, il m’arrive encore de perdre la balle en situation de stress",
            3: "Contrôle fonctionnel — Je contrôle la balle de manière stable et sans effort. Et le positionnement de mes joueurs me permet de récupérer parfois des balles flottantes",
            4: "Maîtrise mécanique — Mon contrôle est fluide et propre. Je peux varier mes gestes sans perdre la balle. Mes mouvements sont économes. Mes joueurs à l’arrêt sont parfaitement positionnés pour récupérer parfois des balles flottantes",
            5: "Technique avancée — Je maîtrise différents types de contrôle (stop, rollover, tic-tac, séries). Ma technique reste stable même sous pression. Je rattrappe un bon pourcentage de balle flottante",
        },
        "Dimension 1.2 — La précision": {
            1: "Exécution aléatoire — Je joue à l’instinct. Je ne sais pas toujours où va la balle. J’ai un ou deux tirs efficaces à ma barre préférée, mais je ne comprends pas vraiment leur exécution.",
            2: "Précision fragile — J’ai un ou deux tirs dont je comprends le geste à ma barre préférée. Mais la régularité dépend beaucoup du flow ou du contexte.",
            3: "Précision fonctionnelle — Mon tir ou ma sortie principale est globalement fiable. Je sais où je vais jouer et je peux l’exécuter correctement. J’ai au moins deux tirs avec lesquels je suis très confortables sur ma barre préférée",
            4: "Précision stable — J’ai développé trois tirs à ma barre préférée. Je peux répéter mon arme principale avec constance, même sous pression modérée. Mes autres barres sont en développement",
            5: "Précision maîtrisée — Je suis capable d’être précise sur plusieurs barres. Je peux exécuter différentes options avec constance, même en fin de set",
        },
        "Dimension 1.3 — Transition et opportunisme": {
            1: "Réaction tardive — Je récupère la balle mais je ne sais pas quoi en faire. Je perds des opportunités évidentes.",
            2: "Opportunisme hésitant — Je vois certaines ouvertures. mais j’hésite ou je manque d’exécution rapide.",
            3: "Conversion fonctionnelle — Je suis capable de transformer une récupération propre en action offensive simple.",
            4: "Opportunisme actif — Je punis régulièrement les erreurs adverses. Je sais accélérer quand une fenêtre s’ouvre.",
            5: "Opportunisme stratégique — Je crée et exploite les micro-opportunités. Je contrôle les transitions (défense → 5 → 3) avec intention et rapidité.",
        },
    },

    "Bloc 2 — Intelligence stratégique": {
        "Dimension 2.1 — Stratégie par barre": {
            1: "Jeu non structuré — Je joue chaque barre sans plan clair. Je réagis au moment.",
            2: "Intention partielle — J’ai un plan sur ma barre préférée mais pas sur les autres.",
            3: "Plan fonctionnel — J’ai un plan simple sur ma 5 ou ma 3. Je sais comment je veux entrer ou finir un point.",
            4: "Plan structuré multi-barres — J’ai un plan clair sur plusieurs barres (entrée 5 → transition → finition). Je sais comment construire un point.",
            5: "Architecture stratégique complète — Chaque barre a une intention claire. Je relie défense, 5 et 3 dans un système cohérent. Je peux adapter cette architecture selon l’adversaire.",
        },
        "Dimension 2.2 — Intelligence de match": {
            1: "Absence d’analyse — Je joue sans vraiment analyser mon adversaire.",
            2: "Observation ponctuelle — Je remarque un ou deux éléments évidents (ex : tir fort, défaut de défense, tempo).",
            3: "Tactique — Je peux identifier plusieurs forces et faiblesses et adapter mes choix pour exploiter ces éléments.",
            4: "Stratégie — Je construis un plan de match cohérent et je peux orienter le jeu vers mes forces.",
            5: "Maîtrise stratégique dynamique — J’analyse rapidement mon adversaire et j’ajuste mon plan en cours de match en contrôlant le tempo et en maximisant les possessions de balle.",
        },
    },

    "Bloc 3 — Mental et communication": {
        "Dimension 3.1 — Gestion des émotions et discours intérieur en simple": {
            1: "Déséquilibre interne — Quand je fais une erreur, je m’en veux longtemps. Je peux perdre le fil d’un set et sortir de mon plan.",
            2: "Instabilité sous pression — Je tente de me ressaisir, mais les erreurs affectent mon rythme ou ma prise de décision.",
            3: "Régulation fonctionnelle — Je parviens généralement à me recentrer après une erreur. Je garde mon plan dans la plupart des situations.",
            4: "Stabilité stratégique — Je gère les moments clés (4-4, retard, avance). Je contrôle mon tempo et mon discours intérieur.",
            5: "Maîtrise compétitive — Je reste lucide et cohérente sous forte pression. Mon niveau technique et stratégique reste stable. Je transforme les moments critiques en opportunités.",
        },
        "Dimension 3.2 — Communication stratégique en double": {
            1: "Communication désorganisée — Il n’y a pas de plan clair. Les échanges sont confus, contradictoires ou inexistants.",
            2: "Communication minimale — On échange quelques informations simples, mais sans réelle coordination stratégique.",
            3: "Communication fonctionnelle — On définit un plan simple (ex : forcer un tir, couvrir un angle). Les calls sont clairs et utiles.",
            4: "Communication stratégique — On ajuste activement le plan en fonction de l’adversaire. Les échanges sont courts, précis et orientés performance.",
            5: "Communication intégrée — On fonctionne comme une unité stratégique. On anticipe les intentions de l’autre et on contrôle le tempo ensemble.",
        },
        "Dimension 3.3 — Gestion des émotions en double": {
            1: "Déséquilibre émotionnel — Je me fâche ou j’exprime des émotions négatives qui affectent le binôme.",
            2: "Instabilité sous pression — Je peux devenir tendue, silencieuse ou transmettre du stress.",
            3: "Régulation fonctionnelle — Je parviens généralement à me recentrer. Je ne laisse pas mes émotions nuire au jeu.",
            4: "Co-régulation constructive — Je stabilise mes émotions et j’aide mon/ma partenaire à rester stable.",
            5: "Leadership émotionnel — Je reste lucide sous pression et ma régulation renforce la cohésion du binôme.",
        },
    },

    "Bloc 4 — Culture d’apprentissage": {
        "Dimension 4.1 — Observation & Intégration": {
            1: "Je ne regarde peu ou pas de matchs.",
            2: "Je regarde des matchs pour le plaisir. Parfois j’observe certains joueurs dont j’aime le jeu.",
            3: "Je regarde des matchs pour le plaisir, et j’analyse les adversaires que je vais affronter en tournoi.",
            4: "Je regarde régulièrement certains joueurs. Je prends des notes et je classe différents types de jeu en catégories.",
            5: "Je comprends les styles de jeu. J’explore et j’intègre volontairement des éléments ou des systèmes d’autres joueurs dans mon propre jeu.",
        },
        "Dimension 4.2 — Structuration personnelle": {
            1: "Jeu spontané — Je joue principalement pour le plaisir et l’aspect social. Je ne me fixe pas d’objectif particulier.",
            2: "Progression par immersion — Je veux progresser. Je participe aux hebdos et aux majeurs en espérant monter naturellement en niveau. Je n’ai pas de plan structuré.",
            3: "Intention ciblée — Je me fixe des objectifs techniques précis (ex : développer une passe, stabiliser un tir). Je fais parfois des efforts ciblés pour travailler ces points.",
            4: "Plan régulier — J’ai un plan semi structuré qui mêle temps de pratique solo structuré (par jour ou par semaine) et participation à des tournois amicaux. Je surveille ma progression et je me fixe des objectifs de progression pour chaque grand tournoi",
            5: "Système orienté performance — J’ai un plan d’entraînement structuré et éprouvé avec des objectifs mesurables, souvent liés à une échéance. Ce plan prend en compte les aspects techniques et mentaux. Je suis mes progrès et j’ajuste mon plan en conséquence.",
        },
        "Dimension 4.3 — Feedback et mentorat": {
            1: "Distance au feedback — Je ne cherche pas activement de conseils ou je n’ose pas demander du feedback.",
            2: "Feedback reçu mais difficile à intégrer — Je reçois parfois des conseils et j’essaie de les appliquer. Je ne les comprends pas toujours car je ne maîtrise pas encore le vocabulaire. Certains me semblent contradictoires et j’ai du mal à savoir quand ils sont applicables à mon jeu ou à la situation.",
            3: "Ouverture structurée — Je demande des conseils ou des retours. Je comprends la plupart du vocabulaire utilisé. J’essaie d’appliquer les ajustements quand ils me semblent pertinents.",
            4: "Appui structurant — J’ai une ou plusieurs personnes de référence (coach, joueuse expérimentée, mentor informel). Je discute régulièrement stratégie et progression avec elles.",
            5: "Écosystème d’apprentissage intégré — J’ai un mentor, un coach ou un petit réseau de référence. Je sollicite du feedback ciblé. Je l’intègre dans mon plan d’entraînement et je cherche à comprendre en profondeur les ajustements proposés.",
        },
    },
}
