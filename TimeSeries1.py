import matplotlib.pylab as plt
import numpy as np
import pandas as pd
% matplotlib
inline

data = pd.read_csv('AirPassengers.csv')

data.head()

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)

ts = data[‘  # Passengers’]

ts.head(10)

ts['1949']

plt.plot(ts)


def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()

    # Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)


test_stationarity(ts)

ts_log = np.log(ts)

ts_log_diff = ts_log - ts_log.shift()

ts_log_diff.dropna(inplace=True)
test_stationarity(ts_log_diff)
plt.plot(ts_log_diff)
