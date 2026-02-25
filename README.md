# Kiriaini Market: Spatial Data Dashboard
A lightweight Streamlit-based geospatial analytics dashboard for exploring parcel data within Kiriaini Market. This application provides interactive spatial visualization, parcel statistics, dynamic valuation, and exportable reports.
 
 **Overview**
The Kiriaini Market Analytics Dashboard enables users to:
Visualize parcel boundaries on an interactive map
Analyze parcel size distribution
Compute total market area
Estimate total market value based on a dynamic unit price
Filter parcels by size
Download filtered parcel reports

**Built using:**
Streamlit – Web application framework
Pandas – Data processing
Folium – Interactive mapping
streamlit-folium – Folium integration in Streamlit

 **Data Source**
The application loads parcel data from a local Parquet file:
Kiriaini_Parcels.parquet

**Expected fields:**
Column	Description
parcel_id	Unique parcel identifier
area_m2	Parcel area in square meters
geom	GeoJSON geometry (string format)

**Features**
1. Market Statistics (Sidebar)
Total number of parcels
Total market area (m²)
Average parcel size
2. Valuation Tool
User-defined Price per m² (KES)
Real-time calculation of total market value
3. Parcel Size Filter
Interactive slider to filter parcels by area
Map and export update dynamically
4. Interactive Parcel Explorer
GeoJSON parcel visualization
Hover tooltips displaying parcel ID
Zoomable and pannable Folium map
5. Export Functionality
Download filtered dataset as CSV
Geometry excluded for reporting purposes
6. Map Configuration
Center: [-0.6027211, 36.9512379]
Zoom Level: 15
Rendered using Folium and embedded in Streamlit

**Installation**
pip install streamlit pandas folium streamlit-folium pyarrow
Run the Application
streamlit run app.py
Ensure Kiriaini_Parcels.parquet is in the same directory as the application file.

**Use Cases**
Market spatial analysis
Land valuation estimation
Urban planning insights
Investment feasibility assessment
Parcel-level reporting

**License**
This project is intended for analytical and educational use. Modify and extend as needed.
Author: _Hari Spatial_
Built with: Streamlit & Folium
