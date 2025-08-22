import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
data = pd.read_csv('munis.csv')

st.title("Primera aplicación ")



munis = data['entidad'].unique().tolist()
mun = st.selectbox('seleccione un municipio: ',
             munis)
             
filtro = data[data['entidad'] ==mun]


gen = (filtro 
       .groupby('clasificacion_ofpuj')['total_recaudo']
       .sum())
total_gen = gen.sum()
gen = (gen/total_gen).round(2)
st.write(total_gen)
det = ( filtro
       .groupby('clasificacion_ofpuj')['total_recaudo']
       .sum())

 # clasificacion general

 # clasificacion detallada 

#pie chart
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.pie(det.values, labels=det.index)
st.pyplot(fig)

fin = (filtro
       .groupby(['clas_gen', 'clasificacion_ofpuj'])['total_recaudo'] 
       .sum()
       .reset_index())

fig = px.treemap(fin, path=[px.Constant('Total'), 
                            'clas_gen',
                            'clasificacion_ofpuj'],
                            values='total_recaudo')
st.plotly_chart(fig)
