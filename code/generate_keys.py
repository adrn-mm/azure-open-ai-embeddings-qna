import pickle
from pathlib import Path
import os

import streamlit_authenticator as stauth

names = ["Adrian Maulana Muhammad"]
usernames = ["adrnmm"]
passwords = ["password01"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
    