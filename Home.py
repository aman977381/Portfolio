import streamlit as st
from pathlib import Path
from PIL import Image

# -- Path Setings --
curent_dir = Path(__file__).parent if  "__file__" in locals() else Path.cwd()
css_files = curent_dir/"styles"/"main.css"