#!/usr/bin/env python3
"""
Gera os 14 notebooks práticos básicos (Hands-on) para o curso de Ciência dos Dados (Versão 2026).
"""
import os
import json

def create_notebook(aula_id, title, subtitle, objectives, cells_data):
    """
    Gera arquivo de notebook Jupyter limpo e padronizado.
    """
    colab_badge = (
        f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        f"(https://colab.research.google.com/github/neylemkeunesp/CienciaDados2026/blob/main/{aula_id}/{aula_id}_Pratica.ipynb)"
    )
    
    header_lines = [
        f"# {title}",
        f"### {subtitle}",
        f"**Prof. Dr. Ney Lemke** | *UNESP -- Instituto de Biociências de Botucatu*",
        colab_badge,
        "",
        "---",
        "### 🎯 Objetivos Práticos da Aula:",
    ]
    for obj in objectives:
        header_lines.append(f"- {obj}")
    header_lines.append("---")
    
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [l + "\n" for l in "\n".join(header_lines).split("\n")]
        }
    ]
    
    for c_type, content in cells_data:
        if c_type == "md":
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [l + "\n" for l in content.split("\n")]
            })
        elif c_type == "code":
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [l + "\n" for l in content.split("\n")]
            })
            
    nb = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.12"
            },
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    target_path = os.path.join(aula_id, f"{aula_id}_Pratica.ipynb")
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Notebook gerado com sucesso: {target_path}")

