import streamlit as st
import base64
from utils.diagram_processor import DiagramProcessor
from utils.export_handler import ExportHandler
from utils.platform_converter import PlatformConverter

# Configure page
st.set_page_config(
    page_title="Mermaid Diagram Processor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.title("Mermaid Diagram Processor")
    
    # Input area for diagrams
    diagram_input = st.text_area(
        "Enter your Mermaid diagram(s)",
        height=300,
        help="Paste your Mermaid diagram content here"
    )
    
    if diagram_input:
        # Process diagrams
        diagrams = DiagramProcessor.parse_mermaid(diagram_input)
        combined_diagram = DiagramProcessor.combine_diagrams(diagrams)
        themed_diagram = DiagramProcessor.apply_theme(combined_diagram)
        
        # Display the processed diagram
        st.markdown("### Preview")
        st.markdown(f"