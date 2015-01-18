#missionaries and cannibals

#Notes about the strategy to solve the problem.
#   - Search node representation: 
#       -- Current state, 
#       -- parent node, 
#       -- action performed to get from the parent to this node, 
#       -- path cost, 
#       -- depth
#
#   - Given:
#       -- Initial state
#       -- Goal state
#       -- Constraints
#       -- Boat capacity
#
#   - State representation:
#       -- # of missionaries in the left
#       -- # of cannibals in the left
#       -- Is the boat on the left?
#       -- # of missionaries in the right
#       -- # of cannibals in the right
#       -- Is the boat on the right?
#
#   - Needs:
#       -- A function to check the validity of the solution
#           --- The number of cannibals is not more than the number of missionaries in any side.
#           --- The boat is either left or right, not both in the same time, or not existant.
#           --- 
#       -- Enumerate the list of all possible actions (This is how to expand the tree)
#           --- 1 C, 1 M
#           --- 2 C
#           --- 2 M
#           --- 1 C
#           --- 1 M
#
#       -- Main game loop - FIFO search
#           --- Start from the initial state, put it in the fring.
#           --- Check if this current state is the goal state or not
#           --- Apply all actions to this state to generate all possible child states
#           --- Disregard all unvalid child states
#           --- Remove the current state (initial state in this case) from the fringe and put it in the hash table of the visited nodes.
#           --- Put the rest of these childeren states in the fring.
#           --- Repeat this process till either you reach a goal or the fringe is empty
#           --- 

actions_list = ["1M1C","1M","1C","2M","2C"]

def expand_states (current_state):
    actions_list = ["1M1C","1M","1C","2M","2C"]
    states_list = []
    if current_state[2] == True: #The boat is on the right, and will go left
        #print "From right to left"
        for action in actions_list:
            if action == "1M1C":
                new_state = current_state [:]
                new_state[0] -= 1
                new_state[1] -= 1
                new_state[3] += 1
                new_state[4] += 1
                new_state[5] = True
                new_state[2] = False
                states_list.append(new_state)
            elif action == "1M":
                new_state = current_state [:]
                new_state[0] -= 1
                #new_state[1] -= 1
                new_state[3] += 1
                #new_state[4] += 1
                new_state[5] = True
                new_state[2] = False
                states_list.append(new_state)
            elif action == "2M":
                new_state = current_state [:]
                new_state[0] -= 2
                #new_state[1] -= 1
                new_state[3] += 2
                #new_state[4] += 1
                new_state[5] = True
                new_state[2] = False
                states_list.append(new_state)            
                
            elif action == "2C":
                new_state = current_state [:]
                #new_state[0] -= 2
                new_state[1] -= 2
                #new_state[3] += 2
                new_state[4] += 2
                new_state[5] = True
                new_state[2] = False
                states_list.append(new_state)            
                
            elif action == "1C":
                new_state = current_state [:]
                #new_state[0] -= 2
                new_state[1] -= 1
                #new_state[3] += 2
                new_state[4] += 1
                new_state[5] = True
                new_state[2] = False
                states_list.append(new_state)            
                
    elif current_state[5] == True: #The boat is on the right, and will go left
        #print "From left to right"
        for action in actions_list:
            if action == "1M1C":
                new_state = current_state [:]
                new_state[0] += 1
                new_state[1] += 1
                new_state[3] -= 1
                new_state[4] -= 1
                new_state[2] = True
                new_state[5] = False
                states_list.append(new_state)
            elif action == "1M":
                new_state = current_state [:]
                new_state[0] += 1
                #new_state[1] -= 1
                new_state[3] -= 1
                #new_state[4] += 1
                new_state[2] = True
                new_state[5] = False
                states_list.append(new_state)
            elif action == "2M":
                new_state = current_state [:]
                new_state[0] += 2
                #new_state[1] -= 1
                new_state[3] -= 2
                #new_state[4] += 1
                new_state[2] = True
                new_state[5] = False
                states_list.append(new_state)            
                
            elif action == "2C":
                new_state = current_state [:]
                #new_state[0] -= 2
                new_state[1] += 2
                #new_state[3] += 2
                new_state[4] -= 2
                new_state[2] = True
                new_state[5] = False
                states_list.append(new_state)            
                
            elif action == "1C":
                new_state = current_state [:]
                #new_state[0] -= 2
                new_state[1] += 1
                #new_state[3] += 2
                new_state[4] -= 1
                new_state[2] = True
                new_state[5] = False
                states_list.append(new_state)            
    return states_list    


def solution_validity (states_list): #Check on the constraint we have
    valid_states = []
    for state in states_list:
        if ((state[0] == 0) or (state[0] >= state[1])) and ((state[3] == 0) or (state[3] >= state[4])) and (state[3] in range(0,4)) and (state[4] in range(0,4)) and (state[0] in range(0,4)) and (state[1] in range(0,4)):
            valid_states.append(state)
    return valid_states

def check_visited (state_list,visited_list):
    final_states = []    
    for state in state_list:
        if state not in visited_list:
            final_states.append(state)
            
    return final_states

def generate_states (current_state,visited_states, fringe):
    new_states = expand_states (current_state)
    valid_states = solution_validity(new_states)
    final_states = check_visited(valid_states, visited_states)
    very_final = []
    for state in final_states:
        if state not in fringe:
            very_final.append(state)
    return very_final

def pathTo (goal_state, node_list):
    path = [goal_state]
    for node in node_list:
        if node[0] == goal_state:
            node0 = node[:]
            path.append(node0[1])
            while(node0[1] != None):
                for nodex in node_list:
                    if nodex[0] == node0[1]:
                        path.append(nodex[1])
                        node0 = nodex[:]
                        continue
            break
        
    for point in path:
        print point    
    pass

def main_loop(current_state = [3,3,True,0,0,False], goal_state = [0,0,False,3,3,True]):
    fringe = [current_state]
    path = [current_state]
    explored_states = []
    current_node = [current_state,None] 
    node_list = [current_node]
    while(True):
        if len(fringe) == 0:
            print "No solution found :'("
            return False
        if fringe[0] == goal_state:
            print "A path to the light has been found :)"
            pathTo(goal_state, node_list)
            return path         
        explored_states.append(fringe[0])
        generates_states =  generate_states(fringe[0], explored_states, fringe)
        
        for state in generates_states:
            node_list.append([state,fringe[0]])
        
        del(fringe[0])
        
        fringe += generates_states
        
        #print "whole fringe = ", fringe
        
    pass

main_loop()