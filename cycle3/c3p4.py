import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_sales = [120, 150, 130, 140, 160, 170, 180, 200, 190, 180, 160, 150]
luxury_sales = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
super_luxury_sales = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
plt.plot(months, affordable_sales, color='green', linestyle='-', label='Affordable Segment')
plt.plot(months, luxury_sales, color='orange', linestyle='--', label='Luxury Segment')
plt.plot(months, super_luxury_sales, color='blue', linestyle=':', label='Super Luxury Segment')
plt.xlabel('Months of Year')
plt.ylabel('Sales of Segments')
plt.title('Sales Data')
plt.legend(loc='upper right')
plt.show()
