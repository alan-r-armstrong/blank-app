import streamlit as st
from datetime import datetime
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM MYTABLE;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}")