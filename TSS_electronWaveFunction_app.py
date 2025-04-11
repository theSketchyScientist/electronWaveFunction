import streamlit as st
import streamlit.components.v1 as components
import base64

# --- Set page config
st.set_page_config(
    page_title="Hydrogen Atom Orbitals Viewer", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (Dark theme + Fade-in animation)
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #cccccc;
}

/* Fade-in animation keyframes */
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Container for logo and title */
.title-container {
    display: flex; 
    justify-content: center; 
    align-items: center; 
    animation: fadeIn 1.5s ease-out;
}

/* Logo image */
.title-container img {
    width: 100px;
    margin-right: 20px;
}

/* Title text */
.title-container h1 {
    margin: 0;
    font-size: 2.5rem;
    color: #FFFFFF;
}

/* Subheaders */
h2 {
    color: #ffffff;
}

/* Captions below orbitals */
.caption-text {
    margin-top: -130px;
    text-align: left;
    font-size: 0.95rem;
    color: #888888;
}

/* Footer at the bottom */
.footer {
    margin-top: 50px;
    text-align: center;
    font-size: 0.85rem;
    color: #666666;
}
</style>
""", unsafe_allow_html=True)

# --- Helper function to encode the logo image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Load your logo
logo_base64 = get_base64_of_bin_file('TSS_logo.jpeg')

# --- App Title with Logo (Fade-in effect applied)
st.markdown(f"""
<div class="title-container">
    <img src="data:image/jpeg;base64,{logo_base64}" alt="Logo">
    <h1>Hydrogen Atom Orbitals — Interactive 3D Visualizations</h1>
</div>
""", unsafe_allow_html=True)

# --- App Intro Text
st.markdown("""
Explore 3D visualizations of hydrogen atom orbitals (1s, 2p, 3d) based on exact Schrödinger equation solutions.  
Rotate, zoom, and use dropdowns to switch between different views and orientations!
""")

# --- Function to load and display HTML
def display_html(file_path, title, caption):
    st.subheader(title)
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=600, width=800, scrolling=True)
    st.markdown(f"<div class='caption-text'>{caption}</div>", unsafe_allow_html=True)

# --- Display Orbitals
display_html(
    "hydrogen_1s_orbitals.html", 
    "📚 Hydrogen 1s Orbital — Building the 3D Electron Cloud",
    "📷 Rotate to explore the 1s orbital. Use dropdown to toggle between wavefunction, probability density, and radial probability."
)

display_html(
    "hydrogen_2p_orbitals.html", 
    "📚 Hydrogen 2p Orbitals — Visualizing Directional Shapes",
    "📷 Rotate to explore the 2p orbitals. Use dropdown to toggle between x, y, and z aligned shapes."
)

display_html(
    "hydrogen_3d_orbitals.html", 
    "📚 Hydrogen 3d Orbitals — Angular Dependence and Complex Shapes",
    "📷 Rotate and explore the complex shapes of the hydrogen 3d orbitals! Each has unique nodal planes and cloverleaf structures."
)

# --- Footer
st.markdown("""
<div class='footer'>
    Created by <strong>The Sketchy Scientist</strong> — All rights reserved.
</div>
""", unsafe_allow_html=True)
