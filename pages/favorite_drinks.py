import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import hashlib
import subprocess
import base64

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")

schema_name = "ordering_app"
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@{DB_HOST}/{schema_name}")

# Set page configuration
st.set_page_config(page_title="Snacks & Desserts", layout="wide")

# Ensure user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please log in first!")
    st.stop()

# Retrieve username from session
username = st.session_state.get("username")

# Create layout
col1, col2 = st.columns([4, 1])

with col1:
    homepage_button = st.button("Go to Home Page", key="homepage_button", help="Redirecting to Home Page...")

    if homepage_button:
        st.switch_page("pages/homepage.py")

with col2:
    user_button = st.button("Go to User Details", key="user_button", help="Redirecting to user details...")

    if user_button:
        st.switch_page("pages/user_details.py")