cmake_minimum_required(VERSION 3.20)
project({{cookiecutter.project_slug}} CXX)

set(CMAKE_CXX_STANDARD {{cookiecutter.cxx_std}})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_definitions(-DGMMODULE)

# MSVC runtime selection
if(MSVC)
  if(POLICY CMP0091)
    cmake_policy(SET CMP0091 NEW)
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>DLL")
  endif()
  add_compile_options(/permissive- /Zc:__cplusplus)
endif()

# Platform suffix used by GMod's loader
if(WIN32)
  set(GMOD_PLATFORM "win64")
elseif(UNIX)
  set(GMOD_PLATFORM "linux")
else()
  message(FATAL_ERROR "Unsupported platform")
endif()

# Binary prefix: gmsv_* (server) or gmcl_* (client)
set(GMOD_PREFIX "{{ 'gmsv' if cookiecutter.binary_kind == 'server' else 'gmcl' }}")

add_library({{cookiecutter.module_slug}} MODULE
  src/main.cpp
  include/{{cookiecutter.module_slug}}/module.hpp
)

target_include_directories({{cookiecutter.module_slug}} PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/external/GarrysMod/include
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# On Windows, MODULE libraries are .dll; on Linux .so
set_target_properties({{cookiecutter.module_slug}} PROPERTIES
  PREFIX ""  # no "lib" prefix
  OUTPUT_NAME "${GMOD_PREFIX}_{{cookiecutter.module_slug}}_${GMOD_PLATFORM}"
)

# Release-friendly flags
if(CMAKE_BUILD_TYPE MATCHES "Release")
  if(MSVC)
    target_compile_options({{cookiecutter.module_slug}} PRIVATE /O2)
  else()
    target_compile_options({{cookiecutter.module_slug}} PRIVATE -O3)
  endif()
endif()

# Install to a simple dist/ dir
include(GNUInstallDirs)
install(TARGETS {{cookiecutter.module_slug}}
  LIBRARY DESTINATION dist
  RUNTIME DESTINATION dist
  ARCHIVE DESTINATION dist)
