import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm

data = pd.read_csv('./housePrediction/train.csv')

data.describe()

# univariant

data['SalePrice'].describe()

data['SalePrice'].plot(kind="hist")

sns.distplot(data['SalePrice'], fit=norm)

data['SalePrice'].skew()

data['SalePrice'] = np.log1p(data['SalePrice'])

sns.distplot(data['SalePrice'], fit=norm)

data['SalePrice'].skew()

# bivariant

data.hist(bins=50, figsize=(30, 20));

data['GrLivArea'] = np.log1p(data['GrLivArea'])

var = 'GrLivArea'
livingSales = pd.concat([data['SalePrice'], data[var]], axis=1)
livingSales.plot.scatter(x=var, y='SalePrice')

var = 'YearBuilt'
yearSales = pd.concat([data['SalePrice'], data[var]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
plt.xticks(rotation=90);

# multivariant

corrmat = data.corr(method='spearman')
f, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

# correlation matrix
corrmat = data.corr(method='spearman')
cg = sns.clustermap(corrmat, cmap="YlGnBu", linewidths=0.1);
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
cg
