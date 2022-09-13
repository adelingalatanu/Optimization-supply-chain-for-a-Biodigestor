from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Define the model
model = LpProblem(name="optimal-mix", sense=LpMaximize)

# Define the data

a1A = 3
a2A = 1
a3A = 2
a4A = 0
a5A = 0

a1B = 2
a2B = 2
a3B = 0
a4B = 3
a5B = 0

a1C = 1
a2C = 3
a3C = 0
a4C = 0
a5C = 2

b1 = 120
b2 = 80
b3 = 96
b4 = 102
b5 = 40

cA = 840
cB = 1120
cC = 1200

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 4)}

# Add constraints
model += (a1A * x[1] + a1B * x[2] + a1C * x[3] <= b1)
model += (a2A * x[1] + a2B * x[2] + a2C * x[3] <= b2)
model += (a3A * x[1] + a3B * x[2] + a3C * x[3] <= b3)
model += (a4A * x[1] + a4B * x[2] + a4C * x[3] <= b4)
model += (a5A * x[1] + a5B * x[2] + a5C * x[3] <= b5)

# Set the objective
model += cA*x[1] + cB*x[2] + cC*x[3]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
