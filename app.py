import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# Simulate data
def generate_data():
    data = []
    now = datetime.now()
    for i in range(10):
        time = now - timedelta(minutes=30*i)
        pH = round(random.uniform(6.5, 8.5), 2)
        turbidity = round(random.uniform(10, 50), 2)
        data.append([time.strftime("%Y-%m-%d %H:%M"), pH, turbidity])
    return pd.DataFrame(data, columns=["Timestamp", "pH", "Turbidity"])

df = generate_data()

# Display
st.title("Smart Buoy Water Monitoring")
st.line_chart(df.set_index("Timestamp"))
st.dataframe(df)