import streamlit as st

# Set page configuration to wide and hide sidebar
st.set_page_config(layout="wide")
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        .block-container {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Layout: 2 columns, left for poster, right for buttons
col1, col2 = st.columns([2, 1])  # Adjust ratio as needed

with col1:
    st.image("your_poster.jpg", use_column_width=True, caption="Event Poster")  # Replace with your poster path

with col2:
    st.markdown(
        """
        <div style='display: flex; flex-direction: column; justify-content: center; height: 100vh;'>
            <button style='
                background-color: #22223b;
                color: #f2e9e4;
                padding: 1rem 2rem;
                border: none;
                border-radius: 8px;
                font-size: 1.2rem;
                margin-bottom: 1.5rem;
                cursor: pointer;
                transition: background 0.3s;
            ' onclick="window.location.href='#'">Early Bird</button>
            <button style='
                background-color: #4a4e69;
                color: #f2e9e4;
                padding: 1rem 2rem;
                border: none;
                border-radius: 8px;
                font-size: 1.2rem;
                cursor: pointer;
                transition: background 0.3s;
            ' onclick="window.location.href='#'">Couple Entry</button>
        </div>
        """,
        unsafe_allow_html=True
    )
