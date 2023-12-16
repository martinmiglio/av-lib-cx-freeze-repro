from cx_Freeze import Executable, setup

PROJECT_NAME = "av-lib-cx-freeze-repro"
ENTRY_POINT = "src\\main.py"
VERSION = "dev"


exe = Executable(
    script=ENTRY_POINT,
    target_name=f"{PROJECT_NAME}.exe",
)

setup(
    name=PROJECT_NAME,
    executables=[exe],
)
