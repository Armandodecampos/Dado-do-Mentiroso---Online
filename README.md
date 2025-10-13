# Configuração do Projeto de Login com Supabase

Este projeto é uma aplicação de página única (SPA) que oferece uma interface completa para autenticação e gestão de perfil, utilizando Supabase como backend.

## Passo 1: Configurar o Backend no Supabase

Antes de a aplicação funcionar, é necessário configurar a base de dados e as políticas de segurança no seu projeto Supabase.

1.  **Crie um Projeto no Supabase**: Se ainda não tiver um, vá a [supabase.com](https://supabase.com/), crie uma conta e inicie um novo projeto.

2.  **Execute o Script SQL**:
    *   No painel do seu projeto Supabase, navegue até ao **SQL Editor**.
    *   Clique em **+ New query**.
    *   Abra o ficheiro `supabase_setup.sql` que se encontra neste projeto.
    *   Copie todo o conteúdo do ficheiro e cole-o no editor de SQL.
    *   Clique em **RUN**.

    Este script irá criar as tabelas `profiles` e `posts`, ativar a Row-Level Security (RLS) e definir as políticas de segurança essenciais para garantir que os utilizadores só possam aceder e modificar os seus próprios dados.

## Passo 2: Configurar o Frontend (`index.htm`)

A aplicação frontend precisa de saber como comunicar com o seu projeto Supabase. Para isso, tem de inserir as suas chaves de API no ficheiro `index.htm`.

1.  **Encontre as Suas Chaves de API**:
    *   No painel do seu projeto Supabase, vá a **Project Settings** > **API**.
    *   Nesta página, irá encontrar o **Project URL** e a chave **anon (public)**.

2.  **Atualize o Ficheiro `index.htm`**:
    *   Abra o ficheiro `index.htm` num editor de código.
    *   Procure pelas seguintes linhas de código (perto da linha 800):

        ```javascript
        const SUPABASE_URL = 'SUA_SUPABASE_URL'; // Substitua com o seu URL do projeto
        const SUPABASE_ANON_KEY = 'SUA_SUPABASE_ANON_KEY'; // Substitua com a sua chave anon (pública)
        ```

    *   **Substitua** `'SUA_SUPABASE_URL'` pelo seu **Project URL**.
    *   **Substitua** `'SUA_SUPABASE_ANON_KEY'` pela sua chave **anon (public)**.

    **Importante**: Não partilhe a sua chave `service_role` (secreta) no lado do cliente. A chave `anon` é segura para ser usada publicamente, desde que a Row-Level Security esteja ativada.

## Passo 3: Executar a Aplicação

Depois de configurar o backend e o frontend, pode executar a aplicação.

*   **Abra o ficheiro `index.htm`** diretamente no seu navegador de internet (ex: Google Chrome, Firefox).

A página de login deverá aparecer, e poderá criar uma conta, fazer login e testar todas as funcionalidades.
