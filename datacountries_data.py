```python
SCENARIOS_DATA = [
    {
        "name": "Triade Autoritaire",
        "probability": 92,
        "factors": "Président >10 ans + Corruption + Répression",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Égypte (2013), Zimbabwe (2017)"
    },
    {
        "name": "Crise Économique",
        "probability": 87,
        "factors": "Inflation >50% + Chômeurs jeunes >30%",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Venezuela (2014-2019), Tunisie (2011)"
    },
    {
        "name": "Fragmentation Ethnique",
        "probability": 78,
        "factors": "Conflits ethniques + Inégalités",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Rwanda (1994), Yougoslavie (1990s)"
    },
    {
        "name": "Insécurité Multiforme",
        "probability": 82,
        "factors": "Terrorisme + Criminalité organisée",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Somalie (1991-), Mexique (2006-)"
    },
    {
        "name": "Crise Environnementale",
        "probability": 65,
        "factors": "Sécheresse + Pénuries d'eau",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Syrie (2011-), Yémen (2015-)"
    },
    {
        "name": "Ingérence Étrangère",
        "probability": 75,
        "factors": "Troupes étrangères + Soutien à groupes armés",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Afghanistan (2001-2021), Ukraine (2014-)"
    },
    {
        "name": "Transition Démocratique",
        "probability": 70,
        "factors": "Institutions faibles + Corruption",
        "event": "Soulèvement populaire ou coup d'État militaire",
        "examples": "Exemples historiques: Tunisie (2011), Burkina Faso (2014)"
    }
]

CRITICAL_INDICATORS = [
    "Corruption >60/100 (Transparency International)",
    "Pauvreté >40%",
    "Présence de groupes armés actifs",
    "Président au pouvoir >10 ans",
    "Dépendance aux ressources >50% des exportations",
    "Chômage jeunes >25%",
    "Inflation >30%",
    "Conflits ethniques/religieux historiques",
    "Ingérence étrangère significative",
    "Stress hydrique >40%"
]
```

**Option B: Update Imports in `PredGeoapp.py`**
- If you prefer to keep `datacountries_data.py` and define `scenarios_data` inline or elsewhere, update the imports in `PredGeoapp.py` to match the file structure. For example, if you keep `datacountries_data.py` and add `scenarios_data.py`:

  ```python
  from data.datacountries_data import COUNTRIES_DATA
  from data.scenarios_data import SCENARIOS_DATA, CRITICAL_INDICATORS
  ```

**Recommended Action**: Go with **Option A** by renaming `datacountries_data.py` to `data/countries_data.py` and creating `data/scenarios_data.py` to align with the imports already in `PredGeoapp.py`. This minimizes changes to the main script.

#### 4. Update GitHub Actions Workflow
Your `.github_workflows_deploy.yml` specifies Python 3.10, but Streamlit Cloud is using Python 3.13.6, which caused the `distutils` issue with `numpy==1.24.3`. Update the workflow to use Python 3.13 to match the Streamlit Cloud environment, and add a step to upgrade pip.

Here’s the updated `.github/workflows/deploy.yml`:

<xaiArtifact artifact_id="f0dc830b-bc97-4d03-a306-a0b6ea3caac1" artifact_version_id="64470600-f183-4652-b311-445e064a9f2d" title="deploy.yml" contentType="text/yaml">
```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Deploy to Streamlit Cloud
      uses: streamlit/streamlit-app-action@v0.0.1
      with:
        app-name: geopolitical-predictor
        app-file: PredGeoapp.py
        app-dir: .
```
