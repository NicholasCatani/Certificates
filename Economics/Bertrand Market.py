## Importing libraries

from scipy import optimize
from numpy import array, arange


##
def u(p,n): # utility for consumer who values good at n
    return n-p

consumer_types = arange(0.0,1.01,0.01) # 100 consumers with n varying between 0 and 1

def buy(p,n):
    if u(p,n) >= 0:
        buy = 1.0
    else:
        buy = 0.0
    return buy

def total_demand(p):            # total demand equals the sum of demands of consumers n for all consume
    demand_vector = [buy(p,n)/len(consumer_types) for n in consumer_types]
    return sum(demand_vector)



##
def profit(p1,p2,c1):
    if p1 > p2:
        profits = 0
    elif p1 == p2:
        profits = 0.5*total_demand(p1)*(p1-c1)
    else:
        profits = total_demand(p1)*(p1-c1)
    return profits

def reaction(p2,c1):
    if p2 > c1:
        reaction = c1+0.99*(p2-c1)
    else:
        reaction = c1
    return reaction


##
def vector_reaction(p,param): # vector param = (c1,c2)
    return array(p)-array([reaction(p[1],param[0]),reaction(p[0],param[1])])



######################################################### Testing

Mc = [11, 10]    ## Marginal costs
Price = [20, 20] # initial guess: p1 = p2 = 0.5
ans = optimize.fsolve(vector_reaction, Price, args = (Mc))
print(ans)


##################### Debug completed!









