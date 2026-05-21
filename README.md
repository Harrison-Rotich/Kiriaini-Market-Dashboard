# Cloud-Native Spatial Analytics Engine
A lightweight Streamlit dashboard for real-time spatial analytics and parcel visualization in Kiriaini Market. The application streams geospatial parcel data directly from cloud storage using DuckDB, enabling fast serverless analysis, interactive mapping, valuation modeling, and parcel insights.

## Overview
The dashboard enables users to:
* Visualize parcel boundaries on an interactive Folium map
* Stream spatial data directly from cloud-hosted Parquet files
* Compute parcel statistics in real time
* Estimate market value using dynamic price inputs
* Explore parcel geometry with hover-based tooltips
* Run serverless spatial SQL queries using DuckDB

## Built With
* Streamlit — Interactive web application framework
* DuckDB — In-memory analytics and spatial SQL engine
* Folium — Interactive geospatial visualization
* streamlit-folium — Folium integration for Streamlit
* Pandas — Data processing and analytics

## Data Source
The application loads parcel data directly from a remote cloud-hosted Parquet file:
`kiriaini_parcels.parquet`

Expected fields:
| Column   | Description                   |
| -------- | ----------------------------- |
| id       | Unique parcel identifier      |
| geometry | Parcel geometry in WKB format |

## Core Features
### Cloud-Native Spatial Streaming
* Reads Parquet data directly from remote storage
* No local database required
* Fast columnar querying with DuckDB

### Spatial Analytics
* Automated parcel area computation
* Real-time market statistics
* Average and total parcel size metrics

### Dynamic Valuation Engine
* User-defined price per m² (KES)
* Instant total market value estimation

### Interactive Map Explorer
* GeoJSON parcel rendering
* Hover tooltips with parcel ID and area
* Zoomable and pannable Folium map

### Serverless Architecture
* Fully in-memory processing
* Spatial extensions enabled dynamically
* Lightweight deployment workflow

## Map Configuration
* Center: `[-0.6025998, 36.9538168]`
* Zoom Level: `17`
* Powered by Folium + Streamlit

## Installation
pip install streamlit pandas duckdb folium streamlit-folium pyarrow

## Run the Application
streamlit run app.py
Update the `CLOUD_PARQUET_URL` variable with your GitHub Raw or cloud storage Parquet URL before deployment.

## Use Cases
* Spatial market intelligence
* Land valuation analysis
* Cloud-native GIS prototyping
* Parcel-level spatial reporting
* Lightweight geospatial dashboards

## License
Intended for analytical, educational, and experimental geospatial applications.
**Author:** Hari Spatial
**Built with:** Streamlit, DuckDB & Folium
