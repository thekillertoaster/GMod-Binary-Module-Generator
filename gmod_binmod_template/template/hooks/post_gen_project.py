import re
import shutil
import platform
import subprocess
import sys
import urllib.request
import zipfile
import io
import os
import stat
from pathlib import Path

slug = "{{cookiecutter.module_slug}}"
if not re.fullmatch(r"[a-z0-9_]+", slug):
    print("module_slug must be [a-z0-9_]+", file = sys.stderr)
    sys.exit(1)


def fetch_gmod_headers():
    dest = os.path.join(os.getcwd(), "external", "GarrysMod")
    repo = "https://github.com/danielga/garrysmod_common.git"  # or your preferred header repo
    try:
        if not os.path.exists(dest):
            print(f"Fetching Garry's Mod headers into {dest}...")
            subprocess.run(["git", "clone", "--depth=1", repo, dest], check = True)
        else:
            print("Headers already exist, skipping fetch.")
    except Exception as e:
        print(f"⚠️ Could not fetch headers: {e}")


def ensure_ninja():
    if shutil.which("ninja"):
        print("✅ Ninja build system found in PATH.")
        return

    project_root = Path.cwd()
    tools_dir = project_root / ".tools"
    tools_dir.mkdir(exist_ok = True)
    ninja_path = tools_dir / ("ninja.exe" if os.name == "nt" else "ninja")

    if ninja_path.exists():
        print(f"✅ Ninja already present at {ninja_path}")
        return

    # Pick correct binary for the platform
    system = platform.system().lower()
    if system == "windows":
        url = "https://github.com/ninja-build/ninja/releases/latest/download/ninja-win.zip"
    elif system == "linux":
        url = "https://github.com/ninja-build/ninja/releases/latest/download/ninja-linux.zip"
    elif system == "darwin":
        url = "https://github.com/ninja-build/ninja/releases/latest/download/ninja-mac.zip"
    else:
        print("⚠️ Unsupported platform for automatic Ninja install.")
        return

    print(f"⚙️ Downloading Ninja for {system} ...")
    with urllib.request.urlopen(url) as r:
        with zipfile.ZipFile(io.BytesIO(r.read())) as z:
            z.extractall(tools_dir)

    os.chmod(ninja_path, os.stat(ninja_path).st_mode | stat.S_IEXEC)
    print(f"✅ Installed Ninja locally at {ninja_path}")

    # modify CMakePresets.json so builds automatically find it
    # preset = project_root / "CMakePresets.json"
    # if preset.exists():
    #     content = preset.read_text()
    #     if "CMAKE_MAKE_PROGRAM" not in content:
    #         # Append the var to each configurePreset
    #         new_content = content.replace(
    #             '"cacheVariables": {',
    #             '"cacheVariables": {\n      "CMAKE_MAKE_PROGRAM": "${sourceDir}/.tools/ninja${'
    #             'hostSystemName:Windows:?\\.exe:}",'
    #         )
    #         preset.write_text(new_content)
    #         print("🪄 Updated CMakePresets.json to use local Ninja automatically.")


fetch_gmod_headers()
ensure_ninja()
print("✅ Environment ready! Try running:\n  cmake --preset win && cmake --build --preset win-release --parallel")
