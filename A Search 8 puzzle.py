
# A* Search for 8 Puzzle

import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            distance += abs(i//3 - goal_pos//3)
            distance += abs(i%3 - goal_pos%3)

    return distance


def astar(start):

    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        zero = state.index(0)

        for move in [-3, 3, -1, 1]:

            new_pos = zero + move

            if 0 <= new_pos < 9:
                if abs(zero//3 - new_pos//3) + \
                   abs(zero%3 - new_pos%3) == 1:

                    new = list(state)
                    new[zero], new[new_pos] = \
                        new[new_pos], new[zero]

                    new = tuple(new)

                    if new not in visited:
                        heapq.heappush(
                            pq, (g+1+heuristic(new),
                                 g+1, new, path+[state])
                        )

    return None


result = astar(start)

for state in result:
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()
