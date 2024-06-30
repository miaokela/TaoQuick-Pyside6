import os
import subprocess


def compile_qrc(qrc_file, output_py):
    result = subprocess.run(
        ["pyside6-rcc", qrc_file, "-o", output_py], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error compiling {qrc_file}: {result.stderr}")
    else:
        print(f"Successfully compiled {qrc_file} to {output_py}")


if __name__ == "__main__":
    qrc_file = "TaoQuick.qrc"
    output_py = "TaoQuick.py"

    compile_qrc(qrc_file, output_py)
