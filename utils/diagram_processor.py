import base64
import io
from typing import List, Tuple

class DiagramProcessor:
    @staticmethod
    def parse_mermaid(content: str) -> List[str]:
        """Parse multiple Mermaid diagrams from content."""
        diagrams = []
        current_diagram = []
        in_diagram = False
        
        for line in content.split('\n'):
            if line.strip().startswith('graph') or line.strip().startswith('sequenceDiagram'):
                if current_diagram:
                    diagrams.append('\n'.join(current_diagram))
                current_diagram = [line]
                in_diagram = True
            elif in_diagram:
                current_diagram.append(line)
                
        if current_diagram:
            diagrams.append('\n'.join(current_diagram))
            
        return diagrams

    @staticmethod
    def combine_diagrams(diagrams: List[str]) -> str:
        """Combine multiple Mermaid diagrams with proper spacing."""
        return '\n\n'.join(diagrams)

    @staticmethod
    def apply_theme(diagram: str) -> str:
        """Apply custom theme to Mermaid diagram."""
        theme_config = """
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#1A1A2E',
    'primaryTextColor': '#E6E6E6',
    'primaryBorderColor': '#CD7F32',
    'lineColor': '#CD7F32',
    'secondaryColor': '#33334C',
    'tertiaryColor': '#E6E6E6'
  }
}}%%
"""
        return f"{theme_config}\n{diagram}"
