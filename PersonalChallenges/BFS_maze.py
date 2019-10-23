#Maze navigation using BFS. 1's are walls, 2 is start and 3 is end.
#Aleksandr Kovalev 10/16/2019
 
def print_maze(maze):
 for row in maze:
   print(row)
 
maze = [[2,0,0,0,0,1],
        [0,1,0,1,0,0],
        [0,1,1,1,1,0],
        [0,0,1,0,0,0],
        [1,0,1,0,1,0],
        [1,0,1,0,3,1]]
 
print_maze(maze)
print("\n")
 
visited = [[0,0,0,0,0,1],
          [0,1,0,1,0,0],
          [0,1,1,1,1,0],
          [0,0,1,0,0,0],
          [1,0,1,0,1,0],
          [1,0,1,0,3,1]]
 
y, x = 0, 0
visited[y][x] = 2
move_count = 0
end = False
 
def solve(maze, visited, y, x):
 
  yq = []
  xq = []
  moves = 0
  path_options = 0
  path_options_left = 1
 
  def print_q(yq, xq):
    print("y: ", yq)
    print("x: ", xq)
 
  yq.append(y)
  xq.append(x)
 
  while len(yq) > 0:
 
    print(y, x)
    print_q(yq, xq)
    y = yq.pop(0) #pop last would make this code into DFS
    x = xq.pop(0)
    print(y, x)
 
    if maze[y][x] == 3:
      break
 
    if maze[y - 1][x] == 0 and visited[y - 1][x] == 0 and y != 0: #safety protect from back indexing
      yq.append(y - 1)
      xq.append(x)
      visited[y - 1][x] = 2
      path_options += 1
  
    if  x < len(maze)-1 and maze[y][x + 1] == 0 and visited[y][x + 1] == 0:  #protect from out of range
      yq.append(y)
      xq.append(x + 1)
      visited[y][x + 1] = 2
      path_options += 1
  
    if y < len(maze)-1 and maze[y + 1][x] == 0 and visited[y + 1][x] == 0:  #protect from out of range
      yq.append(y + 1)
      xq.append(x)
      visited[y + 1][x] = 2
      path_options += 1
  
    if maze[y][x - 1] == 0 and visited[y][x - 1] == 0 and x != 0: #safety protect from back indexing
      yq.append(y)
      xq.append(x - 1)
      visited[y][x - 1] = 2
      path_options += 1
 
    print("paths options found: ", path_options)
    print("path options left: ", path_options_left)
    path_options_left -= 1
    if path_options_left == 0:
      path_options_left = path_options
      path_options = 0
      moves += 1
 
    print("move: ", moves)
    print("\n")
 
 
solve(maze, visited, y, x)
print_maze(visited)
 
 

