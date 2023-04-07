def auxiliar_list (list_a, n):
    """This method function is to recieve a list with indexes and returns a list with False in every position except for the indexes ones"""
    a_list = [False] * n
    for i in range (len(list_a)):
        a_list[list_a[i]-1] = True
    return a_list

def backtrack_caller1 (r_list, l_list, s_list, n, p, k):
    
    #Backtrack caller starts the two biggests branches of the tree one starting from the first list and
    #the other one stating the second list.                                               
    maximun_effort = 0
    value = backtrack_solver1 (r_list , l_list, s_list, n, p, k, maximun_effort,1,p*k)
    if value > maximun_effort:
        maximun_effort = value
    value = backtrack_solver1 (r_list , l_list, s_list, n, p, k, maximun_effort,2,p*k)
    if value > maximun_effort:
        maximun_effort = value
    return maximun_effort        
    
def backtrack_solver1 (r_list, l_list, s_list, n, p, k, maximun_effort, list, maximun):
    for i in range (max(1,n-k+1)):
        if list == 1:
            for j in range(i,min(i+k,n)):
                if r_list[j]:
                    s_list[j]+=1
        if list == 2:
            for j in range(i,min(i+k,n)):
                if l_list[j]:
                    s_list[j]+=1
        
        if p>1:
            
            value=backtrack_solver1 (r_list , l_list, s_list, n, p-1, k, maximun_effort,1,maximun)
            if value>maximun_effort:
                maximun_effort=value
            value=backtrack_solver1 (r_list , l_list, s_list, n, p-1, k, maximun_effort,2,maximun)
            if value>maximun_effort:
                maximun_effort=value
        if maximun_effort==maximun or maximun_effort==n:
            break
        #It only counts the maximun amount of integers it has seen on the leaves of the tree to avoid unnecesary counting and because even if it isnt unique
        #there is always a leave with the maximun
        if p==1:
            value=0
            for j in range(len(s_list)):
                if s_list[j]!=0:
                    value+=1
            if value>maximun_effort:
                maximun_effort=value
        if list == 1:
            for j in range(i,min(i+k,n)):
                if r_list[j]:
                    s_list[j]-=1
        if list == 2:
            for j in range(i,min(i+k,n)):
                if l_list[j]:
                    s_list[j]-=1
    return maximun_effort  
    
def backtrack_solver2 (r_list, l_list, s_list, n, p, k, maximun_effort, maximun):
    #The idea of this one is that for a given index and p, it only makes sense to take the best of the two lists, because it can always come back to that index
    #in another p if both lists (in that index) belonged to a maximun, and by taking only one list we reduce the amount of nodes in the tree potentially by half
    for i in range (max(1,n-k+1)):
        right=0
        left = 0
        for j in range(i,min(i+k,n)):
                if r_list[j] and s_list[j]==0:
                    right+=1
                if l_list[j] and s_list[j]==0:
                    left+=1

        if right>left:
            for j in range(i,min(i+k,n)):
                if r_list[j]:
                    s_list[j]+=1
        else:
            for j in range(i,min(i+k,n)):
                if l_list[j]:
                    s_list[j]+=1
        
        if p>1:
            value=backtrack_solver2 (r_list , l_list, s_list, n, p-1, k, maximun_effort,maximun)
            if value>maximun_effort:
                maximun_effort=value
        # This two prunes work under the logic of reaching the maximun posible answer, it can be because p (the amount of times you can take an index) and k
        #(the amount of integers we can see) are reached p*k = maximun , or because the n (amount of diferrent integers in the problem) is smaller than p*k and it is reached
        if maximun_effort==maximun or maximun_effort==n:
            break
        #It only counts the maximun amount of integers it has seen on the leaves of the tree to avoid unnecesary counting and because even if it isnt unique
        #there is always a leave with the maximun
        if p==1:
            value=0
            for j in range(len(s_list)):
                if s_list[j]!=0:
                    value+=1
            if value>maximun_effort:
                maximun_effort=value
        if right>left:
            for j in range(i,min(i+k,n)):
                if r_list[j]:
                    s_list[j]-=1
        else:
            for j in range(i,min(i+k,n)):
                if l_list[j]:
                    s_list[j]-=1
    return maximun_effort

