

import time

large_dict = {i: i for i in range(10000000)}


start_time = time.time()
exists = 1 in large_dict
print("Time taken to check if 1 exists in large_dict: {}".format(time.time() - start_time))



start_time = time.time()
exists = 1 in large_dict.keys()
print("Time taken to check if 1 exists in large_dict: {}".format(time.time() - start_time))
