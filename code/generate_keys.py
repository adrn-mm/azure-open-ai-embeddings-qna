import pickle
from pathlib import Path
import os

import streamlit_authenticator as stauth

names = ["admin"]
usernames = ["admin"]
passwords = ["insert_your_password_here"] # change the password here

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
    