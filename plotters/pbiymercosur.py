import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[gapminder['country'].isin(['Argentina', 'Paraguay', 'Uruguay', 'Brazil'])], "year", "gdpPercap", color = 'country')
        .add(so.Line())
        .add(so.Dots())
        .label(
            title="Países del Mercosur",
            x="Año",
            y="PBI",
        )        
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="La cátedra",
        figura=figura,
    )
