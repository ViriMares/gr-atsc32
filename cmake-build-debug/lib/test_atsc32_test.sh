#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/local/gr-modtool/gr-atsc32/lib
export PATH=/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-atsc32 
