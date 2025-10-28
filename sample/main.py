from printfx import PrintFX

# Test with default font style
printfx = PrintFX("RED")
printfx.printfx("Default font style")

# Test with bold font
printfx_bold = PrintFX("GREEN", "BOLD")
printfx_bold.printfx("Bold font")

# Test with underlined font
printfx_underline = PrintFX("BLUE", "UNDERLINE")
printfx_underline.printfx("Underlined font")

# Specify font style at runtime
printfx.printfx("Italic at runtime", font_style="ITALIC")
printfx.printfx("Strikethrough at runtime", font_style="STRIKETHROUGH")

# Change color and font style simultaneously
printfx.printfx("Red with bold", color="RED", font_style="BOLD")
printfx.printfx("Green with underline", color="GREEN", font_style="UNDERLINE")

# HTML color code examples
printfx.printfx("This text uses a custom HTML color #FF5733", color="#FF5733")
printfx.printfx("This text uses another HTML color #1ABC9C with italic style", color="#1ABC9C", font_style="ITALIC")