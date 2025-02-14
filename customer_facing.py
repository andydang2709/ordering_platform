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

# TODO: Initialize the app
st.title("Homestead Coffee Order")
st.sidebar.header("Options")