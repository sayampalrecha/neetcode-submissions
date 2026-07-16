def is_valid_state(state):
  # check is it is a valid solution
  
  return True

def get_candidates(state):
  return []

# recursive function that calls the earlier one and checks the search
# makes a deep copy
def search(state, solutions):
  if is_valid_state(state):
    solutions.append(state.copy())
    # return

  for candidates in get_candidates(state):
    state.add(candidate)
    search(state, solutions)
    state.remove(candidate)

# this is what the leetcode problem want us to write 
def solve():
  solutions = []
  state = set()
  search(state, solutions)
  return solutions
  