def iterative_solution_qm(r_list, l_list, s_list, n, p, k, maximun_effort, maximun): #l=1 , r=2
    #This one is a faliure
    # It was intended to iterate only for the indexes that maximized the amount of integers on every p, wich would reduce the amount of nodes in the tree very much
    # it has a good time but sadly it has some cases where it doesnt give the correct answer
    local_maximun_amount = 0
    local_maximun =[]
    for i in range(max(n-k+1,1)):
        to_count_l =0
        to_count_r =0
        for j in range (i,min(i+k,n)):
            if(l_list[j] and s_list[j]==0):
                to_count_l+=1
            if(r_list[j] and s_list[j]==0):
                to_count_r+=1
        if to_count_l>to_count_r:
            if to_count_l == local_maximun_amount:
                local_maximun.append((1,i))
            if to_count_l > local_maximun_amount:
                local_maximun = [(1,i)]
                local_maximun_amount=to_count_l
        else:
            if to_count_r == local_maximun_amount:
                local_maximun.append((2,i))
            if to_count_r > local_maximun_amount:
                local_maximun = [(2,i)]
                local_maximun_amount = to_count_r
    for t in local_maximun:
        if(t[0]==1):
            for j in range(t[1],min(n,t[1]+k)):
                if l_list[j]:
                    s_list[j]+=1
            if p > 1:
                value = iterative_solution_qm(r_list,l_list,s_list,n,p-1,k,maximun_effort,maximun)   
                if value>maximun_effort:
                    maximun_effort=value
                if maximun_effort==maximun or maximun_effort==n:
                    break
            if p==1:
                value=0
                for j in range(len(s_list)):
                    if s_list[j]!=0:
                        value+=1
                if value>maximun_effort:
                    maximun_effort=value
            for j in range(t[1],min(n,t[1]+k)):
                if l_list[j]:
                    s_list[j]-=1

        else:
            for j in range(t[1],min(n,t[1]+k)):
                if r_list[j]:
                    s_list[j]+=1
            if p > 1:
                value = iterative_solution_qm(r_list,l_list,s_list,n,p-1,k,maximun_effort,maximun)   
                if value>maximun_effort:
                    maximun_effort=value
                if maximun_effort==maximun or maximun_effort==n:
                    break
            if p==1:
                value=0
                for j in range(len(s_list)):
                    if s_list[j]!=0:
                        value+=1
                if value>maximun_effort:
                    maximun_effort=value
            for j in range(t[1],min(n,t[1]+k)):
                if r_list[j]:
                    s_list[j]-=1
    return maximun_effort

class TTNode:
    def __init__(self, remaining_p, partial_solution,seen):
        self.remain_p = remaining_p
        self.partial_sol = partial_solution
        self.seen = seen       
        self.forming = []

def ternary_tree_solver (r_list, l_list, n, p, k):
    root = TTNode(p, [False]*n,0)
    unfinished_leaves = [root]
    future_leaves = []
    the_MAX = 0
    result = []
    forming = []
    max_amout_of_nodes=0
    aux_list = [[False]*n]
    for i in range(len(aux_list)):
        if r_list[i] or l_list[i]:
            aux_list[i] = True
    aleft_list = [0] * n
    count=0
    for i in range (n-1,-1,-1):
        if r_list[i] or l_list[i]:
            count+=1
        aleft_list[i]=count

    
    for i in range(n):
        if len(unfinished_leaves)>max_amout_of_nodes:
            max_amout_of_nodes = len(unfinished_leaves)
        for node in unfinished_leaves:
            node:TTNode
            if node.remain_p > 0 and node.seen + aleft_list[i] > the_MAX:
                if node.partial_sol[i]:
                    # if the node already saw that number, there's no need to count it, so send the node to the list of the next iteration
                    future_leaves.append(node)
                else:
                    if r_list[i]:
                        new_node = TTNode(node.remain_p - 1, list.copy(node.partial_sol), node.seen)
                        count = 0
                        for j in range (i,min(i+k,n)):
                            if r_list[j] and not new_node.partial_sol[j]:
                                new_node.partial_sol[j]=True
                                count+=1

                        new_node.seen += count
                        new_node.forming = node.forming + [(2,i)]
                        
                        if new_node.seen > the_MAX:
                            the_MAX= new_node.seen
                            result = new_node.partial_sol
                            forming = new_node.forming
                            if new_node.seen == n or new_node.seen == p*k:
                                return the_MAX, result, forming , max_amout_of_nodes

                        future_leaves.append(new_node)

                    if l_list[i]:
                        new_node = TTNode(node.remain_p - 1, list.copy(node.partial_sol), node.seen)
                        count = 0
                        for j in range (i,min(i+k,n)):
                            if l_list[j] and not new_node.partial_sol[j]:
                                new_node.partial_sol[j]=True
                                count+=1

                        new_node.seen += count
                        new_node.forming = node.forming + [(1,i)]
                        
                        if new_node.seen > the_MAX:
                            the_MAX= new_node.seen
                            result = new_node.partial_sol
                            forming = new_node.forming
                            if new_node.seen == n or new_node.seen == p*k:
                                return the_MAX, result, forming, max_amout_of_nodes

                        future_leaves.append(new_node)

                    future_leaves.append(node)

        unfinished_leaves = future_leaves
        future_leaves = []

    return the_MAX, result, forming