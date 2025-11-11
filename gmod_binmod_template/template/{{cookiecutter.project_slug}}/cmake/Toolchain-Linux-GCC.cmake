# Minimal GCC/Clang toolchain for Linux
set(CMAKE_SYSTEM_NAME Linux)

# Prefer system compilers; override with CC/CXX if you like
if(NOT DEFINED CMAKE_C_COMPILER)
  set(CMAKE_C_COMPILER gcc)
endif()
if(NOT DEFINED CMAKE_CXX_COMPILER)
  set(CMAKE_CXX_COMPILER g++)
endif()

# Flags common for GMod modules
add_compile_options(-fPIC)
add_compile_definitions(GMMODULE _GNU_SOURCE)

# No "lib" prefix for MODULE libraries
set(CMAKE_SHARED_LIBRARY_PREFIX "")
