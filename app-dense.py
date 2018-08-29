# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:26:14 2018

@author: newton
"""


from scipy.special import zeta
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

DEBUG = False
# WARNING: Increasing precision will incur heavy computation cost and will
#          cause massive slowdown. 
ARITHMATIC_PRECISION = 5


def riemann_zeta_approximator(s):
    value = 0
    terms = {}
    if np.iscomplex(s):
        for n in range(10**ARITHMATIC_PRECISION):
          if n != 0:
            denominator = n**s
            nth_term = 1 / denominator
            value += nth_term
            terms[str(n)] = nth_term
    else:
        value = zeta(s)
    return value

def main():
    r = np.linspace(-10,10,1000)
    i = np.linspace(-10,10,1000)
    s_coordinates = [complex(r[id_r],i[id_i]) for id_i in range(len(i)) for id_r in range(len(r))]

    transformed_coordinates = [riemann_zeta_approximator(wee) for wee in s_coordinates]

    input_real = np.real(s_coordinates)
    input_imag = np.imag(s_coordinates)
    output_real = np.real(transformed_coordinates)
    output_imag = np.imag(transformed_coordinates)

    trace0 = go.Scatter(
        x = input_real,
        y = input_imag,
        mode = 'markers',
        name = 'input',
        marker=dict(
            size=1,
            color=np.sqrt(input_real**2 + input_imag**2),                
            colorscale='Rainbow',   
            opacity=1
        )
    )

    trace1 = go.Scatter(
        x = output_real,
        y = output_imag,
        mode = 'markers',
        name = 'output',
        marker=dict(
            size=1,
            color=np.sqrt(input_real**2 + input_imag**2),                
            colorscale='Rainbow',   
            opacity=1
        )
    )

    data = []
    data.append(trace0)
    fig = go.Figure(data=data)
    plot(fig, filename='viz-s.html')

    data = []
    data.append(trace1)
    fig = go.Figure(data=data)
    plot(fig, filename='viz-zeta.html')

    if DEBUG:
        print(0)

if __name__ == "__main__":
    main()