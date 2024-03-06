ODD = "odd"
EVEN = "even"
PRIME = "prime"
def filter_numbers(num):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """




list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']

 filter(str.isdigit, list_of_strings)
 < filter

    0xb45eb1cc >

    In[3]: list(filter(str.isdigit, list_of_strings))
    Out[3]: ['100', '1', '50']