from conjugate_gradient import conjugate_gradient
import numpy as np

edges = []
edges.append((0, 1, 0.1))
edges.append((1, 2, 0.2))
edges.append((2, 3, 0.3))
edges.append((0, 3, 0))

b = np.array([-10, 0, 0, 10])

f = conjugate_gradient(edges, b, 1e-10)

print(f)
    
