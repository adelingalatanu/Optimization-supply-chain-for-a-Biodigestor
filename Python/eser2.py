from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

# Define the model
model = LpProblem(name="diet",sense=LpMinimize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 8)}

# Data

a11 = 11.5
a12 = 3.15
a13 = 8
a14 = 18.5
a15 = 2.1
a16 = 12.0
a17 = 9

a21 = 72.7
a22 = 4.85
a23 = 3.8
a24 = 0.5
a25 = 0
a26 = 68
a27 = 74

a31 = 1.5
a32 = 1.55
a33 = 11
a34 = 19
a35 = 0.1
a36 = 6
a37 = 1

l1 = 25
l2 = 15
l3 = 10

u1 = 35
u2 = 25
u3 = 20

c1 = 4
c2 = 4
c3 = 15
c4 = 22.5
c5 = 3
c6 = 1
c7 = 5

# Add constraints

model += (a11*x[1] + a12*x[2] + a13*x[3] + a14*x[4] + a15*x[5] + a16*x[6] + a17*x[7] >= l1)
model += (a21*x[1] + a22*x[2] + a23*x[3] + a24*x[4] + a25*x[5] + a26*x[6] + a27*x[7] >= l2)
model += (a31*x[1] + a32*x[2] + a33*x[3] + a34*x[4] + a35*x[5] + a36*x[6] + a37*x[7] >= l3)

model += (a11*x[1] + a12*x[2] + a13*x[3] + a14*x[4] + a15*x[5] + a16*x[6] + a17*x[7] <= u1)
model += (a21*x[1] + a22*x[2] + a23*x[3] + a24*x[4] + a25*x[5] + a26*x[6] + a27*x[7] <= u2)
model += (a31*x[1] + a32*x[2] + a33*x[3] + a34*x[4] + a35*x[5] + a36*x[6] + a37*x[7] <= u3)

# Set the objective
model += c1*x[1] + c2*x[2] + c3*x[3] + c4*x[4] + c5*x[5] + c6*x[6] + c7*x[7]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
	print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
	print(f"{name}: {constraint.value()}")
