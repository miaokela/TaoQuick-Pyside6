import os
import subprocess


def generate_qrc(directory, output_file):
    with open(output_file, "w") as f:
        f.write("<RCC>\n")
        f.write('    <qresource prefix="/">\n')

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".qml"):
                    file_path = os.path.join(root, file).replace("\\", "/")
                    f.write(f"        <file>{file_path}</file>\n")

        f.write("    </qresource>\n")
        f.write("</RCC>\n")


def compile_qrc(qrc_file, output_py):
    result = subprocess.run(
        ["pyside6-rcc", qrc_file, "-o", output_py], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error compiling {qrc_file}: {result.stderr}")
    else:
        print(f"Successfully compiled {qrc_file} to {output_py}")


if __name__ == "__main__":
    qrc_file = "resources.qrc"
    output_py = "resources_rc.py"

    generate_qrc(".", qrc_file)
    compile_qrc(qrc_file, output_py)
