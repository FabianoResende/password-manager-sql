# 🔐 Gerenciador de Senhas em Python + SQLite

Um projeto didático desenvolvido para praticar **Python**, **SQL (SQLite)** e **versionamento com Git/GitHub**.  
O aplicativo funciona via terminal e permite gerar, salvar, listar, consultar e apagar senhas de forma simples e organizada.

---

## 🚀 Funcionalidades

- ✔️ Gera senhas aleatórias com diferentes tamanhos  
- ✔️ Salva as senhas em um banco SQLite (`passwords.db`)  
- ✔️ Lista todas as senhas cadastradas  
- ✔️ Mostra detalhes de uma senha específica  
- ✔️ Apaga senhas pelo ID  
- ✔️ Código organizado em módulos (`generator.py`, `database.py`, `app.py`)

---

## 🗂 Estrutura do Projeto

```
password-manager-sql/
│
├── app.py           # Menu principal e fluxo do programa
├── generator.py     # Gerador de senhas
├── database.py      # Conexão e operações no SQLite
├── passwords.db     # Banco de dados (opcional no Git)
└── README.md        # Documentação do projeto
```

---

## 🛠 Tecnologias e Ambiente

- **Linguagem:** Python 3.10
- **Banco de Dados:** SQLite3
- **IDE:** PyCharm 2024
- **Versionamento:** Git & GitHub

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/FabianoResende/gerenciador-de-senhas-sql.git
```

2. Entre na pasta:

```bash
cd gerenciador-de-senhas-sql
```

3. Execute o programa:

```bash
python app.py
```

---

## 📸 Exemplo de Uso

```
=== GERENCIADOR DE SENHAS ===
1 - Gerar e salvar nova senha
2 - Listar senhas salvas
3 - Ver senha específica
4 - Apagar senha
0 - Sair
Escolha uma opção: 1
Serviço (ex: Gmail): fabianofresende
Usuário (opcional): Fabiano
Tamanho da senha (padrão 12): 8

Senha gerada: A9#kP2!x
Salvar no banco? (s/n): s
Senha salva com sucesso!
```

---

## 📌 Melhorias Futuras

- 🔒 Criptografar as senhas antes de salvar  
- 🖥 Criar uma interface gráfica (Tkinter ou PyQt)  
- 🌐 Criar uma API para acessar as senhas  
- 📱 Criar uma versão mobile  

---

## 👨‍💻 Autor

**Fabiano Resende**  
Estudante de Sistemas de Informação | Python, Java e SQL  
Repositório: `https://github.com/FabianoResende` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2FFabianoResende")

```

---


