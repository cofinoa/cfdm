from . import abstract
#from future.utils import with_metaclass


class DomainAncillary(abstract.PropertiesDataBounds):
#    with_metaclass(abc.ABCMeta, abstract.PropertiesDataBounds)):
    '''A domain ancillary construct of the CF data model.

A domain ancillary construct provides information which is needed for
computing the location of cells in an alternative coordinate
system. It is referenced by a term of a coordinate conversion formula
of a coordinate reference construct. It contains a data array which
depends on zero or more of the domain axes.

It also contains an optional array of cell bounds, stored in a
`Bounds` object, recording the extents of each cell (only applicable
if the array contains coordinate data), and properties to describe the
data.

An array of cell bounds spans the same domain axes as the data array,
with the addition of an extra dimension whose size is that of the
number of vertices of each cell.

    '''
    
#--- End: class