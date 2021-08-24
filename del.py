import itertools
import numpy as np
inp = [(480, 300), (600, 420)]
x_coords = [x for x in range(inp[0][0], inp[1][0] + 1,10)]
y_coords = [y for y in range(inp[0][1], inp[1][1] + 1,15)]
output = np.array(list(itertools.product(x_coords, y_coords)))
print(x_coords)
print(y_coords)
np.savetxt("data.csv", output, delimiter = ",")