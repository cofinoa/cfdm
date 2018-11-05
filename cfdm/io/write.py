from .. import __version__
from .. import (CoordinateReference,
                Field,
                Data)

from . import CFDMImplementation

from .netcdf import NetCDFWrite


implementation = CFDMImplementation(version=__version__,
                                    CoordinateReference=CoordinateReference,
                                    Field=Field,
                                    Data=Data)

def write(fields, filename, fmt='NETCDF4', overwrite=True,
          global_attributes=None, variable_attributes=None,
          external_file=None, datatype=None,
          least_significant_digit=None, endian='native', compress=0,
          fletcher32=False, shuffle=True, HDF_chunksizes=None,
          verbose=False, _implementation=implementation):
    '''Write fields to a netCDF file.

**File format**

See the *fmt* parameter for details on which netCDF file formats are
supported.

**NetCDF variable and dimension names**

These names are stored from fields read a from dataset, or may be set
manually. They are used when writing the field to the file. If a name
has not been set then one will be constructed. The names may be
modified internally to prevent duplication in the file.

Each construct, or construct component, that corresponds to a netCDF
variable has the following methods to get, set and remove a netCDF
variable name: `!nc_get_variable`, `!nc_set_variable` and
`!nc_del_variable` method

The domain axis construct has the following methods to get, set and
remove a netCDF dimension name: `~cfdm.DomainAxis.nc_get_dimension`,
`~cfdm.DomainAxis.nc_set_dimension` and
`~cfdm.DomainAxis.nc_del_dimension`.

**NetCDF attributes**

Field construct properties may be written as netCDF global attributes
or netCDF data variable attributes. See the *global_attributes* and
*variable_attributes* parameters for details.

**External variables**

Constructs marked as external may be omitted from the file and referred
to via the netCDF "external_variables" global attribute. In addition,
omitted constructs may be written to an external file. Constructs that
may be external have the following methods to get and set their
external status: `!nc_get_external` and `!nc_set_external`.

.. versionadded:: 1.7

.. seealso:: `cfdm.read`

:Parameters:

    fields: (sequence of) `Field`
        The field constructs to write to the file.

    filename: `str`
        The output netCDF file name. Various type of expansion are
        applied to the file names.

        Relative paths are allowed, and standard tilde and shell
        parameter expansions are applied to the string.

        *Example:*
          The file ``file.nc`` in the user's home directory can be
          described by any of the following: ``'$HOME/file.nc'``,
          ``'${HOME}/file.nc'``, ``'~/file.nc'``,
          ``'~/tmp/../file.nc'`` or, most simply but assuming that the
          current working directory is ``$HOME``, ``'file.nc'``.
  
    fmt: `str`, optional
        The format of the output file. One of:

          ==========================  ===============================
          *fmt*                       Output file type
          ==========================  ===============================
          ``'NETCDF4'``               NetCDF4 format file. This is
                                      the default.       
          
          ``'NETCDF4_CLASSIC'``       NetCDF4 classic format file
                                      (see below) 
          
          ``'NETCDF3_CLASSIC'``       NetCDF3 classic format file
                                      (limited to file sizes less
                                      than 2 Gb).
          
          ``'NETCDF3_64BIT_OFFSET'``  NetCDF3 64-bit offset format
                                      file
          
          ``'NETCDF3_64BIT'``         An alias for
                                      ``'NETCDF3_64BIT_OFFSET'``
          
          ``'NETCDF3_64BIT_DATA'``    NetCDF3 64-bit offset format
                                      file with extensions (see
                                      below)
          ==========================  ===============================

        By default the format is ``'NETCDF4'``.

        Note that the netCDF3 formats may be considerably slower than
        any of the other options.

        All formats support large files (i.e. those greater than 2 Gb)
        except ``'NETCDF3_CLASSIC'``.

        ``'NETCDF3_64BIT_DATA'`` is a format that requires version
        4.4.0 or newer of the C library (use `cfdm.environment` to see
        which version if the netCDF-C library is in use). It extends
        the ``'NETCDF3_64BIT_OFFSET'`` binary format to allow for
        unsigned/64 bit integer data types and 64-bit dimension sizes.

        ``'NETCDF4_CLASSIC'`` files use the version 4 disk format
        (HDF5), but omits features not found in the version 3
        API. They can be read by HDF5 clients. They can also be read
        by netCDF 3 clients only if they have been re-linked against
        the netCDF4 library.

        ``'NETCDF4'`` files use the version 4 disk format (HDF5) and
        use the new features of the version 4 API.

    overwrite: `bool`, optional
        If False then raise an error if the output file pre-exists. By
        default a pre-existing output file is overwritten.

    global_attributes: (sequence of) `str`, optional
         Create netCDF global attributes from the given field
         construct properties, rather than netCDF data variable
         attributes.

         These attributes are in addition to the following properties,
         which are created as netCDF global attributes by default:
         
           * the `description of file contents
             <http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html#description-of-file-contents>`_
             properties, and

           * properties flagged as global on any of the fields being
             written (see `cfdm.Field.nc_global_properties` for
             details).

         Note that it is not possible to create a netCDF global
         attribute from a property that has different values for
         different fields being written. In this case the property
         will not be written as a netCDF global attribute, even if it
         has been specified by the *global_attributes* parameter or is
         one of the default properties, but will appear as an
         attribute on the netCDF data variable corresponding to each
         field construct that contains the property.

         *Example:*
            ``global_attributes='project'``

         *Example:*
            ``global_attributes=['project', 'experiment']``

    variable_attributes: (sequence of) `str`, optional
         Create netCDF data variable attributes from the given field
         properties, rather than netCDF global attributes.

         By default, all properties other than those which are created
         as netCDF global attributes (see the *global_attributes*
         parameter), are created as attributes netCDF data variables.

         If the same property is named by both the
         *variable_attributes* and *global_attributes* parameters,
         then the former takes precedence.

         *Example:*
            ``variable_attributes='project'``

         *Example:*
            ``variable_attributes=['project', 'doi']``


    external_file: `str`, optional   
        Write constructs that are marked as external, and have data,
        to the named external file. Ignored if there are no such
        constructs .

    datatype: `dict`, optional
        Specify data type conversions to be applied prior to writing
        data to disk. This may be useful as a crude means of packing,
        or because the output format does not support a particular
        data type (for example, netCDF3 classic files do not support
        64-bit integers). By default, input data types are
        preserved. Any data type conversion is only applied to the
        arrays on disk, and not to the input fields themselves.

        Data types conversions are defined by `numpy.dtype` objects in
        a dictionary whose keys are input data types with values of
        output data types.

        *Example:*

          To convert 64-bit integers to 32-bit integers:
          ``datatype={numpy.dtype('int64'): numpy.dtype('int32')}``.
       
    endian: `str`, optional
        The endian-ness of the output file. Valid values are
        ``'little'``, ``'big'`` or ``'native'``. By default the output
        is native endian. See the `netCDF4 package
        <http://unidata.github.io/netcdf4-python>`_ for more details.

        *Example:*
          ``endian='big'``

    compress: `int`, optional
        Regulate the speed and efficiency of compression. Must be an
        integer between ``0`` and ``9``. ``0`` means no compression;
        ``1`` is the fastest, but has the lowest compression ratio;
        ``9`` is the slowest but best compression ratio. The default
        value is ``0``. An error is raised if compression is requested
        for a netCDF3 output file format. See the `netCDF4 package
        <http://unidata.github.io/netcdf4-python>`_ for more details.

        *Example:*
          ``compress=4``
    
    least_significant_digit: `int`, optional
        Truncate the input field data arrays. For a given positive
        integer, N the precision that is retained in the compressed
        data is 10 to the power -N. For example, a value of 2 will
        retain a precision of 0.01. In conjunction with the *compress*
        parameter this produces 'lossy', but significantly more
        efficient compression. See the `netCDF4 package
        <http://unidata.github.io/netcdf4-python>`_ for more details.

        *Example:*
          ``least_significant_digit=3``

    fletcher32: `bool`, optional
        If True then the Fletcher-32 HDF5 checksum algorithm is
        activated to detect compression errors. Ignored if *compress*
        is ``0``. See the `netCDF4 package
        <http://unidata.github.io/netcdf4-python>`_ for details.

    shuffle: `bool`, optional
        If True (the default) then the HDF5 shuffle filter (which
        de-interlaces a block of data before compression by reordering
        the bytes by storing the first byte of all of a variable's
        values in the chunk contiguously, followed by all the second
        bytes, and so on) is turned off. By default the filter is
        applied because if the data array values are not all wildly
        different, using the filter can make the data more easily
        compressible.  Ignored if the *compress* parameter is ``0``
        (which is its default value). See the `netCDF4 package
        <http://unidata.github.io/netcdf4-python>`_ for more details.

    HDF_chunksizes: `dict`, optional
        Manually specify HDF5 chunks for the field data arrays.

        Chunking refers to a storage layout where a data array is
        partitioned into fixed-size multi-dimensional chunks when
        written to a netCDF4 file on disk. Chunking is ignored if the
        field is written to a netCDF3 format file.

        A chunk has the same rank as the data array, but with fewer
        (or no more) elements along each axes. The chunk is defined by
        a dictionary whose keys identify axes with values of the
        chunks size for those axes.

        If a given chunk size for an axis is larger than the axis size
        for any field, then the size of the axis at the time of
        writing to disk will be used instead.

        If chunk sizes have been specified for some but not all axes,
        then the each unset chunk size is assumed to be the full size
        of the axis for each field.

        If no chunk sizes have been set for any axes then the netCDF
        default chunk is used
        (http://www.unidata.ucar.edu/software/netcdf/docs/netcdf_perf_chunking.html).

        If any chunk sizes have already been set on a field with the
        `cf.Field.HDF_chunks` method then these are used in instead.

        A detailed discussion of HDF chunking and I/O performance is
        available at
        https://www.hdfgroup.org/HDF5/doc/H5.user/Chunking.html and
        http://www.unidata.ucar.edu/software/netcdf/workshops/2011/nc4chunking.
        Basically, you want the chunks for each dimension to match as
        closely as possible the size and shape of the data block that
        users will read from the file.

    verbose: `bool`, optional
        If True then print a summary of how constructs map to output
        netCDF variables and dimensions.

:Returns:

    `None`

**Examples:**

TODO

    '''
    # ----------------------------------------------------------------
    # Initialise the netCDF write object
    # ----------------------------------------------------------------
    netcdf = NetCDFWrite(_implementation)

    if fields:
        netcdf.write(fields, filename, fmt=fmt, overwrite=overwrite,
                     global_attributes=global_attributes,
                     variable_attributes=variable_attributes,
                     external_file=external_file,
                     datatype=datatype,
                     least_significant_digit=least_significant_digit,
                     endian=endian, compress=compress,
                     shuffle=shuffle, fletcher32=fletcher32,
                     HDF_chunks=HDF_chunksizes, verbose=verbose)
#--- End: def
