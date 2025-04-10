import streamlit as st
import streamlit.components.v1 as components

# --- Set page config
st.set_page_config(page_title="Hydrogen Atom Orbitals Viewer", layout="centered")

# --- App Title
st.title("Hydrogen Atom Orbitals — Interactive 3D Visualizations")

st.markdown("""
Explore 3D visualizations of hydrogen atom orbitals (1s, 2p, 3d) based on exact Schrödinger equation solutions.
Rotate, zoom, and use dropdowns to switch between different views and orientations!
""")

# --- Function to load and display HTML
def display_html(file_path, title, caption):
    st.subheader(title)
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    container = st.container()
    with container:
        components.html(html_content, height=600, width=800, scrolling=True)
        st.markdown(
            f"<div style='margin-top: -140px; text-align: left; font-size: 0.99rem; color: #999999;'>{caption}</div>", 
            unsafe_allow_html=True
        )
    # st.markdown(divider_html, unsafe_allow_html=True)  # custom clean thin divider

# --- Stack the orbitals
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
