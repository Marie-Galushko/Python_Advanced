from chess.main import is_correct_position

from random import randint


# def generate_list():
#     random_list = []
#
#     for _ in range(8):
#         lst = [randint(0, 7), randint(0, 7)]
#         random_list.append(lst)
#
#     return random_list



def test_chess():
    correct_pos = []
    correct_index = 0

    while correct_index != 4:
        pos = [[randint(0, 7), randint(0, 7)] for _ in range(8)]

        if is_correct_position(pos):
            correct_index += 1
            correct_pos.append(pos)


    return correct_pos


res = test_chess()
for i in res:
    print(i)