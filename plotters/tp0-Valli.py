import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[gapminder["country"]=="Argentina"], x="year", y = "gdpPercap")
        .add(so.Line())
        .add(so.Dot())
        .label(
            title="El PBI per capita de Argentina",
            x="Año",
            y="PBI per capita",
        )
    )
    return dict(
        descripcion="El PBI per capita de Argentina a través de los años",
        autor="Francisca Valli",
        figura=figura,
    )
