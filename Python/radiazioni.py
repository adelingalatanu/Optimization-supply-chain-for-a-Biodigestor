from pulp import *

# Define the model
model = LpProblem(name="Radiazioni", sense=LpMaximize)

# Data
m1 = 5.5
m2 = 9.0
m3 = 6.0
m4 = 2.4
m5 = 7.0
m6 = 5.5
m7 = 9.5

r1 = 12
r2 = 13
r3 = 10
r4 = 15
r5 = 15

a01 = 0.4
a02 = 0.3
a03 = 0.25
a04 = 0.7
a05 = 0.5

a11 = 0.1
a12 = 0.0
a13 = 0.0
a14 = 0.1
a15 = 0.2

a21 = 0.1
a22 = 0.0
a23 = 0.15
a24 = 0.0
a25 = 0.1

a31 = 0.0
a32 = 0.1
a33 = 0.0
a34 = 0.0
a35 = 0.0

a41 = 0.0
a42 = 0.2
a43 = 0.1
a44 = 0.1
a45 = 0.0

a51 = 0.1
a52 = 0.0
a53 = 0.2
a54 = 0.0
a55 = 0.1

a61 = 0.1
a62 = 0.3
a63 = 0.15
a64 = 0.1
a65 = 0.1

a71 = 0.2
a72 = 0.1
a73 = 0.15
a74 = 0.0
a75 = 0.0

x = {j: LpVariable(name=f"x{j}", lowBound=0) for j in range(1, 6)}

# Constraints
model += (x[1] + x[2] + x[3] + x[4] + x[5] <= 60)

model += (x[1] <= r1)
model += (x[2] <= r2)
model += (x[3] <= r3)
model += (x[4] <= r4)
model += (x[5] <= r5)

model += (a11 * x[1] + a12 * x[2] + a13 * x[3] + a14 * x[4] + a15 * x[5] <= m1)
model += (a21 * x[1] + a22 * x[2] + a23 * x[3] + a24 * x[4] + a25 * x[5] <= m2)
model += (a31 * x[1] + a32 * x[2] + a33 * x[3] + a34 * x[4] + a35 * x[5] <= m3)
model += (a41 * x[1] + a42 * x[2] + a43 * x[3] + a44 * x[4] + a45 * x[5] <= m4)
model += (a51 * x[1] + a52 * x[2] + a53 * x[3] + a54 * x[4] + a55 * x[5] <= m5)
model += (a61 * x[1] + a62 * x[2] + a63 * x[3] + a64 * x[4] + a65 * x[5] <= m6)
model += (a71 * x[1] + a72 * x[2] + a73 * x[3] + a74 * x[4] + a75 * x[5] <= m7)

# Set the objective
model += a01 * x[1] + a02 * x[2] + a03 * x[3] + a04 * x[4] + a05 * x[5]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")