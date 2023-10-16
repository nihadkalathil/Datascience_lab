import matplotlib.pyplot as plt
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(days, drinks_sales, linestyle=':', color='cyan', label='Drinks Sales')
plt.scatter(days, drinks_sales, marker='h', color='magenta', edgecolor='black', s=100)
plt.xlabel('Days of Week')
plt.ylabel('Sale of Drinks')
plt.title('Sales Data1', loc='right')
plt.legend()
plt.grid(color='blue')
plt.subplot(2, 1, 2)
plt.plot(days, food_sales, linestyle='--', color='yellow', label='Food Sales')
plt.scatter(days, food_sales, marker='D', color='green', edgecolor='red', s=100)
plt.xlabel('Days of Week')
plt.ylabel('Sale of Food')
plt.title('Sales Data2', loc='center')
plt.legend()
plt.grid(color='blue')
plt.tight_layout()
plt.show()
