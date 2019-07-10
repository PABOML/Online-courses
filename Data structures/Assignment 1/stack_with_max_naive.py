#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        return self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()
    aux_stack = []
    
    num_queries = int(sys.stdin.readline())
    
    
    
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
            if not aux_stack or int(query[1]) >= aux_stack[-1]:
                aux_stack.append(int(query[1]))
                
        elif query[0] == "pop":
            a=stack.Pop()
            if a == aux_stack[-1]:
                aux_stack.pop()
                
        elif query[0] == "max":
            print(aux_stack[-1])
        else:
            assert(0)
            
    '''            
    for i in range(0,len(query)):
        #query = sys.stdin.readline().split()
        #print(query)
        #query = sys.stdin.split()
        if query[i] == "push":
            stack.Push(int(query[i+1]))
            
            if not aux_stack or int(query[i+1]) >= aux_stack[-1]:
                aux_stack.append(int(query[i+1]))
        
        elif query[i] == "pop":
            a = stack.Pop()
            if a == aux_stack[-1]:
                #print(aux_stack)
                aux_stack.pop()
        elif query[i] == "max":
            #print(stack.Max())
            print(aux_stack[-1])
        else:
            assert(len(query))
        #print(aux_stack)
    '''