import requests
import pandas as pd
from datetime import datetime
from config import API_URL, COMPETITIONS
from database import engine
# pyrefly: ignore [missing-import]
from sqlalchemy import text, select
from models import Team, League, LeagueTeam
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

#funções de API
def get_json(url: str) -> dict:
    headers = {
        "Accept" : "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "app-source" : "FP",
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def get_teams(competition):
    # Primeiro garante que a liga existe no banco e pega o ID interno dela (LG_ID)
    lg_id = register_league(competition)

    url_request = f"https://sports.core.api.espn.com/v2/sports/soccer/leagues/{competition}/teams"
    request = get_json(url_request)
    for teams_url in request["items"]:
        team_url = teams_url["$ref"]
        team_request = get_json(team_url)
        
        team_id = team_request["id"]
        team_name = team_request["name"]
        team_abbreviation = team_request["abbreviation"]
        team_logo = team_request["logos"][0]["href"]
        team_location = team_request["venue"]["address"]["country"]
        
        # Salva o time e recebe de volta a Chave Primária do banco (TM_ID)
        internal_tm_id = register_teams(str(team_id), team_name, team_logo, team_location)
        
        # Cria o vínculo entre a Liga e o Time
        register_league_team(lg_id, internal_tm_id)

def get_scoreboard(data: str):
    for competition in COMPETITIONS.values():
        url_request = f"{API_URL}/{competition}/scoreboard?dates={data}"
        request = get_json(url_request)



def register_log(table, status, message):
    con = engine.connect()
    con.execute(text(f"""INSERT INTO FUT_ETL_LOGS (
                     ETL_DATE, ETL_TABLE, ETL_REGISTROS, ETL_STATUS, 
                     ETL_MESSAGE) VALUES (CURRENT_TIMESTAMP, '{table}', 
                     1, '{status}', '{message}')"""))
    con.commit()
    con.close()

def register_league(competition):
    url = f"https://sports.core.api.espn.com/v2/sports/soccer/leagues/{competition}"
    try:
        data = get_json(url)
        name = data.get("name", competition)
        country = data.get("country", {}).get("name", "Desconhecido")
        lg_type = "Torneio" if data.get("isTournament") else "Liga"
    except Exception:
        name = competition
        country = "Desconhecido"
        lg_type = "Liga"

    with Session(engine) as session:
        stmt = select(League).where(League.LG_REQUEST == competition)
        league = session.execute(stmt).scalar_one_or_none()

        if not league:
            league = League(LG_NAME=name, LG_COUNTRY=country, LG_TYPE=lg_type, LG_REQUEST=competition)
            session.add(league)
            session.commit()
            register_log("FUT_LEAGUES", "sucesso", f"Liga {name} registrada com sucesso!")
        
        return league.LG_ID

def register_league_team(lg_id, tm_id):
    with Session(engine) as session:
        stmt = select(LeagueTeam).where(LeagueTeam.LG_ID == lg_id, LeagueTeam.TM_ID == tm_id)
        relation = session.execute(stmt).scalar_one_or_none()
        
        if not relation:
            relation = LeagueTeam(LG_ID=lg_id, TM_ID=tm_id)
            session.add(relation)
            session.commit()
            register_log("FUT_LEAGUES_TEAMS", "sucesso", f"Time vinculado à liga com sucesso!")

def register_teams(team_api_id, team_name, team_logo, team_location):
    with Session(engine) as session:
        stmt = select(Team).where(Team.TM_ID_API == team_api_id)
        team = session.execute(stmt).scalar_one_or_none()

        if not team:
            stmt = select(Team).where(Team.TM_NAME == team_name)
            team = session.execute(stmt).scalar_one_or_none()

        if not team:
            team = Team(TM_NAME=team_name, TM_LOGO=team_logo, TM_COUNTRY=team_location, TM_ID_API=team_api_id)
            session.add(team)
            session.commit()
            register_log("FUT_TEAMS", "sucesso", f"Time {team_name} registrado com sucesso!")
        else:
            team.TM_LOGO = team_logo
            team.TM_COUNTRY = team_location
            team.TM_ID_API = team_api_id
            session.commit()
            register_log("FUT_TEAMS", "sucesso", f"Time {team_name} atualizado com sucesso!")
            
        return team.TM_ID

get_teams("bra.1")

