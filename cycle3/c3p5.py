import matplotlib.pyplot as plt
# Data
modes_of_transport = ['Walking', 'Bicycling', 'Bus', 'Car', 'Other']
frequency = [25, 15, 30, 20, 10]
# Create a bar graph
plt.figure(figsize=(8, 6))
plt.bar(modes_of_transport, frequency, color='green', width=0.1)
# Set labels and title
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')
# Show the bar graph
plt.xticks(rotation=45) # Rotate the x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping of labels
plt.show()