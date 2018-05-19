/* -*- c++ -*- */

#define ATSC3_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "atsc3_swig_doc.i"

%{
#include "atsc3/ldpc_encoder_bb.h"
%}


%include "atsc3/ldpc_encoder_bb.h"
GR_SWIG_BLOCK_MAGIC2(atsc3, ldpc_encoder_bb);
