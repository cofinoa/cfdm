import abc


# ====================================================================
#
# 
#
# ====================================================================

class ConstructAccess(object):
    '''
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _get_constructs(self, *default):
        '''
.. versionadded:: 1.6
        
        '''
        print 'method returns the Constructs instance'
    #--- End: def
    
    def array_constructs(self, copy=False):
        return self._get_constructs().array_constructs(copy=copy)
    
    def auxiliary_coordinates(self, copy=False):
        return self._get_constructs().constructs('auxiliary_coordinate', copy=copy)
    
    def cell_measures(self, copy=False):
        return self._get_constructs().constructs('cell_measure', copy=copy)
    
    def construct_axes(self, key=None):
        return self._get_constructs().construct_axes(key=key)
    
    def construct_type(self, key):
        return self._get_constructs().construct_type(key)
       
    def constructs(self, copy=False):
        '''
        '''
        return self._get_constructs().constructs(copy=copy)
    #--- End: def
    
    def coordinate_references(self, copy=False):
        return self._get_constructs().constructs('coordinate_reference', copy=copy)
    
    def coordinates(self, copy=False):
        '''
        '''
        out = self.dimension_coordinates(copy=copy)
        out.update(self.auxiliary_coordinates(copy=copy))
        return out
    #--- End: def

    def get_construct(self, key, *default):
        '''
        '''
        return self._get_constructs().get_construct(key, *default)
    #--- End: def

    def dimension_coordinates(self, copy=False):
        return self._get_constructs().constructs('dimension_coordinate', copy=copy)
    
    def domain_ancillaries(self, copy=False):
        return self._get_constructs().constructs('domain_ancillary', copy=copy)
    
    def domain_axes(self, copy=False):
        return self._get_constructs().domain_axes(copy=copy)
    
    def domain_axis_name(self, axis):
        '''
        '''
        return self._get_constructs().domain_axis_name(axis)
    #--- End: for
    
    @abc.abstractmethod
    def del_construct(self, key):
        '''
        '''
        pass
    #--- End: def

    def set_auxiliary_coordinate(self, item, key=None, axes=None,
                                 copy=True, replace=True):
        '''
        '''
        if not replace and key in self.auxiliary_coordinates():
            raise ValueError(
"Can't insert auxiliary coordinate object: Identifier {!r} already exists".format(key))

        return self.set_construct('auxiliary_coordinate', item,
                                  key=key, axes=axes, copy=copy)
    #--- End: def

    def set_domain_axis(self, domain_axis, key=None, replace=True, copy=True):
        '''
        '''
        axes = self.domain_axes()
        if not replace and key in axes and axes[key].size != domain_axis.size:
            raise ValueError(
"Can't insert domain axis: Existing domain axis {!r} has different size (got {}, expected {})".format(
    key, domain_axis.size, axes[key].size))

        return self.set_construct('domain_axis',
                                  domain_axis, key=key, copy=copy)
    #--- End: def

    def set_domain_ancillary(self, item, key=None, axes=None,
                                copy=True, replace=True):
        '''
        '''       
        if not replace and key in self.domain_ancillaries():
            raise ValueError(
"Can't insert domain ancillary object: Identifier {0!r} already exists".format(key))

        return self.set_construct('domain_ancillary', item, key=key,
                                  axes=axes,
                                  copy=copy)
    #--- End: def

    def set_construct(self, construct_type, construct, key=None, axes=None,
                      copy=True):
        '''
        '''
        return self._get_constructs().set_construct(construct_type,
                                                    construct,
                                                    key=key,
                                                    axes=axes,
                                                    copy=copy)
    #--- End: def

    def set_construct_axes(self, key, axes):
        '''
        '''
        return self._get_constructs().set_construct_axes(key, axes)
    #--- End: def

    def set_cell_measure(self, item, key=None, axes=None, copy=True, replace=True):
        '''
        '''
        if not replace and key in self.cell_measures():
            raise ValueError(
"Can't insert cell measure object: Identifier {0!r} already exists".format(key))

        return self.set_construct('cell_measure', item, key=key,
                                  axes=axes, copy=copy)
    #--- End: def

    def set_coordinate_reference(self, item, key=None, axes=None,
                                    copy=True, replace=True):
        '''
        '''
        return self.set_construct('coordinate_reference',
                                  item, key=key, copy=copy)
    #--- End: def

    def set_dimension_coordinate(self, item, key=None, axes=None, copy=True, replace=True):
        '''
        '''
        if not replace and key in self.dimension_coordinates():
            raise ValueError(
"Can't insert dimension coordinate object: Identifier {!r} already exists".format(key))

        return self.set_construct('dimension_coordinate',
                                  item, key=key, axes=axes, copy=copy)
    #--- End: def

#--- End: class