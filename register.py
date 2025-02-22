import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")

schema_name = "ordering_app"
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@{DB_HOST}/{schema_name}")

def register():
    st.title("Register New Account")

    new_username = st.text_input("Choose a Username", key="reg_username")
    new_password = st.text_input("Choose a Password", type="password", key="reg_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

    if st.button("Register"):
        if not new_username or not new_password or not confirm_password:
            st.error("All fields are required.")
            return
        
        if new_password != confirm_password:
            st.error("Passwords do not match.")
            return

        hashed_password = hash_password(new_password)

        try:
            with engine.connect() as conn:
                # Check if username already exists
                check_query = text("SELECT user_id FROM customers WHERE user_id = :username")
                existing_user = conn.execute(check_query, {"username": new_username}).fetchone()

                if existing_user:
                    st.error("Username already exists. Please choose another.")
                    return

                # Insert new user
                insert_query = text("""
                    INSERT INTO customers (user_id, password, user_name, favorites, last_visit)
                    VALUES (:username, :password, :user_name, NULL, CURDATE())
                """)
                conn.execute(insert_query, {
                    "username": new_username,
                    "password": hashed_password,
                    "user_name": new_username  # Can be modified to allow full name input
                })

                st.success("Registration successful! You can now log in.")

                # Add a button to go back to login
                if st.button("Go to Login"):
                    subprocess.run(["streamlit", "run", "login.py"])  # Opens login.py in a new process

        except Exception as e:
            st.error(f"Database error: {e}")

if __name__ == "__main__":
    register()