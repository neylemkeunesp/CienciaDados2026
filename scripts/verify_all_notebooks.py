#!/usr/bin/env python3
"""
Script de verificação automatizada dos cadernos práticos do curso Ciência dos Dados (2026).
Executa cada célula de código dos 14 notebooks para certificar ausência de erros.
"""
import glob
import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def verify_all_notebooks():
    notebooks = sorted(glob.glob("Aula*/Aula*_Pratica.ipynb"))
    print(f"Iniciando verificação de {len(notebooks)} cadernos práticos...")
    
    ep = ExecutePreprocessor(timeout=60, kernel_name='python3')
    failed = []
    
    for nb_path in notebooks:
        print(f"Executando: {nb_path} ...", end=" ", flush=True)
        aula_dir = os.path.dirname(nb_path)
        try:
            with open(nb_path, "r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
            # Executa com o diretório da própria aula como cwd (para caminhos de arquivos relativos funcionarem)
            ep.preprocess(nb, {'metadata': {'path': aula_dir}})
            print("✔ OK!")
        except Exception as e:
            print(f"❌ FALHA: {e}")
            failed.append((nb_path, str(e)))
            
    print("\n" + "="*50)
    if not failed:
        print(f"SUCESSO TOTAL! Todos os {len(notebooks)} cadernos foram executados sem erros!")
        return 0
    else:
        print(f"{len(failed)} caderno(s) apresentaram falhas:")
        for path, err in failed:
            print(f"- {path}: {err}")
        return 1

if __name__ == "__main__":
    sys.exit(verify_all_notebooks())
