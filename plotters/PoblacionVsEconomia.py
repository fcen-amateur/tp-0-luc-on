import seaborn as sns
import seaborn.objects as so
from gapminder import gapminder
import numpy as np
import pandas as pd

def plot():
    
   
    paises_objetivo = ["Brazil","Argentina","Chile","Mexico","China","United States","India","Germany","Italy","Japan"]
    paises = gapminder[ (gapminder.country.isin(paises_objetivo)) &(gapminder.year > 1980)]


    figura = (so.Plot(paises,"year",y = paises["gdpPercap"]*paises["pop"],color = "country",pointsize = "pop")
        .add(so.Dot())
        .label(title="PBI vs Poblacion",
            x="Año",
            y="Producto Bruto Interno")
             
        ).scale(pointsize = (1,20))

    
    return dict(
        descripcion="Contario a lo que la intuicion nos diria, no hay una correlacion directa entre la poblacion y el tamaño de una economia. En la modernidad, el acceso a la tecnologia,capitales,educacion junto con la existencia de robustaz instituciones nacionales tienen mucho mas relevancia para las economias que el tamaño de sus poblaciones",
        autor="Daniel Bustos",
        figura=figura,
    )
    

