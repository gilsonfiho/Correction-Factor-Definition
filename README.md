# Correction Factor Definition 📈

Este projeto tem como objetivo definir um **fator de correção** para reduzir o erro de medições em um sistema específico — por exemplo, sistemas de aquisição de dados com sensores (como FBGs). O script apresentado permite a análise de resultados medidos versus valores de referência, oferecendo uma maneira eficiente de aplicar correções estatísticas.

---

## 📌 Motivação

Durante o desenvolvimento de projetos que envolvem sensores físicos, é comum observar pequenas discrepâncias entre os valores lidos e os reais. Este repositório surgiu da necessidade de **calibrar medições** com base em dados empíricos e gerar um **fator de correção confiável**, aumentando a precisão do sistema.

---

## 🧠 Como funciona?

O script `main.py` lê os dados de entrada (manualmente definidos ou por arquivos), realiza cálculos estatísticos para determinar o erro médio e, a partir disso, calcula um fator de correção. Esse fator pode então ser aplicado diretamente em outros sistemas ou em tempo real, dependendo da aplicação.

---
