#include <GarrysMod/Lua/Interface.h>
#include "{{cookiecutter.module_slug}}/module.hpp"

#pragma clang diagnostic push
#pragma ide diagnostic ignored "ConstantFunctionResult"

GMOD_MODULE_OPEN()
{
    gm_print(LUA, "Hello from {{cookiecutter.module_name}} module!");
    return 0;
}

GMOD_MODULE_CLOSE()
{
    gm_print(LUA, "Goodbye from {{cookiecutter.module_name}} module!");
    return 0;
}
