import subprocess
import sys
import importlib
import streamlit as st

def install_and_import(package_name):
    """Installe un package s'il n'est pas disponible et l'importe"""
    try:
        return importlib.import_module(package_name)
    except ImportError:
        print(f"Installation de {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return importlib.import_module(package_name)

# Installer et importer les dépendances nécessaires
px = install_and_import("plotly.express")
go = install_and_import("plotly.graph_objects")
pd = install_and_import("pandas")
np = install_and_import("numpy")

# Configuration de la page
st.set_page_config(
    page_title="Analyse Géopolitique Mondiale",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# En-tête avec profil
st.markdown("""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
    <div style="display: flex; align-items: center;">
        <img src="https://via.placeholder.com/120" style="border-radius: 50%; border: 3px solid #dee2e6; margin-right: 20px;" width="120">
        <div>
            <h1 style="margin-bottom: 5px;">Prince Manantenasoa Dauphin Gelase Michelot</h1>
            <p style="margin-bottom: 0; color: #6c757d; font-style: italic;">Membre de la communauté royale de Madagascar</p>
            <p style="margin-bottom: 0;">Expert en géopolitique et relations internationales</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("Analyse Géopolitique Mondiale Complète")
st.markdown("### Cartographie des risques, conflits et soulèvements par pays, région et continent")

# Données des pays (exemple simplifié)
countries_data = {
    "Afrique": {
        "Afrique du Nord": {
            "Algérie": {"risk": "6/10", "indicators": ["Autoritarisme", "Crise économique"]},
            "Égypte": {"risk": "8/10", "indicators": ["Autoritarisme", "Répression"]},
            "Libye": {"risk": "10/10", "indicators": ["Effondrement de l'État", "Guerre civile"]},
            "Maroc": {"risk": "4/10", "indicators": ["Autoritarisme", "Inégalités"]},
            "Tunisie": {"risk": "7/10", "indicators": ["Crise économique", "Instabilité"]},
            "Soudan": {"risk": "10/10", "indicators": ["Guerre civile", "Répression"]}
        },
        "Afrique de l'Ouest": {
            "Burkina Faso": {"risk": "10/10", "indicators": ["Jihadisme", "Coups d'État"]},
            "Mali": {"risk": "10/10", "indicators": ["Jihadisme", "Coups d'État"]},
            "Niger": {"risk": "10/10", "indicators": ["Coup d'État", "Insécurité"]},
            "Nigeria": {"risk": "9/10", "indicators": ["Terrorisme", "Conflits ethniques"]},
            "Côte d'Ivoire": {"risk": "5/10", "indicators": ["Tensions politiques", "Inégalités"]}
        }
    },
    "Amériques": {
        "Amérique du Nord": {
            "USA": {"risk": "8/10", "indicators": ["Polarisation politique", "Violence politique"]},
            "Canada": {"risk": "2/10", "indicators": ["Tensions identitaires"]},
            "Mexique": {"risk": "9/10", "indicators": ["Criminalité organisée", "Corruption"]}
        }
    },
    "Asie": {
        "Asie de l'Est": {
            "Chine": {"risk": "7/10", "indicators": ["Autoritarisme", "Tensions ethniques"]},
            "Corée du Nord": {"risk": "9/10", "indicators": ["Dictature totalitaire", "Nucléaire"]},
            "Japon": {"risk": "3/10", "indicators": ["Vieillissement démographique"]},
            "Taïwan": {"risk": "9/10", "indicators": ["Menace d'invasion chinoise"]}
        }
    },
    "Europe": {
        "Europe de l'Est": {
            "Ukraine": {"risk": "10/10", "indicators": ["Invasion russe", "Guerre"]},
            "Russie": {"risk": "9/10", "indicators": ["Autoritarisme", "Guerre en Ukraine"]},
            "Biélorussie": {"risk": "8/10", "indicators": ["Autoritarisme", "Dépendance russe"]}
        }
    },
    "Océanie": {
        "Australasie": {
            "Australie": {"risk": "2/10", "indicators": ["Tensions raciales"]},
            "Nouvelle-Zélande": {"risk": "1/10", "indicators": ["Stabilité relative"]}
        }
    }
}

# Scénarios de prédiction
scenarios_data = [
    {"name": "Triade Autoritaire", "probability": 92, "factors": "Président >10 ans + Corruption + Répression"},
    {"name": "Crise Économique", "probability": 87, "factors": "Inflation >50% + Chômage jeunes >30%"},
    {"name": "Fragmentation Ethnique", "probability": 78, "factors": "Conflits ethniques + Inégalités"},
    {"name": "Insécurité Multiforme", "probability": 82, "factors": "Terrorisme + Criminalité organisée"},
    {"name": "Crise Environnementale", "probability": 65, "factors": "Sécheresse + Pénuries d'eau"},
    {"name": "Ingérence Étrangère", "probability": 75, "factors": "Troupes étrangères + Soutien à groupes armés"},
    {"name": "Transition Démocratique", "probability": 70, "factors": "Institutions faibles + Corruption"}
]

# Fonction pour calculer la probabilité de conflit
def predict_conflict_probability(indicators):
    critical_indicators = [
        "Corruption", "Autoritarisme", "Répression", "Guerre civile", "Terrorisme",
        "Pauvreté", "Inégalités", "Instabilité", "Effondrement de l'État",
        "Violence politique", "Criminalité organisée", "Coups d'État",
        "Tensions ethniques", "Conflits religieux", "Crise économique",
        "Chômage jeunes", "Inflation", "Dépendance aux ressources",
        "Stress hydrique", "Changement climatique"
    ]
    
    score = sum(1 for indicator in indicators if any(critical in indicator for critical in critical_indicators))
    max_score = len(indicators)
    probability = min(100, int((score / max_score) * 100))
    
    return probability

# Interface utilisateur
st.header("Modèle de Prédiction des Conflits")

# Sélection du continent
continent = st.selectbox("Sélectionner un continent", list(countries_data.keys()))

# Sélection de la région
region = st.selectbox("Sélectionner une région", list(countries_data[continent].keys()))

# Sélection du pays
country = st.selectbox("Sélectionner un pays", list(countries_data[continent][region].keys()))

# Afficher les détails du pays
country_data = countries_data[continent][region][country]

col1, col2 = st.columns([1, 3])

with col1:
    # Jauge de risque
    risk_value = int(country_data["risk"].split("/")[0])
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risque Actuel"},
        gauge={
            'axis': {'range': [None, 10]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 2], 'color': "lightgreen"},
                {'range': [2, 4], 'color': "green"},
                {'range': [4, 6], 'color': "yellow"},
                {'range': [6, 8], 'color': "orange"},
                {'range': [8, 10], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': risk_value
            }
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Badge de risque
    risk_colors = {
        0: "#28a745", 1: "#5cb85c", 2: "#8bc34a", 3: "#cddc39", 4: "#ffeb3b",
        5: "#ffc107", 6: "#ff9800", 7: "#ff5722", 8: "#f44336", 9: "#d32f2f", 10: "#b71c1c"
    }
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <span style="background-color: {risk_colors[risk_value]}; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; font-size: 0.8rem;">
            {country_data["risk"]}
        </span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader(f"Analyse détaillée: {country}")
    
    # Indicateurs critiques
    st.markdown("**Indicateurs critiques:**")
    for indicator in country_data["indicators"]:
        st.markdown(f"- {indicator}")
    
    # Calculer la probabilité de conflit
    probability = predict_conflict_probability(country_data["indicators"])
    st.metric("Probabilité de conflit", f"{probability}%", delta=None)

# Scénarios de prédiction
st.markdown("---")
st.header("Scénarios de Combinaison de Facteurs")

for scenario in scenarios_data:
    risk_class = "scenario-high" if scenario["probability"] >= 80 else ("scenario-medium" if scenario["probability"] >= 65 else "scenario-low")
    bg_color = "#d32f2f" if scenario["probability"] >= 80 else ("#ff9800" if scenario["probability"] >= 65 else "#8bc34a")
    
    st.markdown(f"""
    <div style="border-left: 5px solid {bg_color}; padding: 15px; margin-bottom: 15px; border-radius: 5px; background-color: rgba(211, 47, 47, 0.1) if {scenario['probability'] >= 80 else rgba(255, 152, 0, 0.1) if {scenario['probability'] >= 65 else rgba(139, 195, 74, 0.1)}">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h5>{scenario['name']}</h5>
            <span style="background-color: {bg_color}; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; font-size: 0.8rem;">
                {scenario['probability']}%
            </span>
        </div>
        <p><strong>Facteurs:</strong> {scenario['factors']}</p>
        <p><strong>Événement probable:</strong> Soulèvement populaire ou coup d'État militaire</p>
    </div>
    """, unsafe_allow_html=True)

# Recommandations
st.markdown("---")
st.header("Recommandations pour les Dirigeants Politiques")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### <span style='color:green'>Prévention</span>", unsafe_allow_html=True)
    st.markdown("- **Réformes institutionnelles**: Limitation des mandats, indépendance judiciaire")
    st.markdown("- **Transparence**: Lutte anti-corruption, e-gouvernement")
    st.markdown("- **Inclusion**: Intégration des minorités, décentralisation")
    st.markdown("- **Éducation**: Programmes pour la jeunesse")
    st.markdown("- **Environnement**: Gestion durable des ressources")

with col2:
    st.markdown("#### <span style='color:orange'>Intervention</span>", unsafe_allow_html=True)
    st.markdown("- **Dialogue national**: Processus inclusif")
    st.markdown("- **Médiation internationale**: ONU, UA, CEDEAO")
    st.markdown("- **Gouvernance partagée**: Gouvernements d'union")
    st.markdown("- **Réformes sécuritaires**: Intégration des ex-combattants")
    st.markdown("- **Aide économique**: Soutien à la croissance")

with col3:
    st.markdown("#### <span style='color:red'>Gestion de Crise</span>", unsafe_allow_html=True)
    st.markdown("- **Opérations de paix**: Mandats robustes de l'ONU")
    st.markdown("- **Justice transitionnelle**: CPI, tribunaux")
    st.markdown("- **Aide humanitaire**: Coordination internationale")
    st.markdown("- **Reconstruction**: Plans post-conflit")
    st.markdown("- **Prévention des récurrences**: Désarmement")
