import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    is_duplicate_file = False

    instance_length = instance.__len__()
    for i in range(instance_length):
        searched_dict = instance.search(i)
        if path_file == searched_dict['nome_do_arquivo']:
            is_duplicate_file = True

    if is_duplicate_file is False:
        txt_importation = txt_importer(path_file)

        insert_dict = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(txt_importation),
            'linhas_do_arquivo': txt_importation
        }

        instance.enqueue(insert_dict)

        print(
            f'{insert_dict}',
            file=sys.stdout
        )


def remove(instance):
    if instance is False:
        return print("Não há elementos")
    path = instance.dequeue()["nome_do_arquivo"]
    return print(f"Arquivo {path} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_search = instance.search(position)
        sys.stdout.write(
            str(file_search)
        )
    except IndexError:
        sys.stderr.write(
            str("Posição inválida")
        )
