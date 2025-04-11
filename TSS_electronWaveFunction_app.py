import streamlit as st
import streamlit.components.v1 as components

# --- Set page config
st.set_page_config(
    page_title="Hydrogen Atom Orbitals Viewer", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for a sleeker look
st.markdown("""
<style>
/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Background and text colors */
body {
    background-color: #0e1117;
    color: #cccccc;
}

/* Title and header styling with fade-in */
h1, h2 {
    animation: fadeIn 1.5s ease-in;
}

h1 {
    text-align: center;
    font-size: 2.5rem;
    color: #FFFFFF;
    margin-bottom: 1rem;
}

h2 {
    color: #ffffff;
}

/* Style the logo image */
.top-logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 160px;
    height: 160px;
    object-fit: cover;
    border-radius: 50%;
    box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.2);
    animation: fadeIn 2s ease-in;
    margin-bottom: 10px;
}

/* Style the captions nicely */
.caption-text {
    margin-top: -60px;
    text-align: left;
    font-size: 0.95rem;
    color: #888888;
    animation: fadeIn 2s ease-in;
}

/* Footer styling */
.footer {
    margin-top: 50px;
    text-align: center;
    font-size: 0.85rem;
    color: #666666;
    animation: fadeIn 2s ease-in;
}

/* Fade-in keyframes */
@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# --- Display top circular logo
st.markdown(
    "<img class='top-logo' src='TSS_logo.jpeg' alt='Logo'>",
    unsafe_allow_html=True
)

# --- App Title
st.title("Hydrogen Atom Orbitals — Interactive 3D Visualizations")

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
    components.html(html_content, height=600, width=None, scrolling=True)
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
