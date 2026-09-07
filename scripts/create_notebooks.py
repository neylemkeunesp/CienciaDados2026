#!/usr/bin/env python3
"""
Gerador dos cadernos práticos padronizados (Material Básico) para o curso Ciência dos Dados (2026).
"""
import json
import os

def make_nb(title, aula_num, subtitle, objectives, sections):
    """
    Cria a estrutura de um notebook Jupyter v4 limpo.
    sections é uma lista de tuplas (tipo, conteudo).
    tipo: 'md' ou 'code'
    """
    colab_badge = (
        f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        f"(https://colab.research.google.com/github/neylemkeunesp/CienciaDados2026/blob/main/{aula_num}/{aula_num}_Pratica.ipynb)"
    )
    
    header_md = f"""# {title}
### {subtitle}
**Prof. Dr. Ney Lemke** | *UNESP -- Instituto de Biociências de Botucatu*  
{colab_badge}

---
### 🎯 Objetivos de Aprendizagem Prática:
""" + "\n".join([f"- {obj}" for obj in objectives]) + "\n\n---"

    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in header_md.split("\n")]
        }
    ]

    for cell_type, content in sections:
        if cell_type == "md":
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [line + "\n" for line in content.split("\n")]
            })
        elif cell_type == "code":
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in content.split("\n")]
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
    return nb

def save_nb(nb_dict, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(nb_dict, f, indent=1, ensure_ascii=False)
    print(f"Salvo: {filepath}")

if __name__ == "__main__":
    print("Módulo de geração de notebooks pronto.")
