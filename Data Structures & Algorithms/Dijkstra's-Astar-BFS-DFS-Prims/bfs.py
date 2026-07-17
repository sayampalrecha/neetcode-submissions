graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')


# ------------- # ------------ # --------------#

from collections import deque

def bfs_by_queue(root):
  queue = deque([root]) # atleast one element in the queue to kick start bfs
  while len(queue) > 0: # aslong as there is an element in the queue
    node = queue.popleft() # dequeue
    for child in node.children: # enqueue children
      if OK(child): # early return if problem condition met
        return FOUND(child)
      queue.append(child)
  return NOT_FOUND
