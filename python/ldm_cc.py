#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr
from gnuradio import blocks

class ldm_cc(gr.hier_block2):
    """
    docstring for block ldm_cc
    """
    def __init__(self, multiple):
        gr.hier_block2.__init__(self,
            "ldm_cc",
            gr.io_signature(2, 2, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature

    	self.blocks_multiply_const_vxx = blocks.multiply_const_vcc((multiple, ))
    	self.blocks_add_xx= blocks.add_vcc(1)
        
    	# Define blocks and connect them
    	self.connect((self,0), (self.blocks_add_xx,0))
    	self.connect((self,1), self.blocks_multiply_const_vxx)
    	self.connect(self.blocks_multiply_const_vxx, (self.blocks_add_xx, 1))
    	self.connect(self.blocks_add_xx, self)
