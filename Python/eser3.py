from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

# Define the problem
model = LpProblem(name="Al", sense=LpMinimize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 7)}

# Data
a11 = 0.5
a12 = 0.75
a13 = 0.20
a14 = 0.01
a15 = 0.02
a16 = 0.02
a17 = 0.02
a18 = 0.02
a19 = 97.0
a110 = 0.06
a111 = 1.40

a21 = 0.5
a22 = 0.7
a23 = 0.2
a24 = 0.01
a25 = 0.02
a26 = 0.02
a27 = 0.02
a28 = 0.02
a29 = 97.0
a210 = 0.06
a211 = 1.45

a31 = 0.30
a32 = 0.50
a33 = 0.35
a34 = 0.05
a35 = 0.05
a36 = 0.05
a37 = 0.05
a38 = 0.05
a39 = 90.0
a310 = 0.77
a311 = 7.83

a4 = 100

a5 = 100

a6 = 100

q1 = 0.5
q2 = 1.20
q3 = 2.20

Q = 4.5

c1 = 1230
c2 = 1230
c3 = 1230
c4 = 2140
c5 = 1300
c6 = 2442

l1 = 0.2
l2 = 0.45
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0
l8 = 0
l9 = 96.9
l10 = 0
l11 = 0

u1 = 0.6
u2 = 0.9
u3 = 0.35
u4 = 0.1
u5 = 0.1
u6 = 0.1
u7 = 0.1
u8 = 0.1
u9 = 100
u10 = 0.15
u11 = 0

# Add the constraints
model += (x[1] <= q1)
model += (x[2] <= q2)
model += (x[3] <= q3)

model += (x[1] + x[2] + x[3] + x[4] + x[5] + x[6] ==Q)

model += (a11*x[1]/Q + a21*x[2]/Q +a31*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l1)
model += (a12*x[1]/Q + a22*x[2]/Q +a32*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l2)
model += (a13*x[1]/Q + a23*x[2]/Q +a33*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l3)
model += (a14*x[1]/Q + a24*x[2]/Q +a34*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l4)
model += (a15*x[1]/Q + a25*x[2]/Q +a35*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l5)
model += (a16*x[1]/Q + a26*x[2]/Q +a36*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l6)
model += (a17*x[1]/Q + a27*x[2]/Q +a37*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l7)
model += (a18*x[1]/Q + a28*x[2]/Q +a38*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l8)
model += (a19*x[1]/Q + a29*x[2]/Q +a39*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l9)
model += (a110*x[1]/Q + a210*x[2]/Q +a310*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l10)
model += (a111*x[1]/Q + a211*x[2]/Q +a311*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q >= l11)

model += (a11*x[1]/Q + a21*x[2]/Q +a31*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u1)
model += (a12*x[1]/Q + a22*x[2]/Q +a32*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u2)
model += (a13*x[1]/Q + a23*x[2]/Q +a33*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u3)
model += (a14*x[1]/Q + a24*x[2]/Q +a34*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u4)
model += (a15*x[1]/Q + a25*x[2]/Q +a35*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u5)
model += (a16*x[1]/Q + a26*x[2]/Q +a36*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u6)
model += (a17*x[1]/Q + a27*x[2]/Q +a37*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u7)
model += (a18*x[1]/Q + a28*x[2]/Q +a38*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u8)
model += (a19*x[1]/Q + a29*x[2]/Q +a39*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u9)
model += (a110*x[1]/Q + a210*x[2]/Q +a311*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u10)
model += (a111*x[1]/Q + a211*x[2]/Q +a311*x[3]/Q + a4*x[4]/Q + a5*x[5]/Q + a6*x[6]/Q <= u11)

# Set the objective
model += c1*x[1] + c2*x[2] + c3*x[3] + c4*x[4] + c5*x[5] + c6*x[6]

# Solve the optimization problem
status = model.solve()

# Get the results
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
	print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
	print(f"{name}: {constraint.value()}")

