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

    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(selfself, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the number of elements in the queue
    def size(self):
        return len(self.queue)


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

    # check is a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return
        else:
            # add vertex to list of Vertices
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                self.adjMat[i].append(0)

            # add a new row for the vertex
            new_row = []
            for i in range(nVert):
                new_row.append(0)
            self.adjMat.append(new_row)

    # add weighted directed edge to the graph
    def add_directed_edge(self, start, finish, weight = 1):
        # adjacency matrix rows are starting vertex
        # adjacency matrix columns are ending vertex
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to the graph
    def add_undirected_edge(self, start, finish, weight = 1):
        # adjacency matrix rows are starting vertex
        # adjacency matrix columns are ending vertex
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 and not(self.Vertices.was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create a Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the stack
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # it all the other vertices according to depth
        while not(theStack.is_empty()):
            # get an adjacentv unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            self.Vertices[i].visited = False
