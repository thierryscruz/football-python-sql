# pyrefly: ignore [missing-import]
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# pyrefly: ignore [missing-import]
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = 'fut_teams'

    TM_ID: Mapped[int] = mapped_column('tm_id', primary_key=True)
    TM_NAME: Mapped[str] = mapped_column('tm_name', String(255), nullable=False, unique=True)
    TM_COUNTRY: Mapped[str] = mapped_column('tm_country', String(255), nullable=False)
    TM_LOGO: Mapped[str] = mapped_column('tm_logo', String(255), nullable=False)
    TM_ID_API: Mapped[str] = mapped_column('tm_id_api', String(255), nullable=True)

class EtlLog(Base):
    __tablename__ = 'fut_etl_logs'

    ETL_ID: Mapped[int] = mapped_column('etl_id', primary_key=True)
    ETL_DATE: Mapped[str] = mapped_column('etl_date', String(255), nullable=False)
    ETL_TABLE: Mapped[str] = mapped_column('etl_table', String(255), nullable=False)
    ETL_REGISTROS: Mapped[int] = mapped_column('etl_registros', nullable=False)
    ETL_STATUS: Mapped[str] = mapped_column('etl_status', String(255), nullable=False)
    ETL_MESSAGE: Mapped[str] = mapped_column('etl_message', String(255), nullable=False)

class League(Base):
    __tablename__ = 'fut_leagues'

    LG_ID: Mapped[int] = mapped_column('lg_id', primary_key=True)
    LG_NAME: Mapped[str] = mapped_column('lg_name', String(255), nullable=False)
    LG_COUNTRY: Mapped[str] = mapped_column('lg_country', String(255), nullable=False)
    LG_TYPE: Mapped[str] = mapped_column('lg_type', String(255), nullable=False)
    LG_REQUEST: Mapped[str] = mapped_column('lg_request', String(255), nullable=False, unique=True)

class LeagueTeam(Base):
    __tablename__ = 'fut_leagues_teams'

    LG_ID: Mapped[int] = mapped_column('lg_id', primary_key=True)
    TM_ID: Mapped[int] = mapped_column('tm_id', primary_key=True)
