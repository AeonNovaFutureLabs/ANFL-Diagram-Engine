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
    """Load sample diagram from assets."""
    with open("attached_assets/Pasted-graph-TB-Physical-Layer-subgraph-Physical-Physical-Infrastructure-direction-TB-1740366126683.txt", "r") as f:
        return f.read()

def main():
    st.title("ANFL Diagram Engine") # Title changed here

    # Input type selection
    input_type = st.sidebar.selectbox(
        "Select Input Type",
        ["Mermaid", "LaTeX"]
    )

    # Input area for diagrams
    sample_diagram = load_sample_diagram() if input_type == "Mermaid" else ""
    diagram_input = st.text_area(
        "Enter your diagram code",
        value=sample_diagram,
        height=300,
        help=f"Paste your {input_type} diagram code here"
    )

    # Preview/Code tabs
    tab1, tab2 = st.tabs(["Preview", "Code"])

    if diagram_input:
        try:
            if input_type == "Mermaid":
                diagrams = DiagramProcessor.parse_mermaid(diagram_input)
                combined_diagram = DiagramProcessor.combine_diagrams(diagrams)
                processed_diagram = DiagramProcessor.apply_theme(combined_diagram)
            else:
                processed_diagram = diagram_input

            with tab1:
                st.markdown("### Visualization")
                if input_type == "Mermaid":
                    st.markdown(f"```mermaid\n{processed_diagram}\n```")
                else:
                    st.latex(processed_diagram)

            with tab2:
                st.markdown("### Source Code")
                st.code(diagram_input, language="mermaid" if input_type == "Mermaid" else "latex")

            # Export options
            st.sidebar.markdown("### Export Options")
            export_format = st.sidebar.selectbox(
                "Export Format",
                ['PDF', 'Notion', 'Obsidian', 'Linear', 'LaTeX']
            )

            try:
                if export_format == 'PDF':
                    pdf = ExportHandler.create_pdf(processed_diagram)
                    st.sidebar.download_button(
                        "Download PDF",
                        pdf,
                        "diagram.pdf",
                        "application/pdf"
                    )
                elif export_format == 'LaTeX':
                    latex_output = ExportHandler.create_latex(processed_diagram) if input_type == "Mermaid" else processed_diagram
                    st.sidebar.download_button(
                        "Download LaTeX",
                        latex_output.encode(),
                        "diagram.tex",
                        "text/plain"
                    )
                else:
                    platform_output = PlatformConverter.convert_for_platform(
                        processed_diagram,
                        export_format
                    )
                    st.sidebar.download_button(
                        f"Download for {export_format}",
                        platform_output.encode(),
                        f"diagram_{export_format.lower()}.md",
                        "text/markdown"
                    )
            except Exception as e:
                st.sidebar.error(f"Error during export: {str(e)}")

        except Exception as e:
            st.error(f"Error processing diagram: {str(e)}")

if __name__ == "__main__":
    main()