import sys


def txt_importer(path_file):

    if path_file.endswith('.txt'):
        try:
            with open(path_file, mode='r', encoding='utf8') as f:
                contents = f.read().splitlines()
                return contents

        except Exception:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    else:
        print("Formato inválido", file=sys.stderr)
