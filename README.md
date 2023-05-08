# (AINDA EM CONSTRUÇÃO) Minhas Tarefas (Sistema)

## Descrição do Projeto

Sistema, com uma API e Cliente WEB, para controle de tarefas.

Com ele, será possível criar, editar e deletar tarefas.

## Execute a versão atual

Para facilitar a execução do projeto, foi construído um Colab, que automatiza todo o processo. Para acessa-lo, basta ir ao link [Minhas Tarefas - Sistema - Colab](https://colab.research.google.com/drive/17wfMChRn8GpyV0ip21IBKOqMCUfdPLV0?usp=sharing#forceEdit=true&sandboxMode=true), e seguir o passo a passo definido lá. Bom testes!

## Informações Técnicas

### Banco de Dados e ORM

Para o Banco de Dados, foi escolhido o SQLite, por ser um banco de dados mais simples. O que vai funcionar muito bem para o sistema.

Para o ORM, foi escolhido o PonyORM, por ser um ORM leve, porém completo.

#### Configurações do Banco de Dados e ORM

Para definir as configurações, foi escolhido user Variáveis de Ambiente.

O projeto, por padrão, utiliza uma instancia de SQLite, mas o configurador (config.py) foi escrito para dar suporte a todos [os providers](https://docs.ponyorm.org/firststeps.html#database-binding), que o PonyORM fornece.

### Modelo de Dados

Os modelos são:

- User
  - full_name: str
  - email: str
  - hashed_password: str
  - tasks: list[Task]

- Task
  - title: str
  - description: str
  - done: bool
  - user: User
