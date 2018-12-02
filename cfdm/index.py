from builtins import super

from . import mixin
from . import core


class Index(mixin.NetCDFVariable,
            mixin.NetCDFDimension,
            mixin.NetCDFInstanceDimension,
            mixin.NetCDFSampleDimension,
            mixin.PropertiesData,
            core.abstract.PropertiesData):
    '''An index variable required to uncompress a ragged array.

.. versionadded:: 1.7.0

    '''
    def __init__(self, properties={}, data=None, source=None,
                 copy=True, _use_data=True):
        '''TODO
        '''
        super().__init__(properties=properties, data=data,
                         source=source, copy=copy,
                         _use_data=_use_data)
        
        self._initialise_netcdf(source)
    #--- End: def
    
    def dump(self, display=True, field=None, key=None, _title=None,
             _create_title=True, _prefix='', _level=0,
             _omit_properties=None):
        '''TODO
        '''
        if _create_title and _title is None: 
            _title = 'Index: ' + self.name(default='')

        return super().dump(display=display, field=field, key=key,
                            _omit_properties=_omit_properties,
                            _prefix=_prefix, _level=_level,
                            _title=_title,
                            _create_title=_create_title)
    #--- End: def
    
#--- End: class
