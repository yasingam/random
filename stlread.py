#Yasin Gamieldien
#Python 2/3 compatible
#Requires Numpy, Pandas
#Free to use, alter, and distribute

import numpy as np
import pandas as pd

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

    stl_data = np.column_stack((xi, yi, zi))
    stl_pandas = pd.DataFrame(stl_data)

    stl_unique = np.array(stl_pandas.drop_duplicates())

    x = stl_unique[:, 0]
    y = stl_unique[:, 1]
    z = stl_unique[:, 2]

    return x, y, z
