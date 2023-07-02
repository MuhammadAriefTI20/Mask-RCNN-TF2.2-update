import tensorflow as tf
import numpy as np
import keras as kr

print("versi Tensorflow = "+tf.version.VERSION)
print("versi Numpy = "+np.version.version)
if len(tf.config.list_physical_devices('GPU')) > 0:    
    print("You have a GPU enabled.")
else:    
    print("Enable a GPU before running this notebook.")
"""
hanya untuk cek versi tensorflow, numpy, dan gpu harusnya sudah sesuai lib yang dibutuhkan
#M.A
"""
