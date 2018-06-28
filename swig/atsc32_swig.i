/* -*- c++ -*- */

#define ATSC32_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "atsc32_swig_doc.i"

%{
#include "atsc32/atsc32_config.h"
#include "atsc32/ldpc_encoder_bb.h"
%}

%include "atsc32/atsc32_config.h"
%include "atsc32/ldpc_encoder_bb.h"
GR_SWIG_BLOCK_MAGIC2(atsc32, ldpc_encoder_bb);

