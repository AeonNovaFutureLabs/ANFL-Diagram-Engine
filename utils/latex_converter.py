import re
from typing import Dict, List, Tuple

class LaTeXConverter:
    @staticmethod
    def mermaid_to_tikz(diagram: str) -> str:
        """Convert Mermaid diagram to TikZ format."""
        header = """
\\documentclass{article}
\\usepackage{tikz}
\\usepackage[utf8]{inputenc}
\\usepackage{xcolor}

% Custom colors
\\definecolor{myblue}{RGB}{26,26,46}
\\definecolor{mybronze}{RGB}{205,127,50}
\\definecolor{mysecondary}{RGB}{51,51,76}
\\definecolor{bggray}{RGB}{230,230,230}

\\usetikzlibrary{shapes,arrows,shadows,backgrounds}

\\begin{document}
\\begin{tikzpicture}[
    node distance=2cm,
    box/.style={
        rectangle,
        rounded corners,
        draw=mybronze,
        fill=white,
        text=myblue,
        minimum height=1cm,
        align=center
    },
    line/.style={
        draw=mybronze,
        ->,
        >=stealth,
        thick
    }
]

"""
        footer = """
\\end{tikzpicture}
\\end{document}
"""
        
        # Convert nodes
        nodes = []
        connections = []
        
        # Extract nodes and connections from Mermaid
        for line in diagram.split('\n'):
            line = line.strip()
            if '-->' in line:
                parts = line.split('-->')
                source = parts[0].strip()
                target = parts[1].strip()
                connections.append((source, target))
            elif '[' in line and ']' in line:
                node_match = re.match(r'(\w+)\["([^"]+)"\]', line)
                if node_match:
                    node_id = node_match.group(1)
                    node_label = node_match.group(2)
                    nodes.append((node_id, node_label))

        # Generate TikZ nodes
        tikz_nodes = []
        for i, (node_id, label) in enumerate(nodes):
            pos = f"({i*3}, {-i*2})"
            tikz_nodes.append(f"\\node[box] ({node_id}) at {pos} {{{label}}};")

        # Generate TikZ connections
        tikz_connections = []
        for source, target in connections:
            tikz_connections.append(f"\\draw[line] ({source}) -- ({target});")

        # Combine all parts
        tikz_content = header + '\n'.join(tikz_nodes) + '\n' + '\n'.join(tikz_connections) + footer
        
        return tikz_content
