from pomegranate import *
#************************************
#
#   AI&CV Jakub Bujak 249120
#
#*************************************

# First node
# this node is independent from others, thus we are using DiscreteDistribution class
alarm = Node(DiscreteDistribution({
    "went off": 0.9,
    "did not go off": 0.1
}), name="alarm")

# Oversleeping is dependant from alarm going off
oversleep = Node(ConditionalProbabilityTable([
    ["went Off", "overslept", 0.1],
    ["went Off", "did not oversleep", 0.9],
    ["did not go off", "overslept", 0.9],
    ["did not go off", "did not oversleep", 0.1]
], [alarm.distribution]), name="oversleep")

# bus is independent form other nodes
bus = Node(DiscreteDistribution({
    "is late": 0.2,
    "is not late": 0.8
}), name="bus")

# Being on time for kolokwium is dependant from bus and oversleeping
on_time = Node(ConditionalProbabilityTable([
    ["overslept", "is late", "take kolokwium", 0.1],
    ["overslept", "is late", "miss kolokwium", 0.9],
    ["overslept", "is not late", "take kolokwium", 0.3],
    ["overslept", "is not late", "miss kolokwium", 0.7],
    ["did not oversleep", "is late", "take kolokwium", 0.2],
    ["did not oversleep", "is late", "miss kolokwium", 0.8],
    ["did not oversleep", "is not late", "take kolokwium", 0.1],
    ["did not oversleep", "is not late", "miss kolokwium", 0.9]
], [oversleep.distribution, bus.distribution]), name="on_time")

# Create a Bayesian Network and add states
universe = BayesianNetwork()
universe.add_states(alarm, oversleep, bus, on_time)

# Add edges connecting nodes
universe.add_edge(alarm, oversleep)
universe.add_edge(oversleep, on_time)
universe.add_edge(bus, on_time)

# Finalize model
universe.bake()