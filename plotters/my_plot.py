import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[(gapminder['country']!='United States') & (gapminder['country']!='Canada')], x="continent")
        .add(so.Dot()).add(so.Line(),so.PolyFit(1))
        .label(
            title='Relación entre gdp per capita y expectativa de vida - Sin cono Norte',
            x='Expectativa de vida',
            y='gdp per capita'
        )
    )
    return dict(
        descripcion="Relación entre gdp per capita y expectativa de vida - Sin cono Norte (US, Canada) + regresión",
        autor="AlejoGonc",
        figura=figura,
    )
