from dijsktra import Graph
    
def ticket_cost(x,y):
  edges = [
    ('Vanc', 'Bost', 561),
    ('Vanc', 'New', 603),
    ('Vanc', 'LasV', 327),
    ('LosA', 'LasV', 169),
    ('LosA', 'SLC', 222),
    ('LosA', 'FtLa', 676),
    ('LasV', 'SLC', 69),
    ('LasV', 'FtLa', 99),
    ('LasV', 'New', 617),
    ('LasV', 'Chic', 254),
    ('Minn', 'New', 237),
    ('Chic', 'New', 226),
    ('FtLa', 'New', 299),
    ('FtLa', 'Bost', 465),
    ('New', 'Bost', 133),
  ]
  
  graph = Graph(edges)
  start = x
  stop = y
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)
  print ("You will have", len(path) - 2, "layovers on your flight." )
  count = 0
  distance = 0
  while count < len(path)-1:
    distance = distance + graph.weights[path[count],path[count+1]]
    count +=1
  print("You will fly", distance, "units")

def main():
  ticket_cost('LosA','Chic')

if __name__ == "__main__":
  main()
  