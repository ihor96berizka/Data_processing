import pandas
import matplotlib.pyplot as plt
import matplotlib
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

filename = 'september.csv'
data = pandas.read_csv(filename, parse_dates=['hour'])

n = 1000
dates = data['hour'].to_list()#[0:n]
print('type(dates): ', type(dates))
print('dates: ')
print(dates)

temperature = data['temperature'].to_list()#[0:n]
#for i in range(0,len(dates)):
#    temperature[i] = temperature[i] / 100.0
print('type(temperature): ', type(temperature))
print('temperature: ')
print(temperature)

filteredData = dict(zip(dates, temperature))
print('filteredData:')
print(filteredData)
# A list of the keys of dictionary
list_keys = [k for k in filteredData]

# or a list of the values
list_values = [v for v in filteredData.values()]
#depth = data['depth'][0:n]

plt.subplot(1, 1, 1)
plt.plot(list_keys, list_values, '-o')
plt.title('Sensors readings')
plt.ylabel('temperature, C')
'''
plt.subplot(2, 1, 2)
plt.plot(dates, temperature, '.')
plt.ylabel("Depth, cm")
plt.xlabel('date')
'''
plt.show()
