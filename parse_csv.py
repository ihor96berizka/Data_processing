import pandas
import matplotlib.pyplot as plt
import matplotlib
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

data = pandas.read_csv('august2.csv', parse_dates=['hour'])

n = 1000
dates = data['hour'][0:n]
print(dates)

temperature = data['temperature'][0:n]
for i in range(0,n):
    temperature[i] = temperature[i] / 100.0
print(temperature)

depth = data['depth'][0:n]

plt.subplot(2, 1, 1)
plt.plot(dates, temperature, '.')
plt.title('Sensors readings')
plt.ylabel('temperature, C')

plt.subplot(2, 1, 2)
plt.plot(dates, depth, '.')
plt.ylabel("Depth, cm")
plt.xlabel('date')

plt.show()
