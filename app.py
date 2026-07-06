import streamlit as st

from views import (
    home,
    upload,
    profile_data,
    cleaning,
    dashboard,
    insights,
    forecast,
    settings
)

st.set_page_config(
    page_title="Neurolytics",
    page_icon="🧠",
    layout="wide"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Upload Dataset",
        "Profile Dataset",
        "Data Cleaning",
        "Dashboard",
        "AI Insights",
        "Forecast",
        "Settings"
    ]
)

if menu == "Home":
    home.show()

elif menu == "Upload Dataset":
    upload.show()

elif menu == "Profile Dataset":
    profile_data.show()

elif menu == "Data Cleaning":
    cleaning.show()

elif menu == "Dashboard":
    dashboard.show()

elif menu == "AI Insights":
    insights.show()

elif menu == "Forecast":
    forecast.show()

else:
    settings.show()