# Boas-vindas ao repositório do TING!

# Entregáveis

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />


Neste projeto será implementado um programa que simule um algoritmo de indexação de documentos similar ao do Google. Esse programa deverá ser capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido por será ter dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

:eyes: **Neste projeto não irá focar na análise de significados ou busca por sinônimos.**


🚵 Habilidades exercitadas:

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸dev-requirements.txt
  ├──🔸pyproject.toml
  ├──🔸README.md
  ├──🔸requirements.txt
  ├──🔸setup.cfg
  ├──🔸setup.py
  ├──statics
  │   ├──🔸arquivo_teste.csv
  │   ├──🔸arquivo_teste.txt
  │   ├──🔸nome_pedro.txt
  │   ├──🔸novo_paradigma_globalizado-min.txt
  │   └──🔸novo_paradigma_globalizado.txt
  ├──tests
  │   ├──🔸__init__.py
  │   ├──🔸test_file_mangement.py
  │   ├──🔸test_file_process.py
  │   ├──🔸test_queue.py
  │   └──🔸test_word_search.py
  ├──ting_file_management
  │   ├──🔹file_management.py
  │   ├──🔹file_process.py
  │   ├──🔸__init__.py
  │   └──🔹queue.py
  ├──ting_word_searches
  │   ├──🔸__init__.py
  │   └──🔹word_search.py
  └──🔸trybe.yml
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas. Para utilizar este recurso siga os passos a seguir:

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo as dependências serão instaladas neste ambiente.
  
  :eyes: Caso precise desativar o ambiente virtual execute o comando _"deactivate"_.
  
  :warning: Lembre-se de ativar o ambiente virtual novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

 👀 **Para executar os testes certifique-se de que você está com o ambiente virtual ativado.**

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

</details>

# Requisitos Obrigatórios

### 1 - Implemente uma fila para armazenar os arquivos que serão lidos.

- Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- A fila (Queue) deve ser uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila deve implementar os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila deverá ser exposto utilizando o método `__len__` que permitirá, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 1.1 - Será validado que o método `enqueue` deve adicionar um elemento à fila, modificando seu tamanho;

- 1.2 - Será validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho;

- 1.3 - Será validado que o método `search` deve retornar um valor da fila a partir de um índice válido e;

- 1.4 - Será validado que o método `search` deve lançar a exceção `IndexError` quando o índice for inválido.
</details>

### 2 - Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

- Caso o arquivo TXT não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

<details>
<summary><b>Exemplo simples de um arquivo txt a ser importado</b></summary>

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- 2.1 - Será validado que o método `txt_importer` deve retornar uma lista contendo as linhas do arquivo;

- 2.2 - Será validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo e;

- 2.3 - Será validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida a mensagem `Formato inválido` na `stderr`.
</details>

### 3 - Implemente uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o pré-processamento do conteúdo.

- A função irá receber como parâmetro a fila implementada no requisito 1 e o caminho do arquivo;

- A instância da fila recebida por parâmetro deve ser utilizada para registrar o processamento dos arquivos;

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, que tenham o mesmo caminho);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

<details>
<summary><b>Exemplo da estrutura de saída:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 3.1 - Será validado que ao executar a função `process` com um arquivo já existente na fila a execução deverá ignorá-lo e;

- 3.2 - Será validado que ao executar a função `process` com sucesso deverá mostrar dados via `stdout`.
</details>

### 4 - Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função irá receber como parâmetro a fila implementada no requisito 1.

- Caso não existam arquivos na fila, a função deve apenas emitir a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, deve ser emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 4.1 - Será validado que ao executar a função `remove` com sucesso deverá exibir mensagem correta via `stdout` e;

- 4.2 - Será validado que ao executar a função `remove` um arquivo inexistente deverá exibir a mensagem correta via `stdout`.
</details>

### 5 - Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.


- A função irá receber como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

<details>
<summary><b>Exemplo da estrutura de saída em caso de sucesso:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 5.1 - Será validado que ao executar a função `file_metadata` com sucesso deverá exibir a mensagem correta via `stdout` e;

- 5.2 - Será validado que ao executar a função `file_metadata` com posição inválida deverá exibir a mensagem correta via `stderr`.
</details>

## Pacote `ting_word_searches`

### 6 - Implemente uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

- A função irá receber como parâmetros a palavra a ser buscada e a fila implementada no requisito 1;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- A busca deve ser _case insensitive_ (não diferenciar maiúsculas e minúsculas);

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 2
    },
    {
      "linha": 7
    }
  ]
}]
````
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- 6.1 - Será validado que ao executar a função `exists_word` com sucesso deverá retornar a estrutura correta;

- 6.2 - Será validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia e;

- 6.3 - Será validado que ao executar a função `exists_word` a fila original não deverá ser alterada.
</details>

### 7 - Implemente uma função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.

- Esta função deverá seguir os mesmos critérios do requisito seis, mas deverá incluir na saída o conteúdo das linhas encontradas, conforme exemplo da estrutura de retorno.

:eyes: **De olho na dica:** este requisito é uma ótima oportunidade para reforçar a prática de código limpo!

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 3,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 4,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
````
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- 7.1 - Será validado que ao executar a função `search_by_word` com sucesso deverá retornar a estrutura correta;

- 7.2 - Será validado que ao executar a função `search_by_word` com palavra inexistente deverá retornar uma lista vazia e;

- 7.3 - Será validado que ao executar a função `search_by_word` a fila original não deverá ser alterada.
</details>
