import streamlit as st
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib backend for compatibility
plt.switch_backend('agg')

st.title("Employee Engagement RFM Dashboard")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_excel('DEPLOYABLE.xlsx', engine='openpyxl')

# 🔧 Load data before using it
rfm = load_data()

# Show Data
if st.checkbox("Show RFM Data"):
    st.dataframe(rfm)

# Cluster Counts
st.subheader("Cluster Distribution")
if 'Cluster' in rfm.columns:
    cluster_counts = rfm['Cluster'].value_counts().sort_index()
    st.bar_chart(cluster_counts)
else:
    st.warning("No 'Cluster' column found in the dataset.")

# PCA Cluster Plot
st.subheader("Cluster Visualization")
if 'PCA1' in rfm.columns and 'PCA2' in rfm.columns:
    fig, ax = plt.subplots()
    sns.scatterplot(data=rfm, x='PCA1', y='PCA2', hue='Cluster', palette='Set2', s=80, ax=ax)
    st.pyplot(fig)
else:
    st.warning("PCA1 or PCA2 columns not found in the dataset.")


