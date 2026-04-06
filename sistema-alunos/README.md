# Sistema de Cadastro de Alunos 🎓

Sistema interativo via terminal para cadastro e gerenciamento de alunos, desenvolvido em Python.
O projeto simula um cenário real de gestão escolar, aplicando lógica de programação, estruturas de dados e tratamento de erros.

---

## 🚀 Funcionalidades

- ✅ Cadastrar aluno com nome, idade e 3 notas
- ✅ Calcular média automaticamente
- ✅ Classificar como **APROVADO** (média ≥ 7.0) ou **REPROVADO**
- ✅ Listar todos os alunos cadastrados com situação
- ✅ Buscar aluno por nome (busca parcial)
- ✅ Menu interativo com loop contínuo

---

## 🛡️ Validações implementadas

| Campo | Validação |
|---|---|
| Opção do menu | Trata letras e números inválidos |
| Idade | Trata entrada não numérica |
| Notas | Trata letras e valores fora do intervalo (0–10) |
| Busca | Case-insensitive (maiúscula/minúscula) |

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Sem dependências externas — roda direto no terminal

---

## ▶️ Como executar

**Pré-requisito:** ter o Python 3 instalado → [python.org](https://www.python.org/downloads/)

```bash
# Clone o repositório
git clone https://github.com/brenoferreirasouto-lgtm/exercicios-logica-python.git

# Acesse a pasta do projeto
cd exercicios-logica-python/sistema-alunos

# Execute o script
python sistema-alunos.py