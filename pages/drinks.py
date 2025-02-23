import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv


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

# TODO: pull this data from database
# TODO: add photo paths
drinks_data = {
    "Coffee": {
        "coffee_base_01": "Espresso",
        "coffee_base_02": "Vietnamese Coffee",
        "coffee_base_03": "Cold Brew"
    },
    "Tea": {
        "tea_base_01": "Earl Grey Tea", 
        "tea_base_02": "Green Tea", 
        "tea_base_03": "Peach & Flower Tea"
    },
    "Matcha": {
        "matcha_base_01": "Matcha", 
        "matcha_base_02": "Hojicha"}
}

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

# Custom CSS for Borders
st.markdown(
    """<style>
    .full-box {
        border: 3px solid #444;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        background-color: #f8f9fa;
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .category-title {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        color: black;
        margin-bottom: 15px;
    }
    .drink-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        padding: 15px;
    }
    .drink-container img {
        width: 150px;
        height: 150px;
        border-radius: 8px;
        object-fit: cover;
    }
    .drink-name {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>""",
    unsafe_allow_html=True
)

st.markdown("## Drink Base")

# ✅ Display Categories with Centered Buttons Inside the Box
for category, drinks in drinks_data.items():
    st.markdown(f"""<div class="full-box">
                    <div class="category-title">{category}</div>""", unsafe_allow_html=True)

    # Centered Buttons Row Inside Full Box
    button_cols = st.columns(len(drinks))  # Adjust dynamically based on number of drinks

    with st.container():
        for i, (drink_key, drink_name) in enumerate(drinks.items()):
            with button_cols[i]:  # Assign each button to a separate column, evenly spaced
                st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
                if st.button(drink_name, key=f"{category}_{drink_key}"):
                    st.switch_page(f"pages/{drink_key}.py")  # ✅ Correct page switching
                st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close full-box

st.markdown("<hr>", unsafe_allow_html=True)

# Navigation Bar at the Bottom
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("pages/homepage.py")

with col2:
    if st.button("🥤 Drinks"):
        st.switch_page("pages/drinks.py")

with col3:
    if st.button("🍩 Foods"):
        st.switch_page("pages/foods.py")

with col4:
    if st.button("🛒 Cart"):
        st.switch_page("pages/cart.py")