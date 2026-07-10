n = int(input())
k = int(input())
numbers = []

for i in range(1, n + 1):
    numbers.append(i)
numbers *= k

delete_index = k - 1 #индекс элемента, который будем удалять

while len(numbers) > k: #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    next_died = numbers[delete_index] #Находим число, которое будем удалять
    next_killer = numbers[delete_index + 1] #Число, которое стоит после удаленного и с которого будем начинать последующий отсчет

    numbers = [i for i in numbers if i != next_died] #Создаем новый список без удаленного числа
    delete_index = numbers.index(next_killer) + (k-1) #Отсчитываем в новом списке индекс, по которомо будет стоять следующее удаленное число

print(numbers[0])
    
    