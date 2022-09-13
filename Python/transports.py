# Import PuLP modeler functions
from pulp import *

# Creates a list of all the supply nodes
Origine = ["1", "2", "3", "4", "5", "6", "7", "8"]
supply = {"1": 30, "2": 40, "3": 20, "4": 35, "5": 40, "6": 30, "7": 25, "8": 50}

# Creates a list of all the demand nodes
Destinazioni = ["1", "2", "3", "4"]
Domanda = {
	"1": 70,
	"2": 70,
	"3": 50,
	"4": 80,
}

# Creates a list of costs of each transportation path
costs = [# Destinazioni
     # 1   2   3   4
     [20, 25, 30, 28], #1 Origini
     [15, 12, 32, 26], #2
     [18, 41, 36, 37], #3
     [32, 23, 35, 20], #4
     [31, 40, 19, 38], #5
     [33, 22, 34, 21], #6
     [25, 29, 26, 27], #7
     [30, 24, 39, 28], #8
]

# The cost data is made into a dictionary
costs = makeDict([Origine, Destinazioni], costs, 0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Trasporto_a_cost_minimo", LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(i, j) for i in Origine for j in Destinazioni]

# A dictionary called 'Vars' is created to contain the referenced variables (the routes)
vars = LpVariable.dicts("Route", (Origine, Destinazioni), 0, None, LpInteger)

# The objective function is added to 'prob' first
prob += (
	lpSum([vars[i][j] * costs[i][j] for (i, j) in Routes]),
	"Sum_of_Transporting_Costs",
	)

for i in Origine:
    prob += (
        lpSum([vars[i][j] for j in Destinazioni]) == supply[i],
        "Sum_of_Products_out_of_Origini_%s" % i,
    )

# The demand minimum constraints are added to prob for each demand node (bar)
for j in Destinazioni:
    prob += (
        lpSum([vars[i][j] for i in Origine]) == Domanda[j],
        "Sum_of_Products_into_Destinazionir%s" % j,
    )

        
prob.writeLP("Trasporto_a_cost_minimo.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
