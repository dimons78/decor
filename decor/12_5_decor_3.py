# Применить написанный логгер к приложению из любого предыдущего д/з
# (к задаче №4 из ДЗ по Генераторам)

import os
import datetime



def logger(old_function):


    def new_function(*args, **kwargs):

        start = str(datetime.datetime.now())

        result = old_function(*args, **kwargs)

        with open('flat_gen.log', 'a+', encoding='utf-8') as file:
            file.write(start + '\n')
            file.write(old_function.__name__ + '\n')
            file.write(f'{args}, {kwargs}\n')
            file.write(f'{result}\n')

        return result

    return new_function


def test_1():

    @logger
    def flat_generator(list_of_list):

        for item in list_of_list:
            if isinstance(item, list):
                for subitem in flat_generator(item):
                    yield subitem
            else:
                yield item

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    flat_generator(list_of_lists_2)


if __name__ == '__main__':
    test_1()
