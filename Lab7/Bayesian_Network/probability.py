from model import universe

getProbability = universe.probability([["went off", "overslept", "is late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "overslept", "is late", "delayed", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "overslept", "is not late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "overslept", "is not late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "did not oversleep", "is late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "did not oversleep", "is late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "did not oversleep", "is not late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["went off", "did not oversleep", "is not late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "overslept", "is late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "overslept", "is late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "overslept", "is not late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "overslept", "is not late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "did not oversleep", "is late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "did not oversleep", "is late", "miss kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "did not oversleep", "is not late", "take kolokwium"]])
print(getProbability)


getProbability = universe.probability([["did not go off", "did not oversleep", "is not late", "miss kolokwium"]])
print(getProbability)