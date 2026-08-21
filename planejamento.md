# Planejamento do Projeto (FutebolData)

## ✅ Fases Concluídas
- [x] **Repositório:** Inicialização do Git, configuração do repositório remoto e criação do `.gitignore` correto.
- [x] **Banco de Dados:** Criação do script de schema inicial em PostgreSQL (`sql/schema.sql`).
- [x] **Modelagem ORM:** Transição do SQL puro para o SQLAlchemy ORM (`models.py`), mapeando Tabelas, Tipos e Chaves Primárias.
- [x] **Inteligência de IDs (Teams):** Lógica no `functions.py` para mapear os times pelo `TM_ID_API` (garantindo independência de APIs futuras).
- [x] **Extração de Ligas:** Integração do endpoint de Ligas da ESPN para extrair e criar as competições no banco dinamicamente.
- [x] **Relacionamento Many-to-Many:** Automatização da tabela de ligação (`FUT_LEAGUES_TEAMS`) salvando quais times jogam em quais ligas.

## 🚀 Fases Pendentes (O que falta fazer)

### 1. Refatoração e Organização (Clean Code)
- [ ] Refatorar a função `register_log` para usar o ORM do SQLAlchemy (atualmente ainda usa raw SQL com strings).
- [ ] Separar as responsabilidades: Mover as funções de extração da API para a pasta `etl/` e usar o `functions.py` só como central.

### 2. Novas Coletas (Core do Projeto)
- [ ] **Classificação (Standings):** Desenvolver a lógica para bater no endpoint de tabela/classificação e salvar no banco.
- [ ] **Partidas (Fixtures / Scoreboard):** Implementar a lógica da função `get_scoreboard` para resgatar placares e status dos jogos.

### 3. Armazenamento Bruto (Data Lake)
- [ ] Implementar rotina para salvar o retorno bruto da API (arquivos `.json`) dentro da pasta `data/raw/` antes de gravar no banco, servindo como backup.

### 4. Deploy e Automação
- [ ] Mover o código para a nuvem (ex: Render ou AWS).
- [ ] Configurar rotinas agendadas (Cron Jobs) para atualizar o banco de dados diariamente ou ao vivo durante as partidas.
