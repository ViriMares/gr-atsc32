/* -*- c++ -*- */
/* 
 * Copyright 2018 Viridiana Mares, Facultad de Ingeniería UNAM.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_ATSC32_LDPC_ENCODER_BB_IMPL_H
#define INCLUDED_ATSC32_LDPC_ENCODER_BB_IMPL_H

#include <atsc32/ldpc_encoder_bb.h>

typedef struct{
    int table_length;
    int d[LDPC_ENCODE_TABLE_LENGTH];
    int p[LDPC_ENCODE_TABLE_LENGTH];
}ldpc_encode_table;

namespace gr {
  namespace atsc32 {

    class ldpc_encoder_bb_impl : public ldpc_encoder_bb
    {
     private:
        unsigned int frame_size;
        unsigned int nouter;
        unsigned int code_rate;
        unsigned int q_val;
        unsigned int table_length;

        void ldpc_lookup_generate(void);

        ldpc_encode_table ldpc_encode;

        const static int ldpc_tab_6_15N[72][28];
        const static int ldpc_tab_6_15S[18][31];

        const static int ldpc_tab_7_15S[21][25];

        const static int ldpc_tab_8_15N[96][20];
        const static int ldpc_tab_8_15S[24][33];

        const static int ldpc_tab_9_15N[108][20];
        const static int ldpc_tab_9_15S[27][17];

        const static int ldpc_tab_10_15N[120][15];
        const static int ldpc_tab_10_15S[30][26];

        const static int ldpc_tab_11_15N[132][16];
        const static int ldpc_tab_11_15S[33][13];


    public:
      ldpc_encoder_bb_impl(atsc3_framesize_t framesize, atsc3_code_rate_t rate);
      ~ldpc_encoder_bb_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace atsc32
} // namespace gr

#endif /* INCLUDED_ATSC32_LDPC_ENCODER_BB_IMPL_H */

