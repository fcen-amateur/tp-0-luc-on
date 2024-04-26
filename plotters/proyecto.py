import seaborn.objects as so
from gapminder import gapminder
import pandas as pd

def plot():
    ex_paises_sovieticos = ["Russia", "Ukraine", "Belarus", "Moldova", "Estonia", "Latvia", "Lithuania"]
    colores = pd.Series([])
    colores.
    for x in gapminder[gapminder.continent == "Europe"]:
        colores.append( "red" if x in ex_paises_sovieticos  else "blue" )
    
       
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Europe"],
            x="year",
            y="lifeExp",
            color= colores
        )
        .add(so.Dot())
        .label(
            title="Expectativa de vida en America",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países de Oceanía a lo largo del tiempo",
        autor="La cátedra",
        figura=figura,
    )
    


