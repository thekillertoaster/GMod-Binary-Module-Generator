# Minimal MSVC toolchain for local builds and CI
set(CMAKE_SYSTEM_NAME Windows)

# Prefer Ninja + cl.exe; you can override via env if needed
if(NOT DEFINED CMAKE_C_COMPILER)
  set(CMAKE_C_COMPILER cl)
endif()
if(NOT DEFINED CMAKE_CXX_COMPILER)
  set(CMAKE_CXX_COMPILER cl)
endif()

# Reasonable default flags
add_compile_definitions(
  _CRT_SECURE_NO_WARNINGS
  NOMINMAX
  WIN32_LEAN_AND_MEAN
  GMMODULE
)

# Don’t inject "lib" prefix for MODULE libs (also set in target properties)
set(CMAKE_SHARED_LIBRARY_PREFIX "")

# Allow parent preset to decide the runtime; if not set, use the DLL CRT
if(POLICY CMP0091)
  cmake_policy(SET CMP0091 NEW)
  if(NOT DEFINED CMAKE_MSVC_RUNTIME_LIBRARY)
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>DLL")
  endif()
endif()
