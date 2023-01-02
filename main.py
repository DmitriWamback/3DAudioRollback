import matplotlib.pyplot as plot

steps = 1000
rollback = 1000
dropoff = 1

def clamp(a, amin, amax):
    if a > amax: return amax
    if a < amin: return amin

    return a

def P(magnitude): # non-linear rollback
    global dropoff
    dropoff = max(dropoff, 5)
    return (clamp(rollback/max(min(magnitude + rollback / (dropoff*1.2), rollback), 0.0001) - 1, 0, dropoff) / dropoff)

def L(magnitude): # linear rollback
    return 1 - (clamp(magnitude, 0, rollback) / rollback)

non_linear = []
linear = []

for i in range(steps):
    non_linear.append(P(i))
    linear.append(L(i))

plot.plot(non_linear, label='P() Non-linear rollback', color='blue')
plot.plot(linear, label='L() linear rollback', color='red')
plot.legend(loc='upper right')
plot.show()
