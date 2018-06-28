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

from gnuradio import digital
from gnuradio import gr

class modulator_bc(gr.hier_block2):
    """
    docstring for block modulator_bc
    """
    def __init__(self, constellation, rate):
        gr.hier_block2.__init__(self,
            "modulator_bc",
            gr.io_signature(1, 1, gr.sizeof_char),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature

        self.sps = sps = 6

        dict = {1: {6: [-1-1j, -1+1j, 1+1j, 1-1j], 8: [-1-1j, -1+1j, 1+1j, 1-1j]},
                2: {6: [-0.5115-1.2092j, -1.2092-0.5115j, -0.2663-0.4530j, -0.4530-0.2663j, -0.5115+1.2092j, -1.2092+0.5115j, -0.2663+0.4530j, -0.4530+0.2663j, 0.5115+1.2092j, 1.2092+0.5115j, 0.2663+0.4530j, 0.4530+0.2663j, 0.5115-1.2092j, 1.2092-0.5115j, 0.2663-0.4530j, 0.4530-0.2663j], 10: [-0.4487-1.1657j, -1.2080-0.5377j, -0.2213-0.4416j, -0.6186-0.2544j, -0.4487+1.1657j, -1.2080+0.5377j, -0.2213+0.4416j, -0.6186+0.2544j, 0.4487+1.1657j, 1.2080+0.5377j, 0.2213+0.4416j, 0.6186+0.2544j, 0.4487-1.1657j, 1.2080-0.5377j, 0.2213-0.4416j, 0.6186-0.2544j], 13: [-0.9517-0.9511j, -0.9524-0.3061j, -0.3067-0.9524j, -0.3061-0.3067j, -0.9517+0.9511j, -0.9524+0.3061j, -0.3067+0.9524j, -0.3061+0.3067j, 0.9517+0.9511j, 0.9524+0.3061j, 0.3067+0.9524j, 0.3061+0.3067j, 0.9517-0.9511j, 0.9524-0.3061j, 0.3067-0.9524j, 0.3061-0.3067j]},
                3: {6: [-1-1j, -1+1j, 1+1j, 1-1j], 8: [-1-1j, -1+1j, 1+1j, 1-1j]},
                4: {6: [-1-1j, -1+1j, 1+1j, 1-1j], 8: [-1-1j, -1+1j, 1+1j, 1-1j]},
                5: {6: [-1-1j, -1+1j, 1+1j, 1-1j], 8: [-1-1j, -1+1j, 1+1j, 1-1j]}}

        dict1 = {1: [0, 1, 3, 2], 2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15], 3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]}

        select = dict[constellation][rate]
        select1 = dict1[constellation]

        self.constel = constel = digital.constellation_calcdist(select, select1, 4, 1).base()

        self.constel.gen_soft_dec_lut(8)

        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=constel,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
        )


        # Define blocks and connect them
        self.connect(self, self.digital_constellation_modulator_0)
        self.connect(self.digital_constellation_modulator_0, self)
