n = 12
k = 2
numbers = []

for i in range(1, n + 1):
    numbers.append(i)
numbers *= 2

#copy_numbers = numbers
delete_index = 1 #индекс элемента, который будем удалять

while len(numbers) > 2: #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    next_died = numbers[delete_index]
    next_killer = numbers[delete_index + 1] #само число, после которого далее следует удаление #9
    #print(next_died)

    copy_numbers = [i for i in numbers if i != next_died]
    numbers = copy_numbers
    #print(numbers)
    #print()

    delete_index = numbers.index(next_killer) + 1

print(numbers[0])    
    