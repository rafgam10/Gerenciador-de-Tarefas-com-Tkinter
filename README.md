# Gerenciador de Tarefas com Tkinter e ttkbootstrap

Este projeto consiste em uma aplicação simples para gerenciar tarefas utilizando Python, Tkinter e a biblioteca ttkbootstrap para estilização.

---

## Funcionalidades

1. **Adicionar Tarefas**:
   - Permite ao usuário adicionar tarefas ao painel de exibição.

2. **Marcar como Completo**:
   - Atualiza a tarefa selecionada, alterando o fundo do texto para indicar que foi concluída.

3. **Remover Tarefas**:
   - Remove a tarefa selecionada da lista.

4. **Atalhos do Programa**:
   - Atalhos para cada função do programa, permitindo maior agilidade.

---

## Código Fonte

### Estrutura de Arquivos
O projeto está organizado da seguinte forma:

```
Gerenciador de Tarefas/
├── env
├── resources/ #Pasta de icones e img
    ├── icons 
    ├── img
├── app.py                # Arquivo principal que inicializa a interface
├── utils/
│   ├── constants.py      # Variáveis de configuração e constantes globais
│   ├── function.py       # Funções e classes para gerenciamento de tarefas
├── img/
│   ├── screenshot_vazio.png
│   ├── tela_cheia_tarefa.png
├── requirements.txt      # Requisisão do projeto
└── README.md             # Documentação do projeto
```

---

## Interface Principal

### Arquivo `app.py`

```python
from tkinter import *
from ttkbootstrap import Style
from utils.function import criar_task

# CONFIGURAÇÃO DA PÁGINA:

root = Tk()
style = Style(theme="superhero")
root.title("Gerenciador de Tarefas")
root.geometry("600x900")

# Campo de entrada para adicionar tarefas
entry_nome_tarefa = ttk.Entry(root, width=50)
entry_nome_tarefa.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botão para adicionar tarefa
button_add = ttk.Button(
    root, text="Adicionar - Enter", width=15, command=lambda: criar_task(entry_nome_tarefa, root)
)
button_add.grid(row=0, column=5, columnspan=8, padx=10, pady=20)

# Separador horizontal
separador = ttk.Separator(root, orient="horizontal")
separador.grid(row=1, column=0, columnspan=20, sticky="ew", padx=10, pady=20)

# Atalhos do Programa
root.bind("<Return>", lambda event: criar_task(entry_nome_tarefa, root))

# Iniciar o loop principal
root.mainloop()
```

---

### Arquivo `utils/function.py`

```python
from tkinter import END
from ttkbootstrap import ttk
from .constants import *

class ModelTask:
    def __init__(self, root, nome_tarefa):
        global linhaN

        # Criação da Task
        self.label_inst = ttk.Label(
            root,
            text=nome_tarefa,
            font=("Ariel", 16),
            background="#4e5d6c",
            width=20,
            anchor="w",
            relief="solid",
            justify="center"
        )
        self.label_inst.grid(row=linhaN, column=colunaLabelN, padx=5, pady=5)

        self.button_check = ttk.Button(
            root,
            text="Check",
            width=5,
            bootstyle=verde,
            command=self.check_task
        )
        self.button_check.grid(row=linhaN, column=colunaButtonCheckN, padx=5, pady=5)

        self.button_delete = ttk.Button(
            root,
            text=" X ",
            width=5,
            bootstyle=vermelho,
            command=self.delete_task
        )
        self.button_delete.grid(row=linhaN, column=colunaButtonDeleteN, padx=5, pady=5)

    def check_task(self):
        self.label_inst.configure(background="#5cb85c")

    def delete_task(self):
        self.label_inst.destroy()
        self.button_check.destroy()
        self.button_delete.destroy()
        lista_de_task.remove(self)

def criar_task(entry, root):
    global linhaN, lista_de_task

    nome_tarefa = entry.get()
    if nome_tarefa:
        linhaN += 1
        task = ModelTask(root, nome_tarefa)
        lista_de_task.append(task)
        entry.delete(0, END)
```

---

## Imagem do Projeto

Imagens do projeto para melhor visualização:

![Gerenciador de Tarefas](/resources/img/todo_vazio.png)

![Gerenciador de Tarefas](/resources/img/todo_cheio.png)

---

## Dependências

- Python 3.12 ou superior.
- Biblioteca ttkbootstrap.

### Instalação de Dependências

Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate   # Windows
pip install ttkbootstrap
```

---

## Como Executar o Projeto

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o script Python:

```bash
python app.py
```

---

## Melhorias Futuras

- Adicionar suporte à persistência de dados (salvar tarefas em um arquivo).
- Melhorar a interface com novos temas e ícones.
- Adicionar opção para editar tarefas já existentes.

--- 

### **Principais Ajustes**
1. Incluí a estrutura de arquivos para melhor clareza do projeto.
2. Alinhei os exemplos de código ao formato atual.
3. Adicionei os atalhos e funcionalidades destacando sua importância.
4. Melhorar o Frontend.