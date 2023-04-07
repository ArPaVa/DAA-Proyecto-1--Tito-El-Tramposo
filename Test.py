import GeneradorTito
import time
import SolverTito

for i in range(100):
    a,b,c,d,e = GeneradorTito.FullyAuthomaticGenerator(time.time())
    r_list = SolverTito.auxiliar_list(a,c)
    l_list = SolverTito.auxiliar_list(b,c)
    s_list = [0] * c
    print (r_list,l_list,c,d,e)
    st = time.time()
    f = SolverTito.backtrack_solver2(r_list,l_list,s_list,c,d,e,0,d*e)
    end = time.time()

    print(round(end-st,5))
    print(f)
    s_list = [0] * c

    st2 = time.time()
    g = SolverTito.ternary_tree_solver(r_list,l_list,c,d,e)
    end2 = time.time()
    print(round(end2-st2,5))
    print(g)
    if f!=g[0]:
        break
