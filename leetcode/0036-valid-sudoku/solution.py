def rev_matr(sub):
    return [list(row) for row in zip(*sub)]


def check_matr(matr) -> bool:
    for row in matr:
        filtered = [x for x in row if x != "."]
        if len(filtered) != len(set(filtered)):
            return False
    return True


def check_unique(matr) -> bool:
    filtered = [x for row in matr for x in row if x != "."]
    return len(filtered) == len(set(filtered))


def check_board(board) -> bool:
    return check_matr(board) and check_matr(rev_matr(board))


class Solution:
    def isValidSudoku(self, board: list[list[str]]):
        res_sub, res_rev = True, True

        if not check_board(board):
            return False

        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                sub = [row[n : 3 + n] for row in board[m : 3 + m]]
                rev = [list(row) for row in zip(*sub)]

                res_sub = check_matr(sub)
                res_rev = check_matr(rev)

                if not (res_rev and res_sub and check_unique(sub)):
                    return False

        return True
