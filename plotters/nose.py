import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(datos_oceania,x="year",y="lifeExp")
    .add(so.Dot())
    .add(so.Lines(color="#bbca"))
    .add(so.Line(), so.PolyFit(1))
    .facet("country")
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con la expectativa de vida de cada pais de Oceania en funcion del tiempo",
        autor="Dante Barbieri",
        figura=figura,
    )
