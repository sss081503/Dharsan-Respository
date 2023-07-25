#  File: TopoSort.py

#  Description: has_cycle and toposort functions

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name: Sashi A

#  Partner UT EID: sa55465

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/27/22

#  Date Last Modified:





import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def is_inside(self, label):
        if label in self.stack:
            return True
        else:
            return False


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    def delete(self, label):
        vertex = self.get_index(label)
        for row in range(len(self.adjMat)):
            del (self.adjMat[row][vertex])
        del (self.adjMat[vertex])
        del (self.Vertices[vertex])


    # do the breadth first search in a graph
    def bfs(self, v):
        # 0. creating Queue
        frontierqueue = Queue()

        # currentv = self.Vertices[v]
        currentv = v
        frontierqueue.enqueue(v)
        discoveredset = []
        (self.Vertices[v]).visited = True

        # 2. Visit an adjacent unvisited vertex (if there is one) in
        # order from the current vertex. Mark it visited and insert
        # it into the queue.
        while (not frontierqueue.is_empty()):

            currentv = frontierqueue.dequeue()
            self.Vertices[currentv].visited = True

            idx = self.Vertices[currentv].get_label()

            lst = self.get_neighbors(idx)
            print(idx)  # PRINTS the bfs traversal

            discoveredset.append(currentv)

            for adjVertex in lst:

                if adjVertex not in discoveredset:
                    discoveredset.append(adjVertex)
                    frontierqueue.enqueue(adjVertex)

        # the Queue is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return

        # determine if a directed graph has a cycle
        # this function should return a boolean and not print the result

    def has_cycle(self):
        num_Vert = len(self.Vertices)
        if num_Vert > 0:

            theStack = Stack()  # creates Stacks for each vertex
            idx = 0
            self.Vertices[idx].visited = True  # marks each vertex as visited as it iterates along the list of verticies
            theStack.push(idx)

            while theStack.is_empty() == False:  # follows format of dfs, but done on each vertex to see if it is possible to come back to starting vertex for each.
                adj_v = self.get_adj_unvisited_vertex(theStack.peek())

                if adj_v == -1:
                    adj_v = theStack.pop()

                else:
                    self.Vertices[adj_v].visited = True
                    theStack.push(adj_v)

                    # want to see if next vertex has path to another vertex
                    for j in range(num_Vert):
                        if self.adjMat[adj_v][j] != 0:
                            if j in theStack.stack:
                                return True
            return False
        else:
            return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        theQueue = Queue()
        num_vert = len(self.Vertices)
        deg = {}

        for vert in range(num_vert):
            count = 0
            for k in range(num_vert):
                if self.adjMat[k][vert] > 0:
                    count = count + 1
            deg[self.Vertices[vert]] = count

        while len(deg) > 0:
            verts = []

            for degree in deg:
                if deg[degree] == 0:
                    verts.append(degree)
            q_list = []

            for v in verts:
                index = self.Vertices.index(v)
                for vert in range(num_vert):
                    if self.adjMat[index][vert] > 0:
                        deg[self.Vertices[vert]] -= 1
                deg.pop(v)
                q_list.append(v.label)
            q_list.sort()

            for k in q_list:
                theQueue.enqueue(k)
        q_vert = []

        while theQueue.is_empty() == False:
            q_vert.append(theQueue.dequeue())

        return q_vert








def main():
    # create the Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        vert = line.strip()
        theGraph.add_vertex(vert)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])
        theGraph.add_directed_edge(start, finish)

    # read the starting vertex for dfs and bfs
    # line = sys.stdin.readline()
    # start_vertex = line.strip()

    # get the index of the starting vertex
    # start_index = theGraph.get_index(start_vertex)

    # do the depth first search
    # print("Depth First Search")
    # cities.dfs(start_index)
    # print()

    # test if a directed graph has a cycle
    if theGraph.has_cycle() == True:
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")
        print()
        print("List of vertices after toposort")
        print(theGraph.toposort())


if __name__ == "__main__":
    main()
