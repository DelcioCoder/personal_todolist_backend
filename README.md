# Gerenciador de Lista de Tarefas (ToDo List)

Este é um projeto de exemplo de um aplicativo de lista de tarefas (ToDo List) construído com Django.

## Funcionalidades Principais do `todolist`

O aplicativo `todolist` permite aos usuários gerenciar suas tarefas de forma eficaz. As principais funcionalidades incluem:

*   **Criação de Tarefas:** Adicionar novas tarefas à lista.
*   **Visualização de Tarefas:** Ver todas as tarefas pendentes e concluídas.
*   **Atualização de Tarefas:** Modificar os detalhes de uma tarefa existente (ex: título, descrição, data de vencimento).
*   **Exclusão de Tarefas:** Remover tarefas da lista.
*   **Marcação de Tarefas como Concluídas:** Indicar que uma tarefa foi finalizada.

## Modelos do `todolist`

O aplicativo `todolist` utiliza os seguintes modelos para organizar os dados:

*   ### `Modality` (Modalidade)
    *   Representa a categoria ou tipo de atividade (ex: Trabalho, Estudo, Pessoal).
    *   Campos:
        *   `name`: Nome da modalidade (texto, obrigatório, máximo de 100 caracteres).
        *   `description`: Descrição da modalidade (texto, opcional).

*   ### `Activity` (Atividade)
    *   Representa uma tarefa específica a ser realizada.
    *   Campos:
        *   `modality`: Chave estrangeira para o modelo `Modality`, indicando a qual modalidade a atividade pertence (obrigatório).
        *   `name`: Nome da atividade (texto, obrigatório, máximo de 150 caracteres).
        *   `description`: Descrição detalhada da atividade (texto, opcional).
        *   `due_date`: Data de vencimento da atividade (data, opcional).
        *   `completed`: Booleano indicando se a atividade foi concluída (padrão: `False`).
        *   `created_at`: Data e hora de criação da atividade (data e hora, adicionado automaticamente).
        *   `updated_at`: Data e hora da última atualização da atividade (data e hora, atualizado automaticamente).

*   ### `Note` (Anotação)
    *   Permite adicionar anotações ou comentários a uma atividade específica.
    *   Campos:
        *   `activity`: Chave estrangeira para o modelo `Activity`, indicando a qual atividade a anotação pertence (obrigatório).
        *   `text`: Conteúdo da anotação (texto, obrigatório).
        *   `created_at`: Data e hora de criação da anotação (data e hora, adicionado automaticamente).

## Outros Aplicativos

O projeto também inclui os seguintes aplicativos Django, que podem ser desenvolvidos futuramente:

*   ### `api`
    *   Este aplicativo será responsável por fornecer uma API RESTful para interagir com os dados do `todolist` e outros possíveis aplicativos. Atualmente, está vazio.

*   ### `user_auth`
    *   Este aplicativo será responsável pela autenticação e gerenciamento de usuários. Atualmente, está vazio.

## Como Contribuir

Informações sobre como contribuir para o projeto serão adicionadas aqui.

## Licença

Informações sobre a licença do projeto serão adicionadas aqui.
