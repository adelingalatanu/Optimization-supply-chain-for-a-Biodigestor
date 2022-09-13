from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

# Define the problem
model = LpProblem(name="stock", sense=LpMinimize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 4)}
y = {j: LpVariable(name=f"y{j}", lowBound=0) for j in range(1, 4)}
w = {k: LpVariable(name=f"w{k}", lowBound=0) for k in range(1, 4)}

# Data
A = 110
B = 60

c = 300
v = 330

s = 10

d1 = 100
d2 = 130
d3 = 150

# Add the constraints
model += (x[1] <= A)
model += (x[2] <= A)
model += (x[3] <= A)

model += (y[1] <= B)
model += (y[2] <= B)
model += (y[3] <= B)

model += (w[1] - 0 - x[1] + d1 == 0)
model += (w[2] - w[1] - x[2] + d2 == 0)
model += (w[3] - w[2] - x[3] + d3 == 0)

# Set the objective 
model += c*x[1] + v*y[1]+ s*w[1] + c*x[2] + v*y[2] + s*w[2] + c*x[3] + v*y[3] + s*w[3]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
	print(f"{var.name}: {var.value()}")

for var in y.values():
	print(f"{var.name}: {var.value()}")

for var in w.values():
	print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
	print(f"{name}: {constraint.value()}")

