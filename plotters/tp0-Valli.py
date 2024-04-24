import seaborn.objects as so
from gapminder import gapminder

datosArg = gapminder[gapminder["country"]=="Argentina"]
datosChile = gapminder[gapminder["country"]=="Chile"]

def plot():
    figura = (
        so.Plot(data = datosArg, x = "year", color = "country")
        .add(so.Line(), y = datosChile.gdpPercap)
        .add(so.Line(), y = datosArg.gdpPercap)
        .label(
            title="El PBI per capita de Argentina y Chile",
            x="Año",
            y="PBI per capita",
        )
    )
    return dict(
        descripcion="Comparación del PBI per capita de Argentina y Chile a través de los años",
        autor="Francisca Valli",
        figura=figura,
    )
