#!/usr/bin/env bash

mkdir -p pdf_slides

for aula in Aula01 Aula02 Aula03 Aula04 Aula05 Aula06 Aula07 Aula08 Aula09 Aula10 Aula11 Aula12 Aula13 Aula14; do
    num="${aula//Aula/}"
    num_lower=$(echo "$num" | tr '[:upper:]' '[:lower:]')
    tex_file="${aula}/slides_aula${num_lower}.tex"
    
    if [ -f "$tex_file" ]; then
        echo "=================================================="
        echo "Compilando: $tex_file"
        echo "=================================================="
        pdflatex -interaction=nonstopmode -output-directory="$aula" "$tex_file" > /dev/null 2>&1 || true
        pdflatex -interaction=nonstopmode -output-directory="$aula" "$tex_file" > /dev/null 2>&1 || true
        
        pdf_file="${aula}/slides_aula${num_lower}.pdf"
        if [ -f "$pdf_file" ]; then
            cp "$pdf_file" "pdf_slides/${aula}_Slides.pdf"
            echo "✔ Gerado com sucesso: pdf_slides/${aula}_Slides.pdf"
        else
            echo "❌ Erro ao gerar PDF para $aula"
        fi
    else
        echo "Aviso: $tex_file não encontrado."
    fi
done

echo ""
echo "Todos os slides disponíveis foram processados!"
ls -lh pdf_slides/
