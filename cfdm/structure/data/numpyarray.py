from builtins import super

import numpy

from . import abstract


class NumpyArray(abstract.Array):
    '''A container for a numpy array.

    '''
    def __init__(self, array=None):
        '''**Initialization**

:Parameters:

    array: `numpy.ndarray`
        The numpy array.

        '''
        super().__init__(array=array)
    #--- End: def
    
    @property
    def dtype(self):
        '''Data-type of the data elements.

:Examples:

>>> a.dtype
dtype('float64')
>>> print(type(a.dtype))
<type 'numpy.dtype'>

        '''
        return self.array.dtype
    #--- End: def

    @property
    def ndim(self):
        '''Number of array dimensions
                
:Examples:

>>> a.shape
(73, 96)
>>> a.ndim
2
>>> a.size
7008

>>> a.shape
(1, 1, 1)
>>> a.ndim
3
>>> a.size
1

>>> a.shape
()
>>> a.ndim
0
>>> a.size
1

        '''
        return self.array.ndim
    #--- End: def
    
    @property
    def shape(self):
        '''Tuple of array dimension sizes.

:Examples:

>>> a.shape
(73, 96)
>>> a.ndim
2
>>> a.size
7008

>>> a.shape
(1, 1, 1)
>>> a.ndim
3
>>> a.size
1

>>> a.shape
()
>>> a.ndim
0
>>> a.size
1

'''
        return self.array.shape
    #--- End: def
    
    @property
    def size(self):
        '''Number of elements in the array.

:Examples:

>>> a.shape
(73, 96)
>>> a.size
7008
>>> a.ndim
2

>>> a.shape
(1, 1, 1)
>>> a.ndim
3
>>> a.size
1

>>> a.shape
()
>>> a.ndim
0
>>> a.size
1
        '''
        return self.array.size
    #--- End: def
    
    def get_array(self):
        '''Return an independent numpy array containing the data.

:Returns:

    out: `numpy.ndarray`
        An independent numpy array of the data.

:Examples:

>>> n = numpy.asanyarray(a)
>>> isinstance(n, numpy.ndarray)
True

        '''
        array = self.array
        
        if not array.ndim and numpy.ma.isMA(array):
            # This is because numpy.ma.copy doesn't work for
            # scalar arrays (at the moment, at least)
            ma_array = numpy.ma.empty((), dtype=array.dtype)
            ma_array[...] = array
            array = ma_array
        else:
            array = array.copy()

        return array
    #--- End: def

#--- End: class
