import matplotlib.pyplot as plt
from functions import num_of_letters

def plot_letter_counts(letter_counts):
    letters=list(letter_counts.keys())
    counts=list(letter_counts.values())

    plt.figure(figsize=(10,5))
    plt.bar(letters,counts,color='skyblue')
    plt.xlabel('Litery')
    plt.ylabel('Ilosc w tekscie')
    plt.title('Czestotliwosc wystepowania liter w tekscie')
    plt.grid(axis='y',linestyle='--')
    plt.show()


text='Maciek'
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result=num_of_letters(text,letters)
print(result)
plot_letter_counts(result)

