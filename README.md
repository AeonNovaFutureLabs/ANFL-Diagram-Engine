# ANFL Diagram Engine

A robust diagram processing engine built for Aeon Nova Future Labs that supports multiple diagram formats and export options.

## Features

- Support for Mermaid and LaTeX diagram inputs
- Interactive preview with code/visualization tabs
- Multiple export formats:
  - PDF with custom styling
  - LaTeX with TikZ
  - Notion-compatible markdown
  - Obsidian-compatible markdown
  - Linear-compatible markdown
- Custom theme support with ANFL color scheme
- IDE integration for VS Code and JetBrains products

## Installation

1. Clone the repository
```bash
git clone https://github.com/AeonNovaFutureLabs/ANFL-Diagram-Engine.git
cd ANFL-Diagram-Engine
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run main.py
```

## Development

- Built with Streamlit for the web interface
- Uses custom styling defined in `styles.css`
- Supports multiple IDE configurations
- Implements ANFL's design guidelines

## Project Structure

```
├── .streamlit/          # Streamlit configuration
├── .vscode/            # VS Code settings
├── .idea/             # JetBrains IDE settings
├── utils/             # Utility modules
│   ├── diagram_processor.py
│   ├── export_handler.py
│   ├── latex_converter.py
│   └── platform_converter.py
├── main.py            # Main application
└── styles.css         # Custom styling
```

## License

Copyright © 2024 Aeon Nova Future Labs. All rights reserved.
