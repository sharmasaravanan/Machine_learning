import pandas as pd
from plotly.plotly import plot_mpl
from pyramid.arima import auto_arima
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv("./electricity.csv", index_col=0)

data.index = pd.to_datetime(data.index)
data.columns = ['Energy Production']

data.iplot(title="Energy Production Jan 1985--Jan 2018", theme='pearl')

result = seasonal_decompose(data, model='multiplicative')
fig = result.plot()
plot_mpl(fig)

stepwise_model = auto_arima(data, start_p=1, start_q=1,
                            max_p=3, max_q=3, m=12,
                            start_P=0, seasonal=True,
                            d=1, D=1, trace=True,
                            error_action='ignore',
                            suppress_warnings=True,
                            stepwise=True)
print(stepwise_model.aic())

train = data.loc['1985-01-01':'2016-12-01']
test = data.loc['2017-01-01':]

stepwise_model.fit(train)

future_forecast = stepwise_model.predict(n_periods=37)
print(future_forecast)

future_forecast = pd.DataFrame(future_forecast, index=test.index, columns=['Prediction'])
pd.concat([test, future_forecast], axis=1).iplot()

pd.concat([data, future_forecast], axis=1).iplot()
