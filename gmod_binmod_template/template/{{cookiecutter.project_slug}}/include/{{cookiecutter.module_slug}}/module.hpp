#pragma once
#include <GarrysMod/Lua/Interface.h>

inline void gm_print(GarrysMod::Lua::ILuaBase *LUA, const char *string) {
    LUA->PushSpecial(GarrysMod::Lua::SPECIAL_GLOB);
    LUA->GetField(-1, "print");
    LUA->PushString(string);
    LUA->Call(1, 0);
    LUA->Pop();
}