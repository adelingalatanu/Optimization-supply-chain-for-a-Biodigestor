from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# Add the constraints to the model
model += (2 * x + y <= 20)
model += (4 * x - 5 * y >= -10)
model += (-x + 2 * y >= -2)
model += (-x + 5* y == 15)

# Add the objective function to the model
obj_func = x + 2 * y
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
	print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
	print(f"{name}: {constraint.value()}")
	