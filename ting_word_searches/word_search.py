def exists_word(word, instance):
    data = []
    for index in range(len(instance)):
        counts_words = []
        file = instance.search(index)
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                counts_words.append(
                    {
                        "linha": index + 1
                    }
                )
        if len(counts_words) > 0:
            data.append(
                {
                    'palavra': word,
                    'arquivo': file['nome_do_arquivo'],
                    'ocorrencias': counts_words
                }
            )

    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
