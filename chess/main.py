pos_queen = ((0, 0), (1, 4), (2, 7), (3, 5),
             (4, 2), (5, 6), (6, 1), (7, 3))

pos_queen_bad = ((0, 0), (1, 1), (2, 2), (3, 3),
                 (4, 4), (5, 5), (6, 6), (7, 7))


def is_correct_position(pos):
    for i in range(8):
        for j in range(i + 1, 7):
            if pos[i][1] == pos[j][1] or \
                    pos[i][0] == pos[j][0] or \
                    pos[i][0] - pos[j][0] == pos[i][1] - pos[j][1]:
                return False

        return True



