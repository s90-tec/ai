
# Alpha-Beta Pruning

def minimax(depth, index, maximizing, values, alpha, beta):

    if depth == 3:
        return values[index]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            val = minimax(depth+1, index*2+i,
                          False, values, alpha, beta)

            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minimax(depth+1, index*2+i,
                          True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = minimax(0, 0, True, values,
                 float('-inf'), float('inf'))

print("Optimal value:", result)
