#HW 5

# Collaboration Statement:
#
########################################

# ---Copy your code from labs 9 and 10 here (you can remove their comments)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        return self.top == None
        # write your code here

    def __len__(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp
        # write your code here

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value
        # write your code here


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head, self.tail, out))

    __repr__ = __str__

    def isEmpty(self):
        # write your code here
        return self.count == 0

    def __len__(self):
        # write your code here
        return self.count

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.tail = new_node
            self.head = new_node
            self.count += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
        # write your code here

    def dequeue(self):
        # write your code here
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp = self.head
            if self.count == 1:
                self.head = None
                self.tail = None
                self.count -= 1
                return temp.value
            else:
                self.head = self.head.next
                self.count -= 1
                return temp.value



#----- HW5 Graph code     
class Graph:

    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:self.vertList = graph_repr

    def addVertex(self,key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self,frm,to,cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))
        return self.vertList

    def bfs(self, start):
    	# Your code starts here
        visited = []
        qu = Queue()
        qu.enqueue(start)
        visited.append(start)  #add the start node to visited and add to queue

        while qu.isEmpty() != True: #start loop until the queue is empty
            start = qu.dequeue()
            self.vertList[start] = sorted(self.vertList[start]) #put them in alphabetical order
            for i in self.vertList[start]:
                if i[0] not in visited: #if the node hasn't been visted, then add to queue and visit it
                    qu.enqueue(i[0])
                    visited.append(i[0])
        return visited #return the list of visited nodes



    def dfs(self, start):
    	# Your code starts here
        visited = []
        stack = Stack()
        stack.push(start) #add the starting node to the stack and append it to visited
        visited.append(start)
        key = "not triggered"

        while True:

            self.vertList[start] = sorted(self.vertList[start]) #sort the nodes so they're in alphabetical order
            for i in self.vertList[start]:
                if i[0] not in visited: #if the node hasn't been visited add to stack and append to visited
                    stack.push(i[0])
                    visited.append(i[0])
                    key = "triggered" #i created this key and when it becomes triggered the loop won't draw from the stack
                    start = i[0] #now we visit the next nodes children
                    break

            if key != "triggered": #if the key isn't changed to triggered then the code will draw from the stack
                start = stack.pop()
                if start == "Stack is empty": #once the stack is empty it will break the loop
                    break
            key = "not triggered"

        return visited


    ### EXTRA CREDIT, uncomment method definition if submitting extra credit
    
    def dijkstra(self,start):
        # Your code starts here
        shortest_distance = {}
        final_answer = {}
        unExplored = self.vertList
        infinity = 99999
        for node in unExplored:
            shortest_distance[node] = infinity #make all of the distance infinity
        shortest_distance[start] = 0 #the starting point can be made zero

        while unExplored:
            minNode = None
            for node in unExplored:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node

            for neighbors, weight in self.vertList[minNode]:
                if weight + shortest_distance[minNode] < shortest_distance[neighbors]:
                    shortest_distance[neighbors] = weight + shortest_distance[minNode] #update the weight if the new weight is less
            unExplored.pop(minNode)
        for i in shortest_distance: #remove all the nodes that are infinity because they were not visited
            if shortest_distance[i] != infinity:
                final_answer[i] = shortest_distance[i]

        return final_answer

