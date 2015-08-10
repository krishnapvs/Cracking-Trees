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

def ispathImproved(graph,start,end):
    q=[start]
    visited=[]
    while q:
        temp=q.pop(0)
        visited.append(temp)
        if (end in visited) or (end in q):
            return "Yes"
        for i in graph[temp]:
            q.append(i)
    return "No"

graph={
    1:[2,3],
    2:[3,4],
    3:[],
    4:[1,2,3]
    }

#print ispath(graph,3,4)
print ispathImproved(graph,3,4)
