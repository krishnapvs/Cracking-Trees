'''Given a directed graph design an algorithm to find out whether there is a route between two nodes.'''

def ispath(graph,start,end):
    a=dfs(graph,start)
    if end in a:
        return "Yes"
    else:
        return "No"

def dfs(graph,start,visited=[]):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph,i,visited)
    return visited


graph={
    1:[2,3],
    2:[3,4],
    3:[],
    4:[1,2,3]
    }

print ispath(graph,3,4)
