# -*- coding: utf-8 -*-
"""
Created on Tue May 15 03:19:18 2018

@author: soham
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

r = np.linspace(-7,7,10)
i = np.linspace(-5,5,10)
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
        size=4,
        color=np.sqrt(input_real**2 + input_imag**2),                
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
"""    
data.append(trace0)
fig = go.Figure(data=data)
plot(fig, filename='viz-s.html')

data=[]
data.append(trace1)
fig = go.Figure(data=data)
plot(fig, filename='viz-zeta.html')