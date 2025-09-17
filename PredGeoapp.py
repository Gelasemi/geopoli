import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data.countries_data import COUNTRIES_DATA
from data.scenarios_data import SCENARIOS_DATA, CRITICAL_INDICATORS
from utils.predictor import predict_conflict_probability
from utils.visualizations import create_risk_gauge, create_timeline_chart

# Configuration de la page
st.set_page_config(
    page_title="Analyse Géopolitique Mondiale",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .profile-header {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .profile-image {
        border-radius: 50%;
        border: 3px solid #dee2e6;
    }
    .risk-badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 15px;
        color: white;
        font-weight: bold;
        font-size: 0.8rem;
    }
    .timeline-item {
        margin-bottom: 10px;
        padding-left: 20px;
        border-left: 2px solid #dee2e6;
    }
    .scenario-card {
        border-left: 5px solid;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
    }
    .scenario-high { border-left-color: #d32f2f; background-color: rgba(211, 47, 47, 0.1); }
    .scenario-medium { border-left-color: #ff9800; background-color: rgba(255, 152, 0, 0.1); }
    .scenario-low { border-left-color: #8bc34a; background-color: rgba(139, 195, 74, 0.1); }
</style>
""", unsafe_allow_html=True)

# En-tête avec profil
def display_profile():
    st.markdown("""
    <div class="profile-header">
        <div style="display: flex; align-items: center;">
            <img src="https://via.placeholder.com/120" class="profile-image" width="120" style="margin-right: 20px;">
            <div>
                <h1 style="margin-bottom: 5px;">Prince Manantenasoa Dauphin Gelase Michelot</h1>
                <p style="margin-bottom: 0; color: #6c757d; font-style: italic;">Membre de la communauté royale de Madagascar</p>
                <p style="margin-bottom: 0;">Expert en géopolitique et relations internationales</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Fonction principale
def main():
    display_profile()
    
    st.title("Analyse Géopolitique Mondiale Complète")
    st.markdown("### Cartographie des risques, conflits et soulèvements par pays, région et continent")
    
    # Sélection du continent
    continents = list(COUNTRIES_DATA.keys())
    selected_continent = st.selectbox("Sélectionner un continent", continents)
    
    # Sélection de la région
    regions = list(COUNTRIES_DATA[selected_continent].keys())
    selected_region = st.selectbox("Sélectionner une région", regions)
    
    # Sélection du pays
    countries = list(COUNTRIES_DATA[selected_continent][selected_region].keys())
    selected_country = st.selectbox("Sélectionner un pays", countries)
    
    # Afficher les détails du pays
    country_data = COUNTRIES_DATA[selected_continent][selected_region][selected_country]
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Jauge de risque
        risk_value = int(country_data["risk"].split("/")[0])
        fig = create_risk_gauge(risk_value)
        st.plotly_chart(fig, use_container_width=True)
        
        # Badge de risque
        risk_color = {
            0: "#28a745", 1: "#5cb85c", 2: "#8bc34a", 3: "#cddc39", 4: "#ffeb3b",
            5: "#ffc107", 6: "#ff9800", 7: "#ff5722", 8: "#f44336", 9: "#d32f2f", 10: "#b71c1c"
        }[risk_value]
        
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <span class="risk-badge" style="background-color: {risk_color};">
                {country_data["risk"]}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader(f"Analyse détaillée: {selected_country}")
        
        # Indicateurs critiques
        st.markdown("**Indicateurs critiques:**")
        for indicator in country_data["indicators"]:
            st.markdown(f"- {indicator}")
        
        # Timeline
        st.markdown("**Chronologie des événements:**")
        timeline_fig = create_timeline_chart(country_data["timeline"])
        st.plotly_chart(timeline_fig, use_container_width=True)
    
    # Section de prédiction
    st.markdown("---")
    st.header("Modèle de Prédiction des Conflits")
    
    # Calculer la probabilité de conflit
    probability = predict_conflict_probability(country_data)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Probabilité de conflit", f"{probability}%", delta=None)
        
        # Échelle de risque
        st.markdown("**Échelle de risque:**")
        risk_scale = pd.DataFrame({
            "Niveau": ["Stabilité", "Tensions", "Pré-crise", "Crise", "Conflit"],
            "Valeur": [0, 3, 5, 7, 10]
        })
        
        fig_risk_scale = px.bar(
            risk_scale, 
            x="Valeur", 
            y="Niveau", 
            orientation='h',
            color="Valeur", 
            color_continuous_scale=["green", "yellow", "red"],
            range_color=[0, 10],
            height=200
        )
        fig_risk_scale.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_risk_scale, use_container_width=True)
    
    with col2:
        # Indicateurs critiques cochés
        st.markdown("**Indicateurs critiques présents:**")
        for indicator in CRITICAL_INDICATORS:
            checked = indicator in country_data["indicators"]
            st.checkbox(indicator, value=checked, disabled=True)
    
    # Scénarios de prédiction
    st.markdown("---")
    st.header("Scénarios de Combinaison de Facteurs")
    
    for scenario in SCENARIOS_DATA:
        risk_class = "scenario-high" if scenario["probability"] >= 80 else ("scenario-medium" if scenario["probability"] >= 65 else "scenario-low")
        
        st.markdown(f"""
        <div class="{risk_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h5>{scenario['name']}</h5>
                <span class="risk-badge" style="background-color: {'#d32f2f' if scenario['probability'] >= 80 else '#ff9800' if scenario['probability'] >= 65 else '#8bc34a'};">
                    {scenario['probability']}%
                </span>
            </div>
            <p><strong>Facteurs:</strong> {scenario['factors']}</p>
            <p><strong>Événement probable:</strong> {scenario['event']}</p>
            <p><strong>Exemples historiques:</strong> {scenario['examples']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recommandations
    st.markdown("---")
    st.header("Recommandations pour les Dirigeants Politiques")
    
    recommendations = {
        "Prévention": [
            "Réformes institutionnelles: Limitation des mandats, indépendance judiciaire",
            "Transparence: Lutte anti-corruption, e-gouvernement",
            "Inclusion: Intégration des minorités, décentralisation",
            "Éducation: Programmes pour la jeunesse, réduction des inégalités",
            "Environnement: Gestion durable des ressources, adaptation climatique"
        ],
        "Intervention": [
            "Dialogue national: Processus inclusif avec toutes les parties",
            "Médiation internationale: ONU, UA, CEDEAO",
            "Gouvernance partagée: Gouvernements d'union nationale",
            "Réformes sécuritaires: Intégration des ex-combattants",
            "Aide économique: Soutien à la croissance, réduction de la dette"
        ],
        "Gestion de Crise": [
            "Opérations de paix: Mandats robustes de l'ONU",
            "Justice transitionnelle: CPI, tribunaux nationaux",
            "Aide humanitaire: Coordination internationale",
            "Reconstruction: Plans post-conflit, réconciliation",
            "Prévention des récurrences: Désarmement, réformes structurelles"
        ]
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### <span style='color:green'>Prévention</span>", unsafe_allow_html=True)
        for rec in recommendations["Prévention"]:
            st.markdown(f"- {rec}")
    
    with col2:
        st.markdown("#### <span style='color:orange'>Intervention</span>", unsafe_allow_html=True)
        for rec in recommendations["Intervention"]:
            st.markdown(f"- {rec}")
    
    with col3:
        st.markdown("#### <span style='color:red'>Gestion de Crise</span>", unsafe_allow_html=True)
        for rec in recommendations["Gestion de Crise"]:
            st.markdown(f"- {rec}")

if __name__ == "__main__":

    main()
