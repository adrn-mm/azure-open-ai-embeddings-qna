import streamlit as st
from stlib import Chat
from stlib import Add_Document
from stlib import Document_Management
from stlib import Index_Management
import pickle
import streamlit_authenticator as stauth
from pathlib import Path
import os

st.set_page_config(layout="wide",
                   page_title='MLPT - LLM ChatBot', page_icon=':robot_face') 

col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image('logo_mlpt.png')

names = ["Admin"]
usernames = ["admin"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
                                    "llm_chatbot", "abcdef",
                                    cookie_expiry_days=7)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    
if authentication_status == None:
    st.warning("Please enter your username & password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    pages = {
        'Chat': Chat,
        'Add Document': Add_Document,
        'Document Management': Document_Management,
        'Index Management': Index_Management
    }

    selection = st.sidebar.radio("Features", list(pages.keys()))

    page = pages[selection]
    page.run()
