import matplotlib.pyplot as plt

hobbies = ['Волейбол', 'Хендмейд', 'Музика', 'Книги', 'Психологія']
shares = [45, 15, 10, 10, 20] 

plt.figure(figsize=(8, 8))
plt.pie(shares, labels=hobbies, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Мої улюблені хобі')
plt.axis('equal')
plt.show()
