# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:26:14 2018

@author: newton
"""


from scipy.special import zeta
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

def riemann_zeta(s):
  value = 0
  terms = {}
  if np.iscomplex(s):
    for n in range(10000):
      if n != 0:
        denominator = n**s
        nth_term = 1 / denominator
        value += nth_term
        terms[str(n)] = nth_term
  else:
    value = zeta(s)
  return value

r = np.linspace(-10,10,1000)
i = np.linspace(-10,10,1000)
p = [complex(r[id_r],i[id_i]) for id_i in range(len(i)) for id_r in range(len(r))]

q = [riemann_zeta(wee) for wee in p]

input_real = np.real(p)
input_imag = np.imag(p)
output_real = np.real(q)
output_imag = np.imag(q)

trace0 = go.Scatter(
    x = input_real,
    y = input_imag,
    mode = 'markers',
    name = 'input',
    marker=dict(
        size=4,
        color='brown',                
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
        size=4,
        color='green',                
        colorscale='Rainbow',   
        opacity=1
    )
)
data = []
"""
for idx in range(len(input_real)):
    trace_new = go.Scatter(
        x=[input_real[idx],output_real[idx]],
        y=[input_imag[idx],output_imag[idx]],
        line=dict(
            color='blue',
            width=1
        )
    )
    data.append(trace_new)    
    
data.append(trace0)
"""
data.append(trace1)

fig = go.Figure(data=data)
plot(fig, filename='viz.html')