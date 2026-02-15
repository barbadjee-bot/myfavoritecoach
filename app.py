import streamlit as st
from src.questionnaire import QUESTIONNAIRE
from src.ui import render_questionnaire, render_results

st.set_page_config(page_title="myFavCoach", layout="wide")
st.title("myFavCoach — V1")

responses, texts = render_questionnaire(QUESTIONNAIRE)
render_results(responses, texts)
