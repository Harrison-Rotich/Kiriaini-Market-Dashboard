
import streamlit as st
import pandas as pd
import duckdb
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(page_title="Cloud-Native LIMS Dashboard", layout="wide")
st.title("🌐 Cloud-Native Spatial Analytics Engine")

# 1. DIRECT REMOTE CLOUD STORAGE URL
# Replace this with your actual GitHub Raw token link
CLOUD_PARQUET_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/kiriaini-market-dashboard/main/kiriaini_parcels.parquet"

# 2. STREAMING DATA VIA DUCKDB
@st.cache_data
def stream_cloud_data():
    # Initialize a clean, fast in-memory DuckDB connection
    db = duckdb.connect()
    db.execute("INSTALL spatial; LOAD spatial;") # Enable spatial engine
    db.execute("INSTALL httpfs; LOAD httpfs;")   # Enable remote file streaming
    
    # Run high-speed columnar spatial SQL query directly on the internet URL
    query = f"""
        SELECT 
            id as parcel_id, 
            ST_Area(ST_GeomFromWKB(geometry)) * 111000 * 111000 as area_m2, -- Rough degree to meter conversion for stats
            ST_AsGeoJSON(ST_GeomFromWKB(geometry)) as geom
        FROM read_parquet('{CLOUD_PARQUET_URL}')
    """
    df = db.execute(query).df()
    db.close()
    return df

try:
    df = stream_cloud_data()

    # 3. SIDEBAR ANALYTICS
    st.sidebar.header("📊 Market Statistics")
    total_area = df['area_m2'].sum()
    avg_area = df['area_m2'].mean()

    st.sidebar.metric("Total Automated Parcels", len(df))
    st.sidebar.metric("Total Area (m²)", f"{total_area:,.2f}")
    st.sidebar.metric("Avg Size (m²)", f"{avg_area:,.2f}")

    # Dynamic Valuation Input
    unit_price = st.sidebar.number_input("Price per m² (KES)", min_value=0, value=5000)
    st.sidebar.metric("Total Market Value", f"KES {total_area * unit_price:,.2f}")

    # 4. MAP VISUALIZATION
    st.subheader("📍 Live Serverless Map View")
    m = folium.Map(location=[-0.6025998054452301, 36.95381681317332], zoom_start=17)

    for _, row in df.iterrows():
        geojson_feature = {
            "type": "Feature",
            "geometry": json.loads(row['geom']),
            "properties": {"id": row['parcel_id'], "area": round(row['area_m2'], 2)}
        }
        folium.GeoJson(
            geojson_feature, 
            tooltip=f"Parcel: {row['parcel_id']}<br>Area: {round(row['area_m2'], 2)} m²"
        ).add_to(m)

    st_folium(m, width=1000, height=500)

except Exception as e:
    st.error(f"Cloud Connection Blocked: {e}")