def generate_all():
    # ----------------------------------------------------
    # Aula 01: Introdução e Primeiros Passos
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula01",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 01: Primeiros Passos e Verificação do Ambiente Analítico",
        objectives=[
            "Verificar as versões das bibliotecas instaladas no ambiente (Python 3, Pandas, NumPy, etc.)",
            "Praticar operações elementares em Python e atribuição de variáveis",
            "Representar um catálogo de dados histórico (Don Giovanni / Leporello) em estruturas nativas de Python",
            "Executar agregações e contagens elementares sem o uso de bibliotecas externas"
        ],
        cells_data=[
            ("md", "## 1. Verificação do Ambiente de Trabalho\n\nNesta primeira etapa, garantimos que as ferramentas modernas de Ciência de Dados estão acessíveis e com versões atualizadas."),
            ("code", "import sys\nimport os\n\nprint(f'Versão do Python: {sys.version}')\nprint(f'Diretório de trabalho atual: {os.getcwd()}')"),
            ("code", "import numpy as np\nimport pandas as pd\nimport matplotlib\n\nprint(f'NumPy versão: {np.__version__}')\nprint(f'Pandas versão: {pd.__version__}')\nprint(f'Matplotlib versão: {matplotlib.__version__}')"),
            ("md", "## 2. Modelando Dados: O Catálogo de Leporello (Don Giovanni)\n\nVamos modelar o catálogo de conquistas de Don Giovanni descrito por Leporello como uma lista de registros (dicionários)."),
            ("code", "# Dados de registro por região/país\ncatalogo = [\n    {'pais': 'Itália', 'quantidade': 640},\n    {'pais': 'Alemanha', 'quantidade': 231},\n    {'pais': 'França', 'quantidade': 100},\n    {'pais': 'Turquia', 'quantidade': 91},\n    {'pais': 'Espanha', 'quantidade': 1003}\n]\n\nprint('Catálogo de Conquistas:')\nfor reg in catalogo:\n    print(f\"{reg['pais']:<10}: {reg['quantidade']:>5}\")"),
            ("md", "## 3. Agregações e Estatísticas Básicas\n\nCalculando o total de registros e encontrando a região com maior contagem."),
            ("code", "total = sum(reg['quantidade'] for reg in catalogo)\nmaior_reg = max(catalogo, key=lambda x: x['quantidade'])\n\nprint(f'Total acumulado: {total}')\nprint(f\"País com mais registros: {maior_reg['pais']} com {maior_reg['quantidade']}\")"),
            ("md", "## ✍️ Exercícios Práticos da Aula 01\n\n### Exercício 1 (Fixação)\nCalcule a média de registros por país no catálogo de Leporello utilizando apenas funções embutidas de Python (`sum`, `len`)."),
            ("code", "# Seu código aqui\nmedia = total / len(catalogo)\nprint(f'Média por país: {media:.2f}')"),
            ("md", "### Exercício 2 (Aplicação)\nCrie uma lista contendo apenas os países que possuem mais de 200 registros."),
            ("code", "# Seu código aqui\npaises_mais_200 = [reg['pais'] for reg in catalogo if reg['quantidade'] > 200]\nprint(f'Países com mais de 200 registros: {paises_mais_200}')"),
            ("md", "### Exercício 3 (Desafio)\nCalcule a porcentagem que a Espanha representa sobre o total de registros do catálogo."),
            ("code", "# Seu código aqui\nespanha_qtd = next(reg['quantidade'] for reg in catalogo if reg['pais'] == 'Espanha')\npercentual_espanha = (espanha_qtd / total) * 100\nprint(f'A Espanha representa {percentual_espanha:.1f}% do catálogo.')")
        ]
    )

    # ----------------------------------------------------
    # Aula 02: O Ecossistema Jupyter e Reprodutibilidade
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula02",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 02: O Ecossistema Jupyter, Markdown Técnico e Comandos Mágicos",
        objectives=[
            "Compreender a diferença entre modo de comando e modo de edição no Jupyter",
            "Praticar a escrita de documentação técnica com Markdown e fórmulas matemáticas em LaTeX",
            "Utilizar comandos mágicos do IPython (`%timeit`, `%whos`, `%pwd`, `!`) para inspeção do ambiente",
            "Garantir a reprodutibilidade da análise através da ordem de execução sequencial das células"
        ],
        cells_data=[
            ("md", "## 1. Documentação Técnica com Markdown e LaTeX\n\nNo Jupyter, podemos misturar texto formatado, listas e equações matemáticas com notação LaTeX:\n\nEquação em linha: $f(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} e^{-\\frac{1}{2}\\left(\\frac{x-\\mu}{\\sigma}\\right)^2}$\n\nEquação em bloco:\n$$\\bar{x} = \\frac{1}{n} \\sum_{i=1}^{n} x_i$$"),
            ("md", "## 2. Comandos Mágicos do IPython (Magics)\n\nComandos que começam com `%` (linha) ou `%%` (célula) fornecem recursos especiais de medição de desempenho e controle do kernel."),
            ("code", "# Medição de tempo de execução com %timeit\n%timeit sum(range(100_000))"),
            ("code", "# Listando todas as variáveis atualmente ativas no Kernel\nx = 42\ny = 'Ciência de Dados'\nz = [1, 2, 3, 4]\n\n%whos"),
            ("code", "# Executando comando do sistema operacional\n!python3 --version"),
            ("md", "## ✍️ Exercícios Práticos da Aula 02\n\n### Exercício 1 (Markdown e LaTeX)\nCrie uma célula markdown abaixo contendo:\n1. Um título de nível 2.\n2. Uma lista com três nomes de bibliotecas Python de Ciência de Dados.\n3. A fórmula do Teorema de Pitágoras em notação LaTeX inline ($a^2 + b^2 = c^2$)."),
            ("code", "# Espaço para anotações de código, se necessário"),
            ("md", "### Exercício 2 (Benchmarking com %timeit)\nCompare o tempo de execução para criar uma lista de números ao quadrado de 0 a 10.000 usando:\na) Loop `for` tradicional com `.append()`\nb) List Comprehension `[i**2 for i in range(10_000)]`"),
            ("code", "# Teste A: loop tradicional\ndef cria_loop():\n    l = []\n    for i in range(10_000):\n        l.append(i**2)\n    return l\n\n%timeit cria_loop()"),
            ("code", "# Teste B: List comprehension\n%timeit [i**2 for i in range(10_000)]")
        ]
    )

    # ----------------------------------------------------
    # Aula 03: Paradigmas e Tipos de Dados
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula03",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 03: Paradigmas de Programação, Operadores e Tipagem em Python",
        objectives=[
            "Explorar os tipos primitivos fundamentais (`int`, `float`, `str`, `bool`) e conversões de tipo",
            "Utilizar operadores aritméticos, relacionais e lógicos com precisão",
            "Comparar abordagens imperativas vs funcionais (`map`, `filter`, funções puras)",
            "Aplicar Type Hints básicos do Python moderno para documentação de funções"
        ],
        cells_data=[
            ("md", "## 1. Tipos de Dados Primitivos e Type Casting\n\nPython é uma linguagem dinamicamente tipada, porém fortemente tipada."),
            ("code", "a = 10          # int\nb = 3.14159     # float\nc = 'UNESP'     # str\nd = True        # bool\n\nprint(type(a), type(b), type(c), type(d))"),
            ("code", "# Conversão explícita de tipos (Casting)\nstr_num = '123'\nnum = int(str_num)\nfloat_num = float(num)\nprint(f'Valor: {float_num}, Tipo: {type(float_num)}')"),
            ("md", "## 2. Paradigma Imperativo vs Funcional\n\nVamos calcular a soma dos quadrados dos números pares de 1 a 10 de duas formas."),
            ("code", "# Abordagem 1: Imperativa (instruindo o passo a passo com mutação de estado)\nsoma_imperativa = 0\nfor x in range(1, 11):\n    if x % 2 == 0:\n        soma_imperativa += x ** 2\n\nprint(f'Soma imperativa: {soma_imperativa}')"),
            ("code", "# Abordagem 2: Funcional (composição de funções puras e imutabilidade)\npares = filter(lambda x: x % 2 == 0, range(1, 11))\nquadrados = map(lambda x: x ** 2, pares)\nsoma_funcional = sum(quadrados)\n\nprint(f'Soma funcional: {soma_funcional}')"),
            ("md", "## ✍️ Exercícios Práticos da Aula 03\n\n### Exercício 1 (Operadores e Tipagem)\nEscreva uma função com type hints que receba um peso em kg (float) e uma altura em metros (float), calcule o IMC e retorne o valor com duas casas decimais."),
            ("code", "def calcula_imc(peso: float, altura: float) -> float:\n    return round(peso / (altura ** 2), 2)\n\nprint(f'IMC: {calcula_imc(70.0, 1.75)}')"),
            ("md", "### Exercício 2 (Estilo Funcional)\nDada a lista de temperaturas em Celsius `[0, 15, 20, 25, 30]`, utilize `map` e uma função lambda para convertê-las para Fahrenheit: $F = C \\times 1.8 + 32$."),
            ("code", "celsius = [0, 15, 20, 25, 30]\nfahrenheit = list(map(lambda c: c * 1.8 + 32, celsius))\nprint(f'Fahrenheit: {fahrenheit}')")
        ]
    )

    # ----------------------------------------------------
    # Aula 04: Ambiente Unix/Linux e Linha de Comando
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula04",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 04: Ferramentas Unix/Linux para Inspeção Rápida de Dados",
        objectives=[
            "Utilizar o bash diretamente do notebook via comandos mágicos (`!`)",
            "Inspecionar arquivos de texto brutos sem estourar a memória RAM (`head`, `tail`, `wc`)",
            "Filtrar e ordenar registros com utilitários de fluxo (`grep`, `sort`, `cut`)",
            "Reconhecer a importância do pré-processamento rápido em linha de comando"
        ],
        cells_data=[
            ("md", "## 1. Navegação e Inspeção de Arquivos\n\nAntes de carregar conjuntos de dados de dezenas de gigabytes no Python, cientistas de dados inspecionam sua estrutura com ferramentas Unix."),
            ("code", "# Verificando os arquivos da pasta da aula de manipulação (Aula08)\n!ls -lh ../Aula08/"),
            ("code", "# Inspecionando as primeiras 5 linhas de um arquivo texto\n!head -n 5 ../Aula08/texto.txt"),
            ("code", "# Contando linhas, palavras e caracteres (wc)\n!wc -l ../Aula08/texto.txt"),
            ("md", "## 2. Filtragem e Pipelines Unix\n\nPodemos combinar comandos com pipes (`|`) para filtrar e contar ocorrências."),
            ("code", "# Filtrando linhas que contêm a palavra 'dados' (case insensitive)\n!grep -i 'dados' ../Aula08/texto.txt | wc -l"),
            ("md", "## ✍️ Exercícios Práticos da Aula 04\n\n### Exercício 1 (Inspeção de CSV)\nUtilize o comando `head` para exibir as primeiras 3 linhas do arquivo `../Aula08/matriznum.csv`."),
            ("code", "!head -n 3 ../Aula08/matriznum.csv"),
            ("md", "### Exercício 2 (Contagem de Linhas)\nDescubra quantas linhas de dados existem no arquivo `../Aula08/matriznum.csv` utilizando `wc -l`."),
            ("code", "!wc -l ../Aula08/matriznum.csv")
        ]
    )

    # ----------------------------------------------------
    # Aula 05: Fundamentos de Python: Strings e Coleções
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula05",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 05: Manipulação Eficiente de Strings e Formatação Moderna",
        objectives=[
            "Dominar métodos essenciais de limpeza e transformação de strings (`split`, `strip`, `replace`, `join`)",
            "Utilizar f-strings modernas para interpolação e formatação numérica avançada",
            "Trabalhar com fatiamento (`slicing`) de sequências",
            "Sanitizar dados textuais brutos comumente encontrados em cadastros e logs"
        ],
        cells_data=[
            ("md", "## 1. Métodos de Limpeza de Texto\n\nDados textuais do mundo real frequentemente contêm espaços excedentes, pontuações indesejadas e variações de caixa."),
            ("code", "registro = '   Dr. Ney Lemke;  Física Médica ; UNESP   \\n'\n\n# Limpando espaços externos e separando por ponto-e-vírgula\ncampos = [campo.strip() for campo in registro.split(';')]\nprint(f'Campos limpos: {campos}')"),
            ("code", "# Transformações de caixa e substituição\nfrase = 'ciência dos dados na física médica'\nprint(frase.upper())\nprint(frase.title())\nprint(frase.replace('física médica', 'saúde'))"),
            ("md", "## 2. F-Strings Modernas e Fatiamento\n\nAs f-strings do Python permitem controle direto de alinhamento e precisão numérica."),
            ("code", "pi = 3.1415926535\nvalor = 1250.75\n\nprint(f'Pi formatado: {pi:.3f}')\nprint(f'Moeda alinhada: R$ {valor:>10.2f}')"),
            ("code", "# Fatiamento [início:fim:passo]\ntexto = 'Python2026'\nprint(texto[0:6])   # 'Python'\nprint(texto[6:])    # '2026'\nprint(texto[::-1])  # Invertido"),
            ("md", "## ✍️ Exercícios Práticos da Aula 05\n\n### Exercício 1 (Higienização de CPFs)\nDada a lista de documentos `[' 123.456.789-00 ', '987.654.321-11\\n', '111.222.333-44']`, crie uma nova lista contendo apenas os dígitos numéricos limpos."),
            ("code", "docs = [' 123.456.789-00 ', '987.654.321-11\\n', '111.222.333-44']\ndocs_limpos = [d.strip().replace('.', '').replace('-', '') for d in docs]\nprint(f'CPFs normalizados: {docs_limpos}')"),
            ("md", "### Exercício 2 (Extração de Domínio de E-mail)\nEscreva uma função que receba um e-mail (ex: `aluno@unesp.br`) e retorne apenas o domínio (ex: `unesp.br`)."),
            ("code", "def extrai_dominio(email: str) -> str:\n    return email.strip().split('@')[-1]\n\nprint(extrai_dominio('ney.lemke@unesp.br'))")
        ]
    )

    # ----------------------------------------------------
    # Aula 06: Estruturas de Dados e Algoritmos
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula06",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 06: Estruturas de Dados Fundamentais e Comprehensions",
        objectives=[
            "Trabalhar com as quatro coleções centrais: Listas, Tuplas, Dicionários e Conjuntos (`set`)",
            "Compreender a eficiência de busca $O(1)$ em dicionários/conjuntos versus $O(n)$ em listas",
            "Utilizar List Comprehensions e Dict Comprehensions para transformações limpas",
            "Agrupar e contar frequências em coleções de dados"
        ],
        cells_data=[
            ("md", "## 1. As Quatro Coleções Nativas de Python\n\n- **Lista (`list`)**: ordenada, mutável, permite duplicatas.\n- **Tupla (`tuple`)**: ordenada, imutável (ideal para registros fixos).\n- **Conjunto (`set`)**: não-ordenado, mutável, elementos únicos (busca rápida $O(1)$).\n- **Dicionário (`dict`)**: pares chave-valor, chaves únicas."),
            ("code", "idades = [21, 25, 21, 30, 25, 19, 21]\n\n# Deduplicação instantânea com set\nidades_unicas = set(idades)\nprint(f'Original: {idades}')\nprint(f'Únicos: {idades_unicas}')"),
            ("md", "## 2. Comprehensions (Listas e Dicionários)\n\nForma idiomática e de alta performance para mapear e filtrar coleções."),
            ("code", "# Quadrados dos números pares de 0 a 10\nquadrados_pares = [x**2 for x in range(11) if x % 2 == 0]\nprint(f'Quadrados pares: {quadrados_pares}')\n\n# Dict comprehension: mapeando palavra -> seu tamanho\npalavras = ['dados', 'ciência', 'python', 'análise']\ntamanhos = {p: len(p) for p in palavras}\nprint(f'Mapeamento de tamanhos: {tamanhos}')"),
            ("md", "## ✍️ Exercícios Práticos da Aula 06\n\n### Exercício 1 (Contagem de Frequências)\nDada uma lista de diagnósticos clínicos, conte quantas vezes cada diagnóstico aparece utilizando um dicionário."),
            ("code", "diagnosticos = ['Gripe', 'Covid', 'Dengue', 'Gripe', 'Covid', 'Gripe', 'Resfriado']\n\ncontagem = {}\nfor diag in diagnosticos:\n    contagem[diag] = contagem.get(diag, 0) + 1\n\nprint(f'Frequências: {contagem}')"),
            ("md", "### Exercício 2 (Operações com Conjuntos)\nDados dois conjuntos de pacientes que realizaram exames A e B, encontre:\na) Pacientes que fizeram ambos os exames.\nb) Pacientes que fizeram apenas o exame A."),
            ("code", "exame_a = {'P01', 'P02', 'P03', 'P04', 'P05'}\nexame_b = {'P03', 'P05', 'P06', 'P07'}\n\nambos = exame_a.intersection(exame_b)\napenas_a = exame_a.difference(exame_b)\n\nprint(f'Fizeram ambos: {ambos}')\nprint(f'Apenas exame A: {apenas_a}')")
        ]
    )

    # ----------------------------------------------------
    # Aula 07: Controle de Fluxo e Funções
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula07",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 07: Controle de Fluxo, Funções Modulares e Boas Práticas",
        objectives=[
            "Aplicar estruturas condicionais e laços de repetição de forma idiomática",
            "Utilizar funções utilitárias `enumerate()` e `zip()` para iteração sobre múltiplos conjuntos",
            "Definir funções com documentação (docstrings), valores padrão e `*args`",
            "Tratar erros e exceções comuns em processamento de dados (`try/except`)"
        ],
        cells_data=[
            ("md", "## 1. Iteração Idiomática com `enumerate` e `zip`"),
            ("code", "pacientes = ['Ana', 'Bruno', 'Carla', 'Daniel']\nidades = [24, 31, 28, 45]\n\n# zip para iterar em paralelo\nfor nome, idade in zip(pacientes, idades):\n    print(f'{nome} tem {idade} anos.')"),
            ("code", "# enumerate para obter índice e elemento simultaneamente\nfor idx, nome in enumerate(pacientes, start=1):\n    print(f'Paciente #{idx}: {nome}')"),
            ("md", "## 2. Funções Modulares e Robustas"),
            ("code", "def estatisticas_basicas(valores: list[float]) -> dict[str, float]:\n    \"\"\"\n    Calcula média, mínimo e máximo de uma lista numérica.\n    \"\"\"\n    if not valores:\n        raise ValueError('A lista não pode estar vazia.')\n    \n    return {\n        'media': sum(valores) / len(valores),\n        'minimo': min(valores),\n        'maximo': max(valores)\n    }\n\nprint(estatisticas_basicas([10.5, 20.0, 15.2, 33.1]))"),
            ("md", "## ✍️ Exercícios Práticos da Aula 07\n\n### Exercício 1 (Função com Validação e Tratamento de Erros)\nEscreva uma função `converte_para_float(lista_strings)` que converta cada elemento para float, ignorando valores que causem `ValueError` (ex: `'N/A'`, `'ausente'`)."),
            ("code", "def converte_para_float(lista: list[str]) -> list[float]:\n    validos = []\n    for item in lista:\n        try:\n            validos.append(float(item))\n        except ValueError:\n            continue\n    return validos\n\ndados_brutos = ['12.5', '30.1', 'N/A', '45.0', 'invalido', '2.8']\nprint(f'Valores numéricos convertidos: {converte_para_float(dados_brutos)}')"),
            ("md", "### Exercício 2 (Classificador Simples com if/elif/else)\nCrie uma função que classifique o nível de glicose em jejum: `< 100` (Normal), `100 a 125` (Pré-diabetes), `>= 126` (Diabetes)."),
            ("code", "def classifica_glicose(valor: float) -> str:\n    if valor < 100:\n        return 'Normal'\n    elif valor <= 125:\n        return 'Pré-diabetes'\n    else:\n        return 'Diabetes'\n\nprint(classifica_glicose(95))\nprint(classifica_glicose(110))\nprint(classifica_glicose(140))")
        ]
    )

    # ----------------------------------------------------
    # Aula 08: Manipulação de Arquivos e I/O
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula08",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 08: Entrada/Saída de Arquivos e Leitura de Dados Compactados",
        objectives=[
            "Utilizar gerenciadores de contexto (`with open`) para manipulação segura de arquivos",
            "Ler arquivos de texto linha por linha de forma eficiente em memória",
            "Ler diretamente arquivos compactados com `gzip` sem descompactá-los no disco",
            "Processar arquivos CSV estruturados usando o módulo padrão `csv.reader`"
        ],
        cells_data=[
            ("md", "## 1. Leitura de Arquivo Texto com Gerenciador de Contexto (`with`)"),
            ("code", "with open('texto.txt', 'r', encoding='utf-8') as f:\n    linhas = [linha.strip() for linha in f.readlines() if linha.strip()]\n\nprint(f'Total de linhas lidas: {len(linhas)}')\nprint(f'Primeira linha: {linhas[0]}')"),
            ("md", "## 2. Leitura Direta de Arquivo Compactado (`.gz`)"),
            ("code", "import gzip\n\n# Lendo arquivo comprimido da estação de outono\nwith gzip.open('arq_abril_outono.txt.gz', 'rt', encoding='utf-8') as f:\n    primeiras_linhas = [f.readline().strip() for _ in range(5)]\n\nfor l in primeiras_linhas:\n    print(l)"),
            ("md", "## ✍️ Exercícios Práticos da Aula 08\n\n### Exercício 1 (Parsing de CSV Manual)\nLeia o arquivo `matriznum.csv` (delimitado por espaços) usando o módulo `csv` e calcule a soma dos valores da primeira coluna numérica."),
            ("code", "import csv\n\nvalores_col1 = []\nwith open('matriznum.csv', 'r', encoding='utf-8') as f:\n    leitor = csv.reader(f, delimiter=' ')\n    for linha in leitor:\n        linha_limpa = [x for x in linha if x]\n        if linha_limpa:\n            try:\n                valores_col1.append(float(linha_limpa[0]))\n            except ValueError:\n                continue\n\nprint(f'Valores coletados: {valores_col1}')\nprint(f'Soma da primeira coluna: {sum(valores_col1):.2f}')"),
            ("md", "### Exercício 2 (Escrita de Arquivo de Relatório)\nGere um arquivo `relatorio_aula08.txt` salvando a contagem de elementos e a média calculada."),
            ("code", "media_col1 = sum(valores_col1) / len(valores_col1) if valores_col1 else 0.0\nwith open('relatorio_aula08.txt', 'w', encoding='utf-8') as f:\n    f.write('Relatório de Processamento - Aula 08\\n')\n    f.write(f'Quantidade de elementos: {len(valores_col1)}\\n')\n    f.write(f'Média: {media_col1:.2f}\\n')\n\nprint('Relatório gerado com sucesso.')")
        ]
    )

    # ----------------------------------------------------
    # Aula 09: Análise de Dados com Pandas I
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula09",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 09: Análise de Dados com Pandas I: Series, DataFrames e Indexação",
        objectives=[
            "Compreender a estrutura de `pd.Series` e `pd.DataFrame`",
            "Carregar dados tabulares a partir de arquivos CSV (`pd.read_csv`)",
            "Realizar indexação rigorosa com `.loc` (rótulos) e `.iloc` (posições inteiras)",
            "Aplicar filtros com máscaras booleanas combinadas (`&`, `|`, `~`)"
        ],
        cells_data=[
            ("md", "## 1. Criação e Inspeção de DataFrames"),
            ("code", "import pandas as pd\n\n# Criando um DataFrame a partir de um dicionário\ndados = {\n    'paciente': ['P01', 'P02', 'P03', 'P04', 'P05'],\n    'idade': [25, 42, 60, 31, 55],\n    'glicose': [92, 115, 140, 88, 128],\n    'grupo': ['Controle', 'Tratamento', 'Tratamento', 'Controle', 'Tratamento']\n}\n\ndf = pd.DataFrame(dados)\ndf"),
            ("code", "# Inspeção sumária\nprint(df.info())\nprint('\\nEstatísticas Numéricas:')\nprint(df.describe())"),
            ("md", "## 2. Indexação e Filtragem Booleana\n\n- `.loc`: seleção baseada em nomes de colunas e rótulos de índice.\n- `.iloc`: seleção baseada estritamente em índices inteiros posicionais."),
            ("code", "# Selecionando linha 0 a 2 e colunas 'paciente' e 'glicose'\nprint(df.loc[0:2, ['paciente', 'glicose']])\n\n# Selecionando com iloc (posições 0 e 1, colunas 0 e 1)\nprint(df.iloc[0:2, 0:2])"),
            ("code", "# Filtro booleano: pacientes do grupo 'Tratamento' com glicose >= 120\nmascara = (df['grupo'] == 'Tratamento') & (df['glicose'] >= 120)\ndf[mascara]"),
            ("md", "## ✍️ Exercícios Práticos da Aula 09\n\n### Exercício 1 (Cálculo de Novas Colunas)\nCrie uma nova coluna chamada `idade_meses` que corresponda à idade do paciente multiplicada por 12."),
            ("code", "df['idade_meses'] = df['idade'] * 12\ndf"),
            ("md", "### Exercício 2 (Agrupamento Descritivo Simples)\nCalcule a média de glicose e de idade para cada um dos grupos (`Controle` vs `Tratamento`)."),
            ("code", "df.groupby('grupo')[['idade', 'glicose']].mean()")
        ]
    )

    # ----------------------------------------------------
    # Aula 10: Pandas II: Limpeza, Agregação e Transformação (ETL)
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula10",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 10: Pandas II: Pipeline de Limpeza, Agregação (GroupBy) e Junções (Merge)",
        objectives=[
            "Identificar e tratar valores ausentes (`isna`, `dropna`, `fillna`)",
            "Aplicar o paradigma Split-Apply-Combine utilizando `groupby` e agregações com `.agg()`",
            "Combinar diferentes tabelas de dados utilizando `pd.merge()` e `pd.concat()`",
            "Estruturar um pipeline básico de transformação de dados (ETL)"
        ],
        cells_data=[
            ("md", "## 1. Tratamento de Dados Ausentes (Missing Values)"),
            ("code", "import pandas as pd\nimport numpy as np\n\ndf_sujo = pd.DataFrame({\n    'id': [101, 102, 103, 104, 105],\n    'temperatura': [36.5, np.nan, 38.2, 37.0, np.nan],\n    'pressao': [120, 130, np.nan, 125, 118],\n    'setor': ['A', 'A', 'B', 'B', 'A']\n})\n\nprint('Valores nulos por coluna:')\nprint(df_sujo.isna().sum())"),
            ("code", "# Imputação de missing pela mediana da coluna\nmediana_temp = df_sujo['temperatura'].median()\ndf_limpo = df_sujo.copy()\ndf_limpo['temperatura'] = df_limpo['temperatura'].fillna(mediana_temp)\ndf_limpo"),
            ("md", "## 2. Agregações Complexas com GroupBy"),
            ("code", "# Agrupando por setor e calculando múltiplas métricas com .agg()\nresumo_setor = df_limpo.groupby('setor').agg(\n    temp_media=('temperatura', 'mean'),\n    temp_max=('temperatura', 'max'),\n    contagem=('id', 'count')\n)\nresumo_setor"),
            ("md", "## 3. Junção de Tabelas (Merge)"),
            ("code", "df_meta = pd.DataFrame({\n    'setor': ['A', 'B'],\n    'responsavel': ['Dra. Julia', 'Dr. Roberto'],\n    'andar': [2, 3]\n})\n\n# Inner join relacionando pacientes ao responsável pelo setor\ndf_completo = pd.merge(df_limpo, df_meta, on='setor', how='left')\ndf_completo"),
            ("md", "## ✍️ Exercícios Práticos da Aula 10\n\n### Exercício 1 (Detecção de Linhas Completas)\nUtilize `dropna()` para gerar um novo DataFrame contendo apenas as linhas que não possuíam nenhum valor nulo no `df_sujo` original."),
            ("code", "df_sem_nulos = df_sujo.dropna()\ndf_sem_nulos"),
            ("md", "### Exercício 2 (Agregação Customizada)\nCalcule o desvio padrão e a média da pressão arterial por responsável médico no `df_completo`."),
            ("code", "df_completo.groupby('responsavel')['pressao'].agg(['mean', 'std'])")
        ]
    )

    # ----------------------------------------------------
    # Aula 11: Computação Numérica com NumPy
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula11",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 11: Computação Científica de Alta Performance com NumPy",
        objectives=[
            "Criar e manipular arrays multidimensionais (`np.ndarray`) com tipos definidos (`dtype`)",
            "Comparar a performance da computação vetorizada versus laços em Python com `%timeit`",
            "Aplicar as regras de Broadcasting em operações entre arrays de dimensões distintas",
            "Realizar fatiamento multidimensional e filtragem condicional em matrizes"
        ],
        cells_data=[
            ("md", "## 1. Criação e Propriedades de Arrays"),
            ("code", "import numpy as np\n\narr_1d = np.array([10, 20, 30, 40, 50], dtype=np.float64)\narr_zeros = np.zeros((3, 4))\narr_seq = np.linspace(0, 1, 11)  # 11 pontos igualmente espaçados de 0 a 1\n\nprint(f'Shape arr_zeros: {arr_zeros.shape}')\nprint(f'Dtype: {arr_1d.dtype}')\nprint(f'Sequência linspace:\\n{arr_seq}')"),
            ("md", "## 2. Vetorização vs Laços Puros (Benchmark)"),
            ("code", "tamanho = 1_000_000\nlista_python = list(range(tamanho))\narr_numpy = np.arange(tamanho)\n\n# Medindo tempo de elevação ao quadrado em Python puro\n%timeit [x**2 for x in lista_python]\n\n# Medindo tempo com vetorização NumPy\n%timeit arr_numpy ** 2"),
            ("md", "## 3. Broadcasting na Prática\n\nO NumPy estende automaticamente arrays com dimensões compatíveis para realizar operações sem cópia explícita de dados."),
            ("code", "matriz = np.array([\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n])\n\nvetor = np.array([10, 20, 30])\n\n# Somando vetor (1, 3) a cada linha da matriz (3, 3)\nsoma_broadcasting = matriz + vetor\nprint(soma_broadcasting)"),
            ("md", "## ✍️ Exercícios Práticos da Aula 11\n\n### Exercício 1 (Normalização Min-Max)\nDado o array `dados = np.array([15, 23, 18, 45, 12, 89, 34])`, normalize seus valores no intervalo $[0, 1]$ usando a fórmula: $x_{norm} = \\frac{x - x_{min}}{x_{max} - x_{min}}$."),
            ("code", "dados = np.array([15, 23, 18, 45, 12, 89, 34])\ndados_norm = (dados - dados.min()) / (dados.max() - dados.min())\nprint(f'Normalizado: {dados_norm}')"),
            ("md", "### Exercício 2 (Filtro Booleano em Matriz)\nCrie uma matriz $4 \\times 4$ de números aleatórios entre 0 e 100 (`np.random.default_rng(42)`) e substitua todos os valores menores que 50 por zero."),
            ("code", "rng = np.random.default_rng(42)\nmatriz_aleatoria = rng.integers(0, 100, size=(4, 4))\nprint('Original:\\n', matriz_aleatoria)\n\nmatriz_aleatoria[matriz_aleatoria < 50] = 0\nprint('\\nModificada (valores < 50 zerados):\\n', matriz_aleatoria)")
        ]
    )

    # ----------------------------------------------------
    # Aula 12: Visualização de Dados I: Matplotlib
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula12",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 12: Visualização de Dados com Matplotlib: Interface Orientada a Objetos",
        objectives=[
            "Dominar a anatomia de um gráfico no Matplotlib (`Figure` e `Axes`)",
            "Utilizar a interface Orientada a Objetos (`fig, ax = plt.subplots()`) recomendada",
            "Criar gráficos de dispersão (`scatter`), linhas e barras com formatação completa",
            "Exportar figuras prontas para publicação científica em alta resolução"
        ],
        cells_data=[
            ("md", "## 1. A Interface Orientada a Objetos (`plt.subplots`)"),
            ("code", "import matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\n# Dados sintéticos de calibração instrumental\ntempo = np.linspace(0, 10, 50)\nsinal = 2.5 * np.sin(tempo) + np.random.normal(0, 0.2, size=50)\n\nfig, ax = plt.subplots(figsize=(8, 4), dpi=100)\nax.plot(tempo, sinal, color='#0F2B45', linewidth=2, label='Sinal Medido')\nax.set_title('Resposta Temporal do Sensor', fontsize=14, fontweight='bold', pad=12)\nax.set_xlabel('Tempo (s)', fontsize=12)\nax.set_ylabel('Tensão (mV)', fontsize=12)\nax.grid(True, linestyle='--', alpha=0.5)\nax.legend(frameon=True)\nplt.tight_layout()\nplt.show()"),
            ("md", "## 2. Gráficos de Dispersão com Dataset Real"),
            ("code", "# Carregando o conjunto de dados automotivo\ndf_carros = pd.read_csv('Automobile price data.csv')\n\n# Limpeza simples de valores não numéricos em 'price' e 'horsepower'\ndf_carros['price'] = pd.to_numeric(df_carros['price'], errors='coerce')\ndf_carros['horsepower'] = pd.to_numeric(df_carros['horsepower'], errors='coerce')\ndf_carros_clean = df_carros.dropna(subset=['price', 'horsepower'])\n\nfig, ax = plt.subplots(figsize=(8, 5))\nscatter = ax.scatter(\n    df_carros_clean['horsepower'],\n    df_carros_clean['price'],\n    c=df_carros_clean['city-mpg'],\n    cmap='viridis',\n    alpha=0.7,\n    edgecolors='none'\n)\ncbar = fig.colorbar(scatter, ax=ax)\ncbar.set_label('Consumo Urbano (City MPG)')\n\nax.set_title('Relação entre Potência (HP) e Preço de Automóveis', fontsize=13)\nax.set_xlabel('Potência (Horsepower)')\nax.set_ylabel('Preço (USD)')\nax.grid(True, linestyle=':', alpha=0.6)\nplt.tight_layout()\nplt.show()"),
            ("md", "## ✍️ Exercícios Práticos da Aula 12\n\n### Exercício 1 (Gráfico de Barras Médio)\nCrie um gráfico de barras exibindo o preço médio dos automóveis por tipo de combustível (`fuel-type`)."),
            ("code", "preco_combustivel = df_carros_clean.groupby('fuel-type')['price'].mean()\n\nfig, ax = plt.subplots(figsize=(6, 4))\nax.bar(preco_combustivel.index, preco_combustivel.values, color=['#1B4973', '#0E7C86'], width=0.5)\nax.set_title('Preço Médio por Tipo de Combustível')\nax.set_ylabel('Preço Médio (USD)')\nax.grid(axis='y', linestyle='--', alpha=0.6)\nplt.tight_layout()\nplt.show()"),
            ("md", "### Exercício 2 (Exportação de Gráfico em Alta Resolução)\nSalve o gráfico do exercício anterior em arquivo PNG com resolução de 300 DPI utilizando `fig.savefig('preco_combustivel.png', dpi=300)`."),
            ("code", "fig.savefig('preco_combustivel.png', dpi=300)\nprint('Figura exportada com sucesso.')")
        ]
    )

    # ----------------------------------------------------
    # Aula 13: Visualização Estatística com Seaborn
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula13",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 13: Visualização Estatística Avançada com Seaborn",
        objectives=[
            "Explorar distribuições univariadas e bivariadas (`sns.histplot`, `sns.kdeplot`)",
            "Identificar assimetrias e outliers com Boxplots e Violin plots",
            "Mapear dimensões categóricas em gráficos de dispersão (`hue`, `style`, `size`)",
            "Calcular matrizes de correlação e visualizá-las com mapas de calor (`sns.heatmap`)"
        ],
        cells_data=[
            ("md", "## 1. Visualização de Distribuições e Outliers"),
            ("code", "import seaborn as sns\nimport matplotlib.pyplot as plt\nimport pandas as pd\n\nsns.set_theme(style='whitegrid', palette='deep')\n\ndf_carros = pd.read_csv('Automobile price data.csv')\ndf_carros['price'] = pd.to_numeric(df_carros['price'], errors='coerce')\ndf_carros['horsepower'] = pd.to_numeric(df_carros['horsepower'], errors='coerce')\ndf_carros_clean = df_carros.dropna(subset=['price', 'horsepower', 'fuel-type', 'body-style'])\n\nfig, axes = plt.subplots(1, 2, figsize=(12, 4))\n\n# Histograma com curva KDE\nsns.histplot(df_carros_clean['price'], kde=True, ax=axes[0], color='#1B4973')\naxes[0].set_title('Distribuição de Preços (Assimetria Positiva)')\n\n# Boxplot comparativo por carroceria\nsns.boxplot(data=df_carros_clean, x='body-style', y='price', ax=axes[1])\naxes[1].set_title('Preço por Tipo de Carroceria')\naxes[1].tick_params(axis='x', rotation=30)\n\nplt.tight_layout()\nplt.show()"),
            ("md", "## 2. Matriz de Correlação e Heatmap"),
            ("code", "colunas_numericas = ['price', 'horsepower', 'city-mpg', 'highway-mpg', 'curb-weight', 'engine-size']\nfor col in colunas_numericas:\n    df_carros_clean[col] = pd.to_numeric(df_carros_clean[col], errors='coerce')\n\ncorr_matrix = df_carros_clean[colunas_numericas].dropna().corr()\n\nplt.figure(figsize=(7, 5))\nsns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.2f', linewidths=0.5)\nplt.title('Matriz de Correlação de Pearson')\nplt.tight_layout()\nplt.show()"),
            ("md", "## ✍️ Exercícios Práticos da Aula 13\n\n### Exercício 1 (Scatterplot Categórico)\nUtilize `sns.scatterplot()` para cruzar `engine-size` (eixo X) com `price` (eixo Y), diferenciando as cores (`hue`) pelo tipo de combustível (`fuel-type`)."),
            ("code", "plt.figure(figsize=(8, 5))\nsns.scatterplot(\n    data=df_carros_clean,\n    x='engine-size',\n    y='price',\n    hue='fuel-type',\n    alpha=0.8,\n    s=70\n)\nplt.title('Preço vs Tamanho do Motor por Combustível')\nplt.tight_layout()\nplt.show()")
        ]
    )

    # ----------------------------------------------------
    # Aula 14: Introdução ao Aprendizado de Máquina (Scikit-Learn)
    # ----------------------------------------------------
    create_notebook(
        aula_id="Aula14",
        title="Ciência dos Dados I: Análise Exploratória (2026)",
        subtitle="Aula 14: Introdução ao Aprendizado de Máquina com Scikit-Learn",
        objectives=[
            "Compreender a API padrão do Scikit-Learn (`fit`, `predict`, `transform`)",
            "Ajustar um modelo de Regressão Linear e interpretar coeficientes e métricas ($R^2$, RMSE)",
            "Visualizar a reta de regressão ajustada sobre os dados reais",
            "Aplicar o algoritmo de agrupamento não-supervisionado K-Means e identificar centróides"
        ],
        cells_data=[
            ("md", "## 1. Aprendizado Supervisionado: Regressão Linear\n\nVamos prever o preço de um automóvel com base em sua potência (`horsepower`)."),
            ("code", "import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import r2_score, mean_squared_error\n\n# Carregando dados\ndf = pd.read_csv('Automobile price data.csv')\ndf['price'] = pd.to_numeric(df['price'], errors='coerce')\ndf['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')\ndf_reg = df.dropna(subset=['price', 'horsepower'])\n\n# Matriz de features X (2D) e vetor target y (1D)\nX = df_reg[['horsepower']]\ny = df_reg['price']\n\n# Instanciando e treinando o modelo\nmodelo = LinearRegression()\nmodelo.fit(X, y)\n\ny_pred = modelo.predict(X)\n\nprint(f'Coeficiente Angular (Slope): {modelo.coef_[0]:.2f}')\nprint(f'Intercepto: {modelo.intercept_:.2f}')\nprint(f'R² Score: {r2_score(y, y_pred):.3f}')\nprint(f'RMSE: {np.sqrt(mean_squared_error(y, y_pred)):.2f}')"),
            ("code", "# Visualizando o ajuste\nplt.figure(figsize=(8, 5))\nplt.scatter(X, y, color='#1B4973', alpha=0.6, label='Dados Reais')\nplt.plot(X, y_pred, color='#D97706', linewidth=2.5, label='Reta de Regressão')\nplt.title('Regressão Linear: Preço vs Potência')\nplt.xlabel('Potência (Horsepower)')\nplt.ylabel('Preço (USD)')\nplt.legend()\nplt.grid(True, linestyle='--', alpha=0.5)\nplt.tight_layout()\nplt.show()"),
            ("md", "## 2. Aprendizado Não-Supervisionado: Clusterização K-Means\n\nIdentificando grupos naturais de veículos combinando potência e consumo de combustível."),
            ("code", "from sklearn.cluster import KMeans\nfrom sklearn.preprocessing import StandardScaler\n\ndf_reg['city-mpg'] = pd.to_numeric(df_reg['city-mpg'], errors='coerce')\nX_cluster = df_reg[['horsepower', 'city-mpg']].dropna()\n\n# Padronização de escala (essencial para métodos baseados em distância)\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X_cluster)\n\n# Ajuste de K-Means com k=3 clusters\nkmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')\nX_cluster['cluster'] = kmeans.fit_predict(X_scaled)\n\nplt.figure(figsize=(8, 5))\nsns_plot = plt.scatter(X_cluster['horsepower'], X_cluster['city-mpg'], c=X_cluster['cluster'], cmap='tab10', alpha=0.7)\nplt.title('Agrupamento K-Means (k=3)')\nplt.xlabel('Potência (HP)')\nplt.ylabel('Consumo (City MPG)')\nplt.grid(True, linestyle=':', alpha=0.6)\nplt.colorbar(sns_plot, label='Cluster')\nplt.tight_layout()\nplt.show()"),
            ("md", "## ✍️ Exercícios Práticos da Aula 14\n\n### Exercício 1 (Predição com o Modelo Treinado)\nUtilize o modelo de Regressão Linear treinado para prever o preço estimado de um veículo com 150 HP e de outro com 220 HP."),
            ("code", "novos_veiculos = pd.DataFrame({'horsepower': [150, 220]})\npredicoes = modelo.predict(novos_veiculos)\nfor hp, preco in zip([150, 220], predicoes):\n    print(f'Veículo com {hp} HP -> Preço estimado: R$ {preco:,.2f}')")
        ]
    )

if __name__ == "__main__":
    generate_all()
