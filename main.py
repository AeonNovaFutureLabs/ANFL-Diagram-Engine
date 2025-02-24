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

def load_sample_diagram():
    with open("attached_assets/Pasted-graph-TB-Physical-Layer-subgraph-Physical-Physical-Infrastructure-direction-TB-1740366126683.txt", "r") as f:
        return f.read()

def main():
    st.title("Mermaid Diagram Processor")

    # Input area for diagrams
    sample_diagram = load_sample_diagram()
    diagram_input = st.text_area(
        "Enter your Mermaid diagram(s)",
        value=sample_diagram,
        height=300,
        help="Paste your Mermaid diagram content here"
    )

    # Platform selection
    platforms = ['Notion', 'Obsidian', 'Linear', 'LaTeX']
    selected_platform = st.selectbox("Select platform for export", platforms)

    if diagram_input:
        # Process diagrams
        diagrams = DiagramProcessor.parse_mermaid(diagram_input)
        combined_diagram = DiagramProcessor.combine_diagrams(diagrams)
        themed_diagram = DiagramProcessor.apply_theme(combined_diagram)

        # Display the processed diagram
        st.markdown("### Preview")
        st.markdown(f"```mermaid\n{themed_diagram}\n```")

        # Export options
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Platform Export")

            if selected_platform == 'LaTeX':
                latex_output = ExportHandler.create_latex(themed_diagram)
                st.code(latex_output, language="latex")
                st.download_button(
                    "Download LaTeX",
                    latex_output.encode(),
                    "diagram.tex",
                    "text/plain"
                )
            else:
                platform_output = PlatformConverter.convert_for_platform(
                    themed_diagram, 
                    selected_platform
                )
                st.code(platform_output, language="markdown")
                st.download_button(
                    f"Download for {selected_platform}",
                    platform_output.encode(),
                    f"diagram_{selected_platform.lower()}.md",
                    "text/markdown"
                )

        with col2:
            st.markdown("### PDF Export")
            pdf = ExportHandler.create_pdf(themed_diagram)
            st.download_button(
                "Download PDF",
                pdf,
                "diagram.pdf",
                "application/pdf"
            )

if __name__ == "__main__":
    main()