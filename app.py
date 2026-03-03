import streamlit as st
import pandas as pd
import json
from streamlit_folium import st_folium
import folium

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Kiriaini Market Analytics", layout="wide")
st.title("📍 Kiriaini Market: Spatial Data Dashboard")

# 2. DATA FETCHING (Now from local file instead of PostgreSQL)
@st.cache_data
def get_data():
    # Load exported file instead of connecting to PostgreSQL
    df = pd.read_parquet("Kiriaini_Parcels.parquet")
    return df

df = get_data()

# 3. SIDEBAR STATISTICS (The "Value Add")
st.sidebar.header("Market Statistics")
total_area = df['area_m2'].sum()
avg_area = df['area_m2'].mean()

st.sidebar.metric("Total Parcels", len(df))
st.sidebar.metric("Total Market Area (m²)", f"{total_area:,.2f}")
st.sidebar.metric("Average Parcel Size", f"{avg_area:,.2f}")

# --- ADD THIS TO YOUR SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.header("💰 Valuation Tool")
unit_price = st.sidebar.number_input("Price per m² (KES)", min_value=0, value=5000)

# Calculate dynamic value
total_value = total_area * unit_price
st.sidebar.subheader(f"Total Market Value:")
st.sidebar.write(f"KES {total_value:,.2f}")

# --- ADD A FILTER TO THE MAIN PAGE ---
st.subheader("Filter by Size")
min_size, max_size = st.select_slider(
    "Select a range of parcel sizes (m²)",
    options=sorted(df['area_m2'].unique()),
    value=(df['area_m2'].min(), df['area_m2'].max())
)

# Logic: Filter the dataframe before showing the map
filtered_df = df[(df['area_m2'] >= min_size) & (df['area_m2'] <= max_size)]

# 4. INTERACTIVE MAP
st.subheader("Interactive Parcel Explorer")
m = folium.Map(location=[-0.6025998,36.9538168], zoom_start=16)

# Download button
csv_data = filtered_df.drop(columns=['geom']).to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Report",
    data=csv_data,
    file_name='Kiriaini_Filtered_Report.csv',
    mime='text/csv',
)

# Add GeoJSON to map (use filtered_df + safe JSON parsing)
for _, row in filtered_df.iterrows():
    geojson_feature = {
        "type": "Feature",
        "geometry": json.loads(row['geom']),
        "properties": {"id": row['parcel_id'], "area": row['area_m2']}
    }
    folium.GeoJson(
        geojson_feature,
        tooltip=f"ID: {row['parcel_id']}"
    ).add_to(m)

# Render the map in Streamlit
st_folium(m, width=1000, height=500)

