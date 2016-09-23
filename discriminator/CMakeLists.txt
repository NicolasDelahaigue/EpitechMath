cmake_minimum_required(VERSION 3.3)
project(discriminator)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

### source
file(GLOB   SRC     src/*)
file(GLOB   CORE    src/core/*)
file(GLOB   LOADER  src/loader/*)
file(GLOB   ALGO    src/algo/*)
file(GLOB   QTREE   src/core/quadtree/*)

### include
include_directories(.)
include_directories(src/*)
include_directories(src/loader/*)
include_directories(src/core/*)
include_directories(src/algo/*)
include_directories(src/core/quadtree/*)

### executable
add_executable(
        discriminator
        ${SRC}
        ${CORE}
        ${LOADER}
        ${ALGO}
        ${QTREE}
)
