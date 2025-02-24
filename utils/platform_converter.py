from typing import Dict

class PlatformConverter:
    @staticmethod
    def convert_for_platform(diagram: str, platform: str) -> str:
        """Convert diagram format for specific platforms."""
        platform_handlers = {
            'notion': PlatformConverter._notion_format,
            'obsidian': PlatformConverter._obsidian_format,
            'linear': PlatformConverter._linear_format
        }

        handler = platform_handlers.get(platform.lower())
        if handler:
            return handler(diagram)
        return diagram

    @staticmethod
    def _notion_format(diagram: str) -> str:
        """Format diagram for Notion."""
        return f"```mermaid\n{diagram}\n```"

    @staticmethod
    def _obsidian_format(diagram: str) -> str:
        """Format diagram for Obsidian."""
        return f"```mermaid\n{diagram}\n```"

    @staticmethod
    def _linear_format(diagram: str) -> str:
        """Format diagram for Linear."""
        return f"```mermaid\n{diagram}\n```"