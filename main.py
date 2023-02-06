from dijsktra import Graph
    
def run_sample():
  edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
  ]
  
  graph = Graph(edges)
  start = 'Y'
  stop = 'X'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)
  

def main():
  run_sample()

if __name__ == "__main__":
  main()
  