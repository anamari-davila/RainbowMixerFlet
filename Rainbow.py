import flet as ft 

def main(page: ft.Page):
    def BackgroundColor(e):
        r = red.value
        redvalue.value = r
        g = green.value
        greenvalue.value = g
        b = blue.value
        bluevalue.value = b
        background = f"#{int(r):02x}{int(g):02x}{int(b):02x}"
        HexValue.value = f"#{int(r):02x}{int(g):02x}{int(b):02x}"
        page.bgcolor = background
        page.update()


    Title = ft.Text(value="Background Color Picker", size=20)
    red = ft.Slider(value=0, min=0, max=255, divisions=255, label="{value}%", on_change=BackgroundColor)
    redvalue = ft.Text(value="")
    blue = ft.Slider(value=0, min=0, max=255, divisions=255, label="{value}%", on_change=BackgroundColor)
    bluevalue = ft.Text(value="")
    green = ft.Slider(value=0, min=0, max=255, divisions=255, label="{value}%", on_change=BackgroundColor)
    greenvalue = ft.Text(value="")
    HexValue = ft.Text(value="#000000")

    ColumnMain = ft.Column(controls=[red, redvalue, blue,bluevalue, green, greenvalue, HexValue])
    page.add(Title, ColumnMain) 

ft.app(target=main)