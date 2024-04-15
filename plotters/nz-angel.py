import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder, x="year", y='gdpPercap', color='continent')
        .add(so.Line(marker='D'), so.Agg('mean'))
        .label(
            title="Evolución de PBI per capita promedio por continente",
            x="Año",
            y="PBI per capita",
            color='Continente'
        )
    )
    return dict(
        descripcion="Masterclass en gráficos de evolución de PBI per capita promedio de continentes",
        autor="Naza",
        figura=figura,
    )