
import heapq

# Represents a chess board for NQueens
class NQueensProblem:
    def __init__(self, n, goal_state=None):
        self.init_state = tuple([-1] * n)
        self.goal_state = goal_state
        self.n = n

    def actions(self, state):
        if state[-1] != -1:  # if all columns are filled
            return []  # then no valid actions exist

        valid_actions = list(range(self.n))
        col = state.index(-1)  # index of leftmost unfilled column
        for row in range(self.n):
            for c, r in enumerate(state[:col]):
                if self.conflict(row, col, r, c) and row in valid_actions:
                    valid_actions.remove(row)
        return valid_actions

    def result(self, state, action):
        col = state.index(-1)  # leftmost empty column
        new = list(state[:])
        new[col] = action  # queen's location on that column
        return tuple(new)

    def goal_test(self, state):
        try:
            if state[-1] == -1:  # if there is an empty column
                return False  # then, state is not a goal state
        except IndexError:  # catch exception
            return True
        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    return False
        return True

    def conflict(self, row1, col1, row2, col2):
        return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

    def g(self, cost, from_state, action, to_state):
        return cost + 1

    def h(self, state):
        conflicts = 0
        for col1, row1 in enumerate(state):
            for col2, row2 in enumerate(state[col1 + 1:], start=col1 + 1):
                if self.conflict(row1, col1, row2, col2):  # if conflict, add 2 to the current conflict value
                    conflicts += 2
        return conflicts


class Node:  # Represents a node in a search tree
    def __init__(self, state, parent=None, action=None,
                 path_cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):  # Returns a list of child nodes
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):  # Returns the child node from executing the given action
        pass

    def solution(self):  # Returns actions from this node to the root node
        if self.state is None:
            return None
        return [node.action for node in self.path()[1:]]

    def path(self):  # Returns list of nodes from this node to the root node
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return "<Node {}(g={}, h={})>".format(self.state, self.path_cost, self.heuristic)

    def __lt__(self, other):
        pass


class NodeA(Node):  # A* Node
    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic=0):
        super().__init__(state, parent, action, path_cost, heuristic)

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = NodeA(next_state, self, action,
                          problem.g(self.path_cost, self.state,
                                    action, next_state),
                          problem.h(next_state))
        return next_node

    def __lt__(self, other):
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)


class NodeU(Node):  # Uniform-Cost Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        super().__init__(state, parent, action, path_cost)

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = NodeU(next_state, self, action,
                          problem.g(self.path_cost, self.state,
                                    action, next_state))
        return next_node

    def __lt__(self, other):
        return self.path_cost < other.path_cost



def uniform_cost_search(problem):
    node = NodeU(problem.init_state)
    return optimal_search(node, problem)


def a_star_search(problem):
    node = NodeA(problem.init_state, heuristic=problem.h(problem.init_state))
    return optimal_search(node, problem)


def optimal_search(node, problem):
    frontier = [node]
    heapq.heapify(frontier)
    expanded = [problem.init_state]
    while frontier:
        current = heapq.heappop(frontier)
        if problem.goal_test(current.state):  # goal has been found
            return current
        if current in expanded:
            continue
        children = current.expand(problem)  # expand child
        expanded.append(current)
        for i in children:
            if i not in expanded:
                heapq.heappush(frontier, i)
    return Node(0, None, None)  # if frontier is empty, no solution

board = NQueensProblem(8)  # A* can solve up to around 15 queens fast
a_star = a_star_search(board)
uniform_cost = uniform_cost_search(board)
print('A*: ' + str(a_star.solution()))
print('Uniform-Cost: ' + str(uniform_cost.solution()))