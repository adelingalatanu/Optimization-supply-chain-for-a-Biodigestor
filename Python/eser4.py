from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Define the problem
model = LpProblem(name="cavalli", sense=LpMaximize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 5)}

# Data
q1 = 3
q2 = 4
q3 = 5
q4 = 6

B = 57

# Add the constraints
model += (x[1] +x[2] + x[3] + x[4] <=B)

# Set the objective
model += q1*x[1] + q2*x[2] + q3*x[3] + q4*x[4]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
	print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
	print(f"{name}: {constraint.value()}")

