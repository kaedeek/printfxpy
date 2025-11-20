from typing import Optional
from .colors import ColorsSet
from .fontsize import FontSize

import re

class PrintFX:
    def __init__(self, color: str = "WHITE", font_style: str = "NORMAL"):
        self.color_list = ColorsSet(color)
        self.font_style = FontSize(font_style)

    def _is_html_color(self, color: str) -> bool:
        return bool(re.match(r"^#([0-9A-Fa-f]{6})$", color))

    def _html_to_ansi(self, color: str) -> str:
        hex_color = color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return f"\033[38;2;{r};{g};{b}m"
    
    def _hex_to_rgb(self, hex_color: str):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def printfx(self, text: str, color: Optional[str] = None, font_style: Optional[str] = None, end: str = "\n") -> None:
        if color:
            if self._is_html_color(color):
                color_code = self._html_to_ansi(color)
            else:
                temp_color = ColorsSet(color)
                color_code = temp_color._getcolor()
        else:
            color_code = self.color_list._getcolor()
        
        if font_style:
            temp_font_style = FontSize(font_style)
            font_code = temp_font_style._get_font_style()
        else:
            font_code = self.font_style._get_font_style()
        
        reset_code = '\033[0m'
        print(f"{color_code}{font_code}{text}{reset_code}", end=end)

    def gradient(self, text: str, start: str, end: str, end_char: str = "\n"):
        if not (self._is_html_color(start) and self._is_html_color(end)):
            raise ValueError("Gradient colors must be HTML hex colors like #RRGGBB")
        
        r1, g1, b1 = self._hex_to_rgb(start)
        r2, g2, b2 = self._hex_to_rgb(end)
        
        length = max(len(text), 1)
        result = ""

        for i, ch in enumerate(text):
            r = r1 + (r2 - r1) * i // (length - 1 or 1)
            g = g1 + (g2 - g1) * i // (length - 1 or 1)
            b = b1 + (b2 - b1) * i // (length - 1 or 1)

            color_code = f"\033[38;2;{r};{g};{b}m"
            result += f"{color_code}{ch}"

        reset_code = "\033[0m"
        print(result + reset_code, end=end_char)