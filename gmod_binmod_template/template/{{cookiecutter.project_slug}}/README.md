# {{cookiecutter.project_name}}

To get started, you can either use an IDE (CLion) with the provided CMake profiles, or you can build the project using CLI commands.

## Building with CLI
1. Open `Developer PowerShell for VS 2022` or `Developer Command Prompt for VS 2022`.
2. Navigate to the project directory:
    ```shell
   cd "C:/path/to/your/project/{{cookiecutter.project_slug}}"
    ```
3. Generate CMake configs:
    ```shell
    cmake --preset win # or linux
    ```
4. Build the project:
    ```shell
   cmake --build --preset win-release --parallel # or linux-release
    ```
5. The compiled binary will be located in the `build/` directory.

## Building with CLion
1. Open CLion and select "Open" to open the project directory.
2. CLion should automatically detect the CMake presets. If not, go to `File > Settings > Build, Execution, Deployment > CMake` and enable the listed presets.
3. Select the desired CMake profile (e.g., `Debug` or `Release`) from the top-right corner.
4. Click the build button (hammer icon) to compile the project.
5. The compiled binary will be located in the `build/IDE/` directory.

*CLion uses its own toolchain settings, so ensure that the correct compiler and environment are set up in CLion's settings if you encounter any issues.*

*Provided CLion presets are for windows builds and may not work for linux builds out of the box. It's best to use CLI for that.*