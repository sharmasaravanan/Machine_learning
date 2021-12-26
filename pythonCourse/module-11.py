import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# figure
# plot
# graph/visualisation stuff

# line chart, scatter plot, bar, pie, histogram and box

x = list(range(1,6))
y = [i*i for i in x]
y1 = [i*i*i for i in x]

print(x,y,y1)

# line chart

plt.plot(x,y,color='r', linestyle='--', marker="s")
plt.xlabel("n value")
plt.ylabel("n^2")
plt.title("Simple line chart")
plt.show()

plt.plot(x,y,'r--s', x, y1, 'b-v')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.title("Simple line chart")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.show()


plt.subplot(211)
plt.plot(x,y,'r--s')
plt.ylabel("f(n)")
plt.title("Simple line chart")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.subplot(212)
plt.plot(x, y1, 'b-v')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.show()

plt.subplot(121)
plt.plot(x,y,'r--s')
plt.ylabel("f(n)")
plt.title("Simple line chart")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.subplot(122)
plt.plot(x, y1, 'b-v')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.show()

plt.figure(1)
plt.plot(x,y,'r--s')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.title("Simple line chart")
plt.legend(["n Vs n^2", "n Vs N^3"])

plt.figure(2)
plt.plot( x, y1, 'b-v')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.title("Simple line chart")
plt.legend(["n Vs n^2", "n Vs N^3"])
plt.show()

# scatter chart
plt.scatter(x,y,color='r',marker='s')
plt.xlabel("n value")
plt.ylabel("f(n)")
plt.title("Simple scatter chart")
plt.show()

import numpy as np
data = {'a': np.arange(5),
        'c': np.random.randint(0, 50, 5),
        'd': np.random.randn(5)}
data['b'] = data['a'] + 10 * np.random.randn(5)
data['d'] = np.abs(data['d']) * 100


plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# bar chart

plt.bar(x,y, facecolor='#123456')
plt.show()

plt.barh(x,y, facecolor='#123456')
plt.show()

x = ['apple','mango','orange']
y = [25,29,41]
plt.bar(x,y)
plt.show()

# pie chart
x = ['apple','mango','orange']
y = [25,29,41]
plt.pie(y,labels=x, labeldistance=0.5)
plt.show()

# hist
x = np.random.randint(0, 50, 15)
plt.hist(x)
plt.show()

x = np.random.randint(0, 50, 15)
plt.boxplot(x)
plt.show()

csvData = pd.read_csv("./Advertising.csv" , index_col=0)
print(csvData.head())

csvData.plot.hist(alpha=0.5)
plt.show()

csvData.plot.box()
plt.show()

csvData.plot.kde()
plt.show()
