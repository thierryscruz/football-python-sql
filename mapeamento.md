REQUESTS:
    events.id: id da partida
    events.date: horario da partida e dia
    events.name: times partida
    events.competitions.venue.fullName: local da partida
    events.competitions.competitors.id: id do time
    events.competitions.competitors.homeAway: home / away  
    events.competitions.competitors.team.logo: link da logo
    events.competitions.competitors.team.displayName: nome do time
    events.competitions.competitors.score.displayValue: placar do time
    events.competitions.status.type.state: estado da partida(pre, post, in)
    events.competitions.status.type.name: STATUS_SECOND_HALF,STATUS_SCHEDULED,STATUS_FINAL_PEN

SQL:
FUT_LEAGUES:
    LG_ID = id
    LG_NAME = nome da liga
    LG_COUNTRY = PAIS DA LIGA
    LG_TYPE = TIPO DE LIGA (CAMPEONATO, COPA)
    LG_REQUEST = CODIGO REQUEST API

FUT_TEAMS:
    TM_ID = id
    TM_NAME = nome do time
    TM_COUNTRY = PAIS DO TIME
    TM_LOGO = link da logo

FUT_LEAGUES_TEAMS:
    LG_ID = id da liga
    TM_ID = id do time

FUT_MATCHES:
    MT_ID = id
    MT_LEAGUE = id da liga
    MT_DATE = data da partida
    MT_VENUE = local da partida
    MT_HOME = Time da Casa (FK FUT_TEAMS)
    MT_AWAY = Time fora (FK FUT_TEAMS)
    MT_HOME_SCORE = placar do time da casa
    MT_AWAY_SCORE = placar do time fora
    MT_STATE = estado da partida(pre, post, in)
    MT_STATUS = status da partida(STATUS_SECOND_HALF,STATUS_SCHEDULED,STATUS_FINAL_PEN)

FUT_ETL_LOGS:
    ETL_ID = id
    ETL_DATE = data do etl
    ETL_TABLE = nome da tabela
    ETL_REGISTROS = quantidade de registros
    ETL_STATUS = status do etl(sucesso, falha)
    ETL_MESSAGE = mensagem do etl