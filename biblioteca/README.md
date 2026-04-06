# Sistema de Gerenciamento de Biblioteca 📚

Sistema interativo via terminal para gerenciamento de acervo de livros, desenvolvido em Python.
O projeto simula um cenário real de controle de empréstimos e devoluções de uma biblioteca,
aplicando lógica de programação, funções, estruturas de dados e tratamento de erros.

---

## 🚀 Funcionalidades

- ✅ Listar todos os livros com status de disponibilidade
- ✅ Emprestar livro (altera status para **Emprestado**)
- ✅ Devolver livro (altera status para **Disponível**)
- ✅ Buscar livros por autor
- ✅ Exibir estatísticas do acervo (total, disponíveis, emprestados)
- ✅ Menu interativo com loop contínuo

---

## 🛡️ Validações implementadas

| Situação | Comportamento |
|---|---|
| Opção inválida no menu | Exibe mensagem de erro e retorna ao menu |
| Letra digitada no menu | Trata com `try/except` sem quebrar o programa |
| Livro já emprestado | Informa que o livro não está disponível |
| Livro já devolvido | Informa que o livro já está na biblioteca |
| Título inexistente | Informa que o livro não foi encontrado |
| Autor inexistente | Informa que o autor não consta no acervo |

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
cd exercicios-logica-python/sistema-biblioteca

# Execute o script
python biblioteca.py