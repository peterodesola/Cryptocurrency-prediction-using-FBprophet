import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


START= "2019-03-01"
TODAY= date.today().strftime("%Y-%m-%d")

st.title("Cryptocurrency Prediction App")

stocks= ('BTC','LTC','ZEC','AUR','NEO','BCH','XRP','ADA','XLM','USDT','ETC','XMR','DASH','FIRO','Nano','Dg', 'ETH','ALGO','VET','XTZ','MZC')
selected_stock= st.selectbox("Select dataset for prediction", stocks)
n_years= st.slider("Years of prediction:", 1, 4)
period=n_years *365

@st.cache
def load_df(ticker):
    df=yf.download(ticker, START, TODAY)
    df.reset_index(inplace=True)
    return df

df_load_state =st.text("Load df...")
df=load_df(selected_stock)
df_load_state.text("Loading df...done!")

st.subheader('Raw data')
st.write(df.tail())

def plot_raw_df():
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Date", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_df()

#forcasting our dataset
df_train= df[['Date', 'Close']]
df_train= df_train.rename(columns={"Date": "ds", "Close": "y"})

m=Prophet()
m.fit(df_train)
future=m.make_future_dataframe(periods=period)
forecast= m.predict(future)

st.subheader('forecast data')
st.write(forecast.tail())


st.write('forecast data')
fig1= plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('forecast components')
fig2= m.plot_components(forecast)
st.write(fig2)


