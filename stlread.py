import numpy as np

def stl(path):
    """
    >>> faces, normals, vertices = stl(path)

    uses numpy to extract information from STL files
    """

    data_raw = np.fromfile(path, dtype='uint8')
    stl_header = data_raw[:80]
    faces = np.frombuffer(data_raw[80:84].tobytes(), dtype='uint32')[0]

    stl_raw = data_raw[84:]
    stl_raw_uint16 = np.frombuffer((stl_raw.tobytes()), dtype='uint16')
    stl_attr_index = np.arange(24, len(stl_raw_uint16), 25)
    stl_uint16 = np.delete(stl_raw_uint16, stl_attr_index)
    stl = np.frombuffer(stl_uint16.tobytes(), dtype='float32')
    stl_shaped = np.reshape(stl, (-1, 3))
    normals = stl_shaped[0:-1:4]

    normals_index = np.arange(0, len(stl_shaped), 4)
    vertices = np.delete(stl_shaped, normals_index).reshape(-1, 3)

    return faces, normals, vertices
