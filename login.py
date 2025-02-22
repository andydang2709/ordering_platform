# TODO: Import necessary packages
# pip install django streamlit numpy pandas matplotlib seaborn scikit-learn sqlalchemy python-dotenv cryptography pymysql
# source .venv/bin/activate
# streamlit run customer_facing.py

###### NOTE: this is how you run a query in Python ######
#   query = "INSERT INTO transactions (date, detail, amount, account, category, belongs_to) VALUES (%s, %s, %s, %s, %s, %s)"
#    with engine.connect() as conn:
#        conn.execute(query, (date, detail, amount, account, category, belongs_to))

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


## TODO: Define all classes

## TODO: Accessing the database
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")

schema_name = "ordering_app"
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@{DB_HOST}/{schema_name}")

## TODO: make login function

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both username and password.")
            return
        
        hashed_password = hash_password(password)

        try:
                with engine.connect() as conn:
                    query = text("SELECT password FROM customers WHERE user_id = :username")
                    result = conn.execute(query, {"username": username}).fetchone()

                    if result and result[0] == hashed_password:
                        st.success(f"Welcome, {username}!")
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                    else:
                        st.error("Invalid username or password.")
        except Exception as e:
            st.error(f"Database error: {e}")    

    # if st.button("Register"):
    #     subprocess.run(["streamlit", "run", "register.py"])


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
                    "user_name": new_username 
                })

                st.success("Registration successful! You can now log in.")

        except Exception as e:
            st.error(f"Database error: {e}")

tab1, tab2 = st.tabs(["Login", "Create a New Account"])

with tab1:
    login()

with tab2:
    register()