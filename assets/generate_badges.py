"""
Script to generate custom SVG badges for ANFL profiles
"""
def generate_badge(label: str, message: str, color: str) -> str:
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
        <linearGradient id="b" x2="0" y2="100%">
            <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
            <stop offset="1" stop-opacity=".1"/>
        </linearGradient>
        <mask id="a">
            <rect width="100" height="20" rx="3" fill="#fff"/>
        </mask>
        <g mask="url(#a)">
            <path fill="#1A1A2E" d="M0 0h50v20H0z"/>
            <path fill="{color}" d="M50 0h50v20H50z"/>
            <path fill="url(#b)" d="M0 0h100v20H0z"/>
        </g>
        <g fill="#fff" text-anchor="middle" font-family="Helvetica" font-size="11">
            <text x="25" y="15" fill="#E6E6E6">{label}</text>
            <text x="75" y="15" fill="#E6E6E6">{message}</text>
        </g>
    </svg>
    """
