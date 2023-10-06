import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
st.set_option('deprecation.showPyplotGlobalUse', False)

# Chargement du fichier Shapefile avec GeoPandas
@st.cache_data
def load_shapefile(shapefile_path):
    return gpd.read_file(shapefile_path)

shapefile_path = "gadm36_SEN_1.shx"
gdf = load_shapefile(shapefile_path)

# Liste des arrondissements uniques dans le jeu de données de Thies
#thies_arrondissements = gdf[gdf['NAME_1'] == 'Thiès']['NAME_3'].unique()
st.write(gdf) 
