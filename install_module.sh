#!/bin/bash
sudo rm -r build
mkdir build && cd build
cmake ../
make
sudo make install
ldconfig
gnuradio-companion
