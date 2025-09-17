import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_risk_gauge(risk_value):
    """
    Crée une jauge de risque interactive
    """
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
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

def create_timeline_chart(timeline_data):
    """
    Crée un graphique de timeline des événements
    """
    df = pd.DataFrame(timeline_data)
    
    # Mapper la sévérité à une couleur
    color_map = {
        "high": "red",
        "medium": "orange",
        "low": "green"
    }
    
    df["color"] = df["severity"].map(color_map)
    
    fig = px.scatter(
        df, 
        x="year", 
        y="event", 
        color="severity",
        color_discrete_map={"high": "red", "medium": "orange", "low": "green"},
        size=[10] * len(df),
        hover_name="event",
        hover_data={"year": True, "severity": True}
    )
    
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')))
    fig.update_layout(
        height=300,
        xaxis_title="Année",
        yaxis_title="Événements",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig