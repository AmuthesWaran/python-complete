import numpy as np
firstname = np.genfromtxt("../firstname.csv", delimiter=",",
                          missing_values="", dtype=str, skip_header=1)

fullname = np.genfromtxt("../fullname.csv", delimiter=",",
                         missing_values="", dtype=str, skip_header=1)

# print(firstname)
print(fullname)
