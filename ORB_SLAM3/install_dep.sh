git clone https://gitlab.com/libeigen/eigen.git -b 3.3.9 Thirdparty/eigen
git clone https://github.com/stevenlovegrove/Pangolin.git -b v0.8  Thirdparty/Pangolin

cd Thirdparty/eigen
mkdir -p build
cd build
rm -f CMakeCache.txt
cmake ..
make -j$(nproc) 
make install

cd ../../../Thirdparty/Pangolin
mkdir -p build
cd build
rm -f CMakeCache.txt
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc) 
make install

