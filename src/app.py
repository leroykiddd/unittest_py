def my_sort(array):
    """
    Сортировка пузырьком
    Функция создана в целях изучения unit-тестирования в python
    """
    length = len(array)
    for i in range(length):
        for k in range(length):
            if array[i] < array[k]:
                array[i], array[k] = array[k], array[i]

    return array