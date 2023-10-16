import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_sales = [120, 150, 130, 140, 160, 170, 180, 200, 190, 180, 160, 150]
luxury_sales = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
super_luxury_sales = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
plt.scatter(months, affordable_sales, color='pink', label='Affordable Segment', s=100)
plt.scatter(months, luxury_sales, color='yellow', label='Luxury Segment', s=100)
plt.scatter(months, super_luxury_sales, color='blue', label='Super Luxury Segment', s=100)
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments', fontsize=18)
plt.title('Sales Data', fontsize=20)
plt.legend()
plt.show()
