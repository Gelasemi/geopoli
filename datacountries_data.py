# Structure des données des pays extraite du HTML
COUNTRIES_DATA = {
    "Afrique": {
        "Afrique du Nord": {
            "Algérie": {
                "risk": "6/10",
                "indicators": [
                    "Autoritarisme",
                    "Crise économique",
                    "Chômage jeunes"
                ],
                "timeline": [
                    {"year": "1954-1962", "event": "Guerre d'indépendance", "severity": "high"},
                    {"year": "1991-2002", "event": "Guerre civile", "severity": "high"},
                    {"year": "2019-2021", "event": "Hirak (mouvement de contestation)", "severity": "medium"},
                    {"year": "2024-2025", "event": "Manifestations contre l'austérité", "severity": "medium"}
                ]
            },
            "Égypte": {
                "risk": "8/10",
                "indicators": [
                    "Autoritarisme",
                    "Crise économique",
                    "Répression"
                ],
                "timeline": [
                    {"year": "1952", "event": "Coup d'État militaire", "severity": "high"},
                    {"year": "2011", "event": "Révolution égyptienne", "severity": "high"},
                    {"year": "2013", "event": "Coup d'État de Sissi", "severity": "high"},
                    {"year": "2024-2025", "event": "Crise économique et pénuries alimentaires", "severity": "high"}
                ]
            },
            # Ajouter d'autres pays d'Afrique du Nord...
        },
        "Afrique de l'Ouest": {
            "Burkina Faso": {
                "risk": "10/10",
                "indicators": [
                    "Jihadisme",
                    "Coups d'État",
                    "Pauvreté"
                ],
                "timeline": [
                    {"year": "2014", "event": "Soulèvement populaire", "severity": "high"},
                    {"year": "2022", "event": "Premier coup d'État", "severity": "high"},
                    {"year": "2023", "event": "Deuxième coup d'État", "severity": "high"},
                    {"year": "2024-2025", "event": "Escalade des attaques jihadistes", "severity": "high"}
                ]
            },
            # Ajouter d'autres pays d'Afrique de l'Ouest...
        },
        # Ajouter d'autres régions d'Afrique...
    },
    "Amériques": {
        "Amérique du Nord": {
            "USA": {
                "risk": "8/10",
                "indicators": [
                    "Polarisation politique",
                    "Violence politique",
                    "Inégalités"
                ],
                "timeline": [
                    {"year": "1954-1968", "event": "Mouvement des droits civiques", "severity": "medium"},
                    {"year": "1992", "event": "Émeutes de Los Angeles", "severity": "medium"},
                    {"year": "2021", "event": "Assaut du Capitole", "severity": "high"},
                    {"year": "2024-2025", "event": "Violences politiques autour des élections", "severity": "high"}
                ]
            },
            # Ajouter d'autres pays d'Amérique du Nord...
        },
        # Ajouter d'autres régions des Amériques...
    },
    # Ajouter d'autres continents...
}