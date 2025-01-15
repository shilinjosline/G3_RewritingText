import matplotlib.pyplot as plt

# Generate the first chart
categories = ['Class A', 'Class B', 'Class C', 'Class D']
values = [0.4, 0.6, 0.8, 0.2]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='skyblue')
plt.title('Class Probabilities - Chart 1')
plt.xlabel('Categories')
plt.ylabel('Probability')
plt.savefig('images/chart1.png')  # Save to the /images folder
plt.close()

# Generate the second chart
values2 = [0.5, 0.3, 0.7, 0.4]

plt.figure(figsize=(6, 4))
plt.bar(categories, values2, color='lightgreen')
plt.title('Class Probabilities - Chart 2')
plt.xlabel('Categories')
plt.ylabel('Probability')
plt.savefig('images/chart2.png')  # Save to the /images folder
plt.close()

print("Charts generated and saved successfully!")
