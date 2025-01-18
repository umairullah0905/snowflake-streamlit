import streamlit as st

conn = st.connection("my_connection", type="snowflake")
df = conn.query("SELECT * FROM mytable;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")