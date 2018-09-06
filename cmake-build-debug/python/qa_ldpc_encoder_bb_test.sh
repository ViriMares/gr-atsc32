#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/local/gr-modtool/gr-atsc32/python
export PATH=/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/usr/local/gr-modtool/gr-atsc32/cmake-build-debug/swig:$PYTHONPATH
/usr/bin/python2 /usr/local/gr-modtool/gr-atsc32/python/qa_ldpc_encoder_bb.py 
