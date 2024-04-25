import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
          gapminder[gapminder["country"].isin(["Gabon", "Kuwait","United States", "Norway", "Australia"])],
          x = "year",
          y = "gdpPercap", 
          color = "country", 
          linestyle = "continent"
        )
        .add(so.Line(linewidth = 3))
        .layout(size = (11,7))
        .label(
          title="Paises con mayor PBI per capita de cada continente", 
          x = "Año", 
          y = "PBI per capita", 
          color = "Pais", 
          linestyle = "Continente"
        )
    )
    return dict(
        descripcion="Evolucion de los paises con mayor PBI per capita de cada continente a lo largo del tiempo",
        autor="La cátedra",
        figura=figura,
    )
