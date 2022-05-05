from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db


@dataclass
class RiskModel(db.Model):
    title: str
    text: str

    # Rain precipitation limit in mm
    PRECIPITATION_LIMIT = 50

    __tablename__ = "risks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    text = Column(String, nullable=False)

    VALIDATOR = {"live_nearby_river": bool, "live_nearby_mountain": bool}

    CASES = {
        "NOT_SPECIFIED": {"live_nearby_river": False, "live_nearby_mountain": False},
        "EARTH_SLIDING": {"live_nearby_river": False, "live_nearby_mountain": True},
        "FLOOD": {"live_nearby_river": True, "live_nearby_mountain": False},
        "FLOOD_AND_SLIDING": {"live_nearby_river": True, "live_nearby_mountain": True},
    }

    # TODO: find a better way to display the texts
    VALUES = {
        "NOT_SPECIFIED": "FORTES CHUVAS: Se mora próximo a encosta ou rio, reúna pertences importantes (documento/dinheiro) e dirija-se p/ o ponto de apoio da Defesa Civil mais próximo.",
        "EARTH_SLIDING": "FORTES CHUVAS: RISCO DE DESLIZAMENTO, reúna pertences importantes (documentos e dinheiro) e dirija-se p/ o ponto de apoio da Defesa Civil mais próximo.",
        "FLOOD": "FORTES CHUVAS: RISCO DE ALAGAMENTO, reúna pertences importantes (documentos e dinheiro) e dirija-se p/ o ponto de apoio da Defesa Civil mais próximo.",
        "FLOOD_AND_SLIDING": "FORTES CHUVAS: RISCO DE DESLIZAMENTO E ALAGAMENTO, reúna pertences importantes (documentos/dinheiro) e dirija-se p/ o ponto de apoio da Defesa Civil + próximo.",
    }
