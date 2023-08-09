echo "Configuring and building Thirdparty/DBoW2 ..."

cd Thirdparty/DBoW2
mkdir -p build
cd build
rm -f CMakeCache.txt

cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

cd ../../g2o

echo "Configuring and building Thirdparty/g2o ..."

mkdir -p build
cd build
rm -f CMakeCache.txt
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

cd ../../Sophus

echo "Configuring and building Thirdparty/Sophus ..."

mkdir -p build
cd build
rm -f CMakeCache.txt
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

cd ../../../

echo "Uncompress vocabulary ..."

cd Vocabulary
tar -xf ORBvoc.txt.tar.gz
cd ..

echo "Configuring and building ORB_SLAM3 ..."

mkdir -p build
cd build
rm -f CMakeCache.txt
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)