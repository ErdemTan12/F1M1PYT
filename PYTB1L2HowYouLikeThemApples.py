boomgaard = 333
boom_in_zon = 146
boom_in_schaduw = boom_in_zon / 100 * 80

schaduwberg1 = boomgaard / 3 * 2

schaduwberg2 = boom_in_zon * boom_in_schaduw
schaduwberg3 = boomgaard / 3 * boom_in_zon
schaduwberg4 = schaduwberg3 + schaduwberg2

print(schaduwberg1)

print(schaduwberg2)

print(schaduwberg3)

print(boom_in_schaduw)

print(schaduwberg4 / 4)