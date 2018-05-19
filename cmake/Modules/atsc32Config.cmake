INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ATSC32 atsc32)

FIND_PATH(
    ATSC32_INCLUDE_DIRS
    NAMES atsc32/api.h
    HINTS $ENV{ATSC32_DIR}/include
        ${PC_ATSC32_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ATSC32_LIBRARIES
    NAMES gnuradio-atsc32
    HINTS $ENV{ATSC32_DIR}/lib
        ${PC_ATSC32_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ATSC32 DEFAULT_MSG ATSC32_LIBRARIES ATSC32_INCLUDE_DIRS)
MARK_AS_ADVANCED(ATSC32_LIBRARIES ATSC32_INCLUDE_DIRS)

