# SIGPAT - Sistema Integrado de Gestão de Patrimonial

Projeto Django para gestão patrimonial.

## Pré-requisitos

Certifique-se de que você tenha as seguintes ferramentas instaladas em seu ambiente:

- Python 3.10 ou superior
- Pip (Python package installer)
- Virtualenv (opcional, mas recomendado)

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone git@github.com:JanielMS/SIGPAT-Django.git
   cd SIGPAT-Django
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências:**

   Execute o comando abaixo para instalar as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Caso não exista o arquivo `requirements.txt`, você pode criar um com o seguinte comando:

   ```bash
   pip freeze > requirements.txt
   ```

   **Dependências do projeto:**
   ```
   asgiref==3.8.1
   Django==5.1.6
   sqlparse==0.5.3
   ```


4. **Realize as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Execute o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   O projeto estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Funcionalidades

🔹 Gestão de Bens (CRUD) | <span style="background-color: yellow;">( Em Breve )</span>

   - Cadastro de bens com campos como nome, categoria, número de patrimônio, descrição, valor, data de aquisição etc.
   - Edição e exclusão de bens.
   - Filtro e busca avançada por categoria, departamento ou fornecedor.

🔹 Categorização de Bens | <span style="background-color: yellow;">( Em Breve )</span>


   - Criar e gerenciar categorias de bens.
   - Associar bens às categorias.

🔹 Gestão de Departamentos/Setores | <span style="background-color: yellow;">( Em Breve )</span>

   - Cadastro e gerenciamento dos setores onde os bens estão alocados.
   - Relacionamento entre bens e departamentos.

🔹 Cadastro de Fornecedores | <span style="background-color: yellow;">( Em Breve )</span>

   - Gerenciar informações de fornecedores (nome, CNPJ, contato etc.).
   - Relacionamento entre bens e fornecedores.

🔹 Controle de Movimentações | <span style="background-color: yellow;">( Em Breve )</span>

   - Registro de movimentações dos bens (transferência entre setores, empréstimos, devoluções).
   - Histórico de movimentações.

🔹 Rastreamento por RFID (Opcional) | <span style="background-color: yellow;">( Em Breve )</span>

   - Leitura de etiquetas RFID para identificar bens automaticamente.
   - Atualização automática da localização dos bens.

🔹 Dashboard com Indicadores | <span style="background-color: yellow;">( Em Breve )</span>

   - Número total de ativos cadastrados.
   - Distribuição de ativos por categoria.
   - Status de manutenção (ativos em manutenção, próximos da revisão).
   - Movimentações recentes.
   - Valor total do patrimônio.

🔹 Testes Unitários | <span style="background-color: yellow;">( Em Breve )</span>

   - Cobertura de testes para garantir a integridade do sistema.

🔹 Relatórios e Exportação de Dados | <span style="background-color: yellow;">( Em Breve )</span>

   - Geração de relatórios sobre bens cadastrados, movimentações e categorias.
   - Exportação para formatos como PDF e Excel.

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionei uma nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
**Autor:** Janiel Maia  
[Link do GitHub](https://github.com/JanielMS)