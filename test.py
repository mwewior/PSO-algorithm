import numpy as np

while 1:
    dif = liczba = np.random.uniform(0, 30)
    # Normalizacja do przedziału od 0 do 2
    print((dif/(dif+1)))
    inertia_weight = 0.7*(dif/(dif+1))