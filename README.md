# PyAV with cx_freeze reproduction

Install using poetry:

```bash
poetry install --with build
```

Build using cx_freeze in poetry environment:

```bash
poetry run python setup.py build_exe
```

Execute the generated executable in the build directory:

```bash
./build/exe.win-amd64-3.11/av-lib-cx-freeze-repro.exe
```
