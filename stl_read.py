#Yasin Gamieldien
#Python2/3 compatible

#Purpose: Binary STL file handling


import numpy as np
import pandas as pd
import time
from random import randint

def stl_read(path):

    """
    Return faces, normals, and vertex co-ordinates of a binary STL

    >>> faces, normals, x1, y1, z1, x2, y2, z2, x3, y3, z3 = stl_read(path)
    """

    raw_data = np.fromfile(path, dtype='uint8')

    header = raw_data[:80]

    faces = np.frombuffer(raw_data[80:84].tobytes(), dtype='uint32')[0]

    raw_stl = np.frombuffer(raw_data[84:].tobytes(), dtype='uint16')
    raw_stl = np.ravel(np.reshape(raw_stl, (-1, 25))[:,:24])
    raw_stl = np.frombuffer(raw_stl.tobytes(), dtype='float32')

    stl = np.reshape(raw_stl, (-1, 12))

    normals = stl[:, :3]

    x1 = stl[:, 3]
    y1 = stl[:, 4]
    z1 = stl[:, 5]

    x2 = stl[:, 6]
    y2 = stl[:, 7]
    z2 = stl[:, 8]

    x3 = stl[:, 9]
    y3 = stl[:, 10]
    z3 = stl[:, 11]

    return faces, normals, x1, y1, z1, x2, y2, z2, x3, y3, z3


def stl_xyz(path):

    """
    Return x, y, z co-ordinates of vertices

    >>> x, y, z = stl_xyz(path)
    """

    faces, normals, x1, y1, z1, x2, y2, z2, x3, y3, z3 = stl_read(path)

    x = np.append(x1, x2)
    x = np.append(x, x3)

    y = np.append(y1, y2)
    y = np.append(y, y3)

    z = np.append(z1, z2)
    z = np.append(z, z3)

    return x, y, z


def unique_vertices(path):

    """
    Return unique vertices
    (Computationally heavy process)

    >>> x, y, z = unique_vertices(path)
    """
    x, y, z = stl_xyz(path)

    stl_data = np.column_stack((x, y, z))
    stl_pandas = pd.DataFrame(stl_data)

    stl_unique = np.array(stl_pandas.drop_duplicates())

    x = stl_unique[:, 0]
    y = stl_unique[:, 1]
    z = stl_unique[:, 2]

    return x, y, z


def stl_poisson_disc(path, points=1000, r=2):

    #learn about Poisson-disc sampling
    print('Analysing STL file....')

    x, y, z = stl_xyz(path)

    print('DONE')
    print('Applying Poisson-disc sampling....')

    stl = np.column_stack((x, y, z))

    random_index = randint(0, len(stl)-1)

    stl_poisson_disc = stl[random_index]

    time_started = time.time()

    while len(stl) > 1:

        stl = stl[np.sqrt((stl[:, 0] - stl[random_index, 0])**2 +
            (stl[:, 1] - stl[random_index, 1])**2 +
            (stl[:, 2] - stl[random_index, 2])**2) > r]

        if len(stl)>0:

            random_index = randint(0, len(stl)-1)

            stl_poisson_disc = np.vstack((stl_poisson_disc,
                stl[random_index]))

    time_ended = time.time()
    time_taken = time_ended - time_started

    print(time_taken, 's')

    return stl_poisson_disc
