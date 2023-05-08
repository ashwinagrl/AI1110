import numpy as np
import matplotlib.pyplot as plt
simlen = 1000000

space = np.arange(1, 21)
numbers = np.repeat(space.reshape(1,20),simlen,axis = 0)
experiments = np.apply_along_axis(lambda x: np.sort(np.random.choice(x,size = 6 , replace = False)),1,numbers)

p =1/38760
print('The Theoretical Probability of winning is: ' + "{0:.7f}".format(p))

jury = np.sort(np.random.choice(space , size = 6 , replace = False))
favor = np.apply_along_axis(lambda x: np.array_equal(x , jury) ,1, experiments)

favor_num = np.count_nonzero(favor)
p_act = favor_num/simlen
print('The Actual Probability of winning is: ' + "{0:.7f}".format(p_act))
