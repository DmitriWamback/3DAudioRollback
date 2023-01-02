import matplotlib.pyplot as plot

steps = 1000
rollback = 90

def clamp(a, amin, amax):
    if a > amax: return amax
    if a < amin: return amin

    return a

def P(magnitude): # non-linear rollback
    return clamp(rollback/max(min(magnitude, rollback), 0.01) - 1, 0, 10) / 10

def L(magnitude): # linear rollback
    return 1 - (clamp(magnitude, 0, rollback) / rollback)

non_linear = []
linear = []

for i in range(steps):
    non_linear.append(P(i/10))
    linear.append(L(i/10))

plot.plot(non_linear, label='P() Non-linear rollback', color='blue')
plot.plot(linear, label='L() linear rollback', color='red')
plot.legend(loc='upper right')
plot.show()
