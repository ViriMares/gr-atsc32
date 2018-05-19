/* -*- c++ -*- */
/*
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


#ifndef INCLUDED_ATSC32_CONFIG_H
#define INCLUDED_ATSC32_CONFIG_H
//Para que se usa?
#define TRUE 1
#define FALSE 0
//Longitudes de codigo
#define FRAME_SIZE_NORMAL 64800
#define FRAME_SIZE_SHORT  16200

#define LDPC_ENCODE_TABLE_LENGTH (FRAME_SIZE_NORMAL * 10)

namespace gr {
  namespace atsc32{
    //tasas de codificación
    enum atsc3_code_rate_t {
      C6_15 = 0,
      C7_15,
      C8_15,
      C9_15,
      C10_15,
      C11_15,
    };
    //longitudes de codigo
    enum atsc3_framesize_t {
      FECFRAME_SHORT = 0,
      FECFRAME_NORMAL,
    };

  } // namespace atsc32
} // namespace gr

typedef gr::atsc32::atsc3_code_rate_t atsc3_code_rate_t;
typedef gr::atsc32::atsc3_framesize_t atsc3_framesize_t;

#endif /* INCLUDED_ATSC32_CONFIG_H */

