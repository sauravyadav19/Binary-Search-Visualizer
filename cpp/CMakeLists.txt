cmake_minimum_required(VERSION 3.10)
project(binary_search_cpp)

set(CMAKE_CXX_STANDARD 17)

# Add pybind11 from the submodule
add_subdirectory(pybind11)

# Create Python module
pybind11_add_module(binary_search_cpp binary_search.cpp)