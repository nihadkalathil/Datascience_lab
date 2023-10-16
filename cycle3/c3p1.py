import matplotlib.pyplot as plt
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]
plt.figure(figsize=(8, 6))
plt.plot(years, car_values, linestyle='-.', color='red', label='Car Value')
plt.scatter(years, car_values, marker='*', color='green', s=200, label='Data Points')
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation', loc='left')
plt.legend()
plt.show()
