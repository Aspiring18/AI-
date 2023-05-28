from queue import PriorityQueue
def cal_manhattan_dist(state, goal_state ):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            
            if tile!= 0:
                goal_post = divmod(tile-1, 3)
                distance += abs(i - goal_post[0])+ abs(j-goal_post[1])
                
    return distance            
        
class Node:
    
    def __init__(self, state, parent, action, depth, cost):
        self.state= state
        self.parent= parent
        self.action = action 
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

def a_search(initial_state, goal_state):
    explored = set()
    frontier = PriorityQueue()
    start_node = Node(initial_state, None,None, 0,0)
    frontier.put((start_node.cost, start_node))
    
    while not frontier.empty():
        current_node = frontier.get()[1]
        
        if current_node.state == goal_state:
            path = []
            while current_node.parent is not None:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
        
            return path
        explored.add(tuple(map(tuple, current_node.state)))
    
        empty_position = find_empty_position(current_node.state)
        possible_actions = find_possible_actions(empty_position)
        
        for actions, new_position in possible_actions:
            child_state= perform_actions(current_node.state, empty_position, new_position)
            child_depth = current_node.depth+1
            child_cost = child_depth + cal_manhattan_dist(child_state, goal_state)
            child_node = Node(child_state, current_node, actions, child_depth, child_cost)
         
            if tuple(map(tuple, child_state)) not in explored:
             frontier.put((child_node.cost, child_node))
    return None   

def find_empty_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return (i,j)
        
def find_possible_actions(empty_position):
    possible_actions = []
    empty_row, empty_col = empty_position
    
    if empty_row > 0:
        possible_actions.append(("Up", (empty_row - 1, empty_col)))
    if empty_row < 2:
        possible_actions.append(("Down", (empty_row +1, empty_col)))
    if empty_col>0:
        possible_actions.append(("Left", (empty_row, empty_col - 1)))
    if empty_col < 2:
        possible_actions.append(("Right", (empty_row, empty_col +1)))
    return possible_actions

def perform_actions(state, empty_position, new_position):
    empty_row, empty_col = empty_position
    new_row, new_col = new_position

    new_state = [list(row) for row in state]
    new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]

    return new_state

initial_state = []
print("Enter your initial state: ")
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)
         
goal_state = []
print("Enter your goal state: ")
for _ in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

path = a_search(initial_state, goal_state)

if path is not None :
    print("A* path: ")
    for action, state in path:
        print(action)
        for row in state: 
            print(row)
        print()
else:
    print("Goal not reachable")
         
        
    
    
     
            
        