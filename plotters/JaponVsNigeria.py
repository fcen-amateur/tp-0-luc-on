import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
from gapminder import gapminder
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


def plot():

    jap = gapminder[gapminder.country == "Japan"]
    nig = gapminder[gapminder.country == "Nigeria"]

    polynomial_features= PolynomialFeatures(degree=2, include_bias=False)

    x_poly = polynomial_features.fit_transform(jap[['year']])

    modelo = linear_model.LinearRegression()

    modelo.fit(x_poly, jap['pop'])

    beta_jap = modelo.coef_

    beta0_jap = modelo.intercept_.item()



    figura = (
        so.Plot(
            data = gapminder,
            x = "year",
            y = "pop",
        )

        .add(so.Dot(color = "orange", edgecolor = ".1", edgewidth = .5), data = jap)
        .add(so.Line(color = "orange"), so.PolyFit(2), label = "Japón", data = jap)

        .add(so.Dot(color = "g", edgecolor = ".1", edgewidth = .5), data = nig)
        .add(so.Line(color = "g", fillcolor = "blue"), so.PolyFit(2), label = "Nigeria", data = nig)

        .add(so.Text(halign='left', text = 'tt'))



        .limit(x = (1950, 2040), y = (0, 2*1e8))

        .label(
            title="Prueba",
            x="Año",
            y="Población",
        )

        


    )

    return dict(
        descripcion="Crecimiento poblacional de Japón contra Nigeria",
        autor="fela!",
        figura=figura,
    )
