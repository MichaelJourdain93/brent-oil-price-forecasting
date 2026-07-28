import streamlit as st
import joblib
from prophet.plot import plot_plotly
# import plotly.graph_objs as go

model = joblib.load('models/prophet_model_final.pkl')

st.title("Previsão do Preço do Petróleo Brent")

days = st.number_input("Quantos dias para prever?", min_value=1, max_value=365, value=7)

future_dates = model.make_future_dataframe(periods=days)

# Gerar previsão
forecast = model.predict(future_dates)

# Exibir resultado
st.write("Previsão do preço em US$ para os próximos {} dias:".format(days))
st.write(forecast[['ds', 'yhat']].tail(days))

# Plotar previsão
plot = plot_plotly(model, forecast)
st.plotly_chart(plot)
