import abc

NOT_IMPLEMENTED = 'This method must be implemented'

class IO(object):
    '''
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, implementation):
        self.implementation = implementation

    @abc.abstractmethod
    def close_file(self, *args, **kwargs):
        '''Open the file for reading.
        '''
        raise NotImplementedError(NOT_IMPLEMENTED)
    #--- End: def
        
    @abc.abstractmethod
    def file_type(cls, *args, **kwargs):
        '''Find the format of a file.
        '''
        raise NotImplementedError(NOT_IMPLEMENTED)
    #--- End: def

    @abc.abstractmethod
    def open_file(self, *args, **kwargs):
        '''Close the file that has been read.
        '''
        raise NotImplementedError(NOT_IMPLEMENTED)
    #--- End: def

#--- End: class
