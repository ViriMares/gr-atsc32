# Install script for directory: /usr/local/gr-modtool/gr-atsc32/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/atsc32" TYPE FILE FILES
    "/usr/local/gr-modtool/gr-atsc32/python/__init__.py"
    "/usr/local/gr-modtool/gr-atsc32/python/ldm_cc.py"
    "/usr/local/gr-modtool/gr-atsc32/python/modulator_bc.py"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/atsc32" TYPE FILE FILES
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/__init__.pyc"
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/ldm_cc.pyc"
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/modulator_bc.pyc"
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/__init__.pyo"
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/ldm_cc.pyo"
    "/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python/modulator_bc.pyo"
    )
endif()

