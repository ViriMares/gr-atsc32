#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Viridiana Mares, Facultad de Ingeniería UNAM.
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
    This is the LDM block from the standar ATSC 3.0.
    This block need two parameters: multiplier factor and normalizing factor.
    LDM combine two layer called "core layyer" and "enhanced layer". Before combination, enhanced layer is multiplied by a factor. After combination, the complete signal is normalized.

    More information about the block can consult Physical Layer Protocol document A322 available here:
    https://www.atsc.org/wp-content/uploads/2016/10/A322-2017a-Physical-Layer-Protocol-2.pdf
    """
    def __init__(self, multiplier):
        gr.hier_block2.__init__(self,
            "ldm_cc",
            gr.io_signature(2, 2, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex))  # Output signature

        normalizing = { 1.0000000: 0.7071068, 0.9440609: 0.7271524, 0.8912509: 0.7465331, 0.8413951: 0.7651789, 0.7943282: 0.7830305, 0.7498942: 0.8000406, 0.7079458: 0.8161736, 0.6683439: 0.8314061, 0.6309573: 0.8457262, 0.5956621: 0.8591327, 0.5623413: 0.8716346, 0.5011872: 0.8940022, 0.4466836: 0.9130512, 0.3981072: 0.9290819, 0.3548134: 0.9424353, 0.3162278: 0.9534626, 0.2818383: 0.9625032, 0.2511886: 0.9698706, 0.2238721: 0.9758449, 0.1995262: 0.9806699, 0.1778279: 0.9845540, 0.1584893: 0.9876723, 0.1412538: 0.9901705, 0.1258925: 0.9921685, 0.1122018: 0.9937642, 0.1000000: 0.9950372, 0.0891251: 0.9960519, 0.0794328: 0.9968601, 0.0707946: 0.9975034, 0.0630957: 0.9980154, 0.0562341: 0.9984226 }
        norm = normalizing[multiplier]

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((multiplier, ))
    	self.blocks_add_xx = blocks.add_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((norm, ))

    	# Define blocks and connect them
    	self.connect((self, 0), (self.blocks_add_xx, 0))
    	self.connect((self, 1), self.blocks_multiply_const_vxx_0)
    	self.connect(self.blocks_multiply_const_vxx_0, (self.blocks_add_xx, 1))
        self.connect(self.blocks_add_xx, self.blocks_multiply_const_vxx_1)
    	self.connect(self.blocks_multiply_const_vxx_1, self)

        print
        print "LDM:"
        print "Multiplier Factor Alfa =", multiplier
        print "Normalizing Factor Beta=", norm