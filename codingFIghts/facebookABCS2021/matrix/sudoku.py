
    
def isValidSudoku( board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                #debes de cambiar de posicion j y element porque sino va a ser lo mismo que (i, element ) y seria incorrecto
                res += [(i, element), ( j, element), (i // 3, j // 3, element)]

    print(len(res))
    print("-----")
    print(len(set(res)))
    
    return len(res) == len(set(res))
        
    
    
    #solucion larga pero valida
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #1. checo rows, despues columns, despues grid
        #puedo llenar un dicc que se reinicilice en cada row o column y contar apariciones
        #rows

        for i in range(9):
            dicc = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, ".":0 }
            for j in range(9):
                if dicc[board[i][j]] == 0:
                    dicc[board[i][j]] += 1
                elif dicc[board[i][j]] != 0 and board[i][j] != ".":
                    return False
        
        for i in range(9):
            dicc = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, ".":0 }
            for j in range(9):
                if dicc[board[j][i]] == 0:
                    dicc[board[j][i]] += 1
                elif dicc[board[j][i]] != 0 and board[j][i] != ".":
                    return False
                else:
                    dicc[board[j][i]] += 1

        #el problema es que asi se esta haciendo en diagonal
        for k in range(0,9, 3):
            dicc = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, ".":0 }
            for i in range(0,3):
                for j in range(0,3):
                    if dicc[board[i][j+k]] == 0:
                        dicc[board[i][j+k]] += 1
                    elif dicc[board[i][j+k]] != 0 and board[i][j+k] != ".":
                        return False
        for k in range(0,9, 3):
            dicc = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, ".":0 }
            for i in range(3,6):
                for j in range(0,3):
                    if dicc[board[i][j+k]] == 0:
                        dicc[board[i][j+k]] += 1
                    elif dicc[board[i][j+k]] != 0 and board[i][j+k] != ".":
                        return False
        
        for k in range(0,9, 3):
            dicc = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, ".":0 }
            for i in range(6,9):
                for j in range(0,3):
                    if dicc[board[i][j+k]] == 0:
                        dicc[board[i][j+k]] += 1
                    elif dicc[board[i][j+k]] != 0 and board[i][j+k] != ".":
                        return False
                


        return True
        
print(isValidSudoku([["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]))