def predict_conflict_probability(country_data):
    """
    Calcule la probabilité de conflit pour un pays donné
    en fonction des indicateurs critiques présents.
    """
    # Mapping des indicateurs critiques à leur poids
    indicator_weights = {
        "Corruption >60/100 (Transparency International)": 15,
        "Pauvreté >40%": 12,
        "Présence de groupes armés actifs": 20,
        "Président au pouvoir >10 ans": 15,
        "Dépendance aux ressources >50% des exportations": 10,
        "Chômage jeunes >25%": 10,
        "Inflation >30%": 8,
        "Conflits ethniques/religieux historiques": 12,
        "Ingérence étrangère significative": 15,
        "Stress hydrique >40%": 8
    }
    
    # Calculer le score total
    total_score = 0
    max_score = 0
    
    for indicator in country_data["indicators"]:
        if indicator in indicator_weights:
            total_score += indicator_weights[indicator]
        max_score += max(indicator_weights.values())
    
    # Convertir en pourcentage
    probability = min(100, int((total_score / max_score) * 100))
    
    # Ajuster en fonction du risque actuel
    current_risk = int(country_data["risk"].split("/")[0])
    
    # Formule de pondération: 70% probabilité calculée + 30% risque actuel
    probability = int(0.7 * probability + 0.3 * current_risk * 10)
    
    return probability