# TODO: Import necessary packages
# pip install django streamlit numpy pandas matplotlib seaborn scikit-learn sqlalchemy python-dotenv cryptography
# source .venv/bin/activate
# streamlit run customer_facing.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

## TODO: Define all classes

# Accessing the database
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")

schema_name = "ordering_app"
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@{DB_HOST}/{schema_name}")

###### NOTE: this is how you run a query in Python ######
#   query = "INSERT INTO transactions (date, detail, amount, account, category, belongs_to) VALUES (%s, %s, %s, %s, %s, %s)"
#    with engine.connect() as conn:
#        conn.execute(query, (date, detail, amount, account, category, belongs_to))

