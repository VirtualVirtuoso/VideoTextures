import numpy as np
import numpy.matlib

"""
|-------------------------------------------------------------------------------
| Loop Overlap Utility
|-------------------------------------------------------------------------------
|
| Given two loop structures, checks to see if they overlap. The loops will
| always be a compound loop and a primitive loop. This is required during
| the Video Loop algorithm
|
"""

def check_loop_overlap(primitive_loop, compound_loop):
    compound_start = np.nonzero(compound_loop[0][:])
    compound_end = np.nonzero(compound_loop[1][:])
    primitive_start = np.matlib.repmat(primitive_loop[1], len(compound_start), 1)
    primitive_end = np.matlib.repmat(primitive_loop[0], len(compound_end), 1)

    overlap1 = compound_start - primitive_end
    overlap2 = compound_end - primitive_start
    overlap3 = compound_end - primitive_end
    overlap4 = compound_start - primitive_start

    any_overlap = (overlap1 < 0).any and (overlap2 > 0).any or \
                  (overlap1 < 0).any and (overlap3 > 0).any or \
                  (overlap4 < 0).any and (overlap2 > 0).any

    return any_overlap
