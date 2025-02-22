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

if __name__ == "__main__":
    login()