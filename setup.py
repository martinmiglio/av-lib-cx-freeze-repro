from cx_Freeze import Executable, setup

PROJECT_NAME = "av-lib-cx-freeze-repro"
ENTRY_POINT = "src\\main.py"
VERSION = "dev"


build_exe_options = {
    "excludes": ["test", "setuptools"],
    "includes": ["av"],  # can't include av.libs (module not found)
}


exe = Executable(
    script=ENTRY_POINT,
    target_name=f"{PROJECT_NAME}.exe",
)

setup(
    name=PROJECT_NAME,
    executables=[exe],
    options={
        "build_exe": build_exe_options,
    },
)
