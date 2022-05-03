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

    CASES = {
        "NOT_SPECIFIED": {"live_nearby_river": False, "live_nearby_mountain": False},
        "EARTH_SLIDING": {"live_nearby_river": False, "live_nearby_mountain": True},
        "FLOOD": {"live_nearby_river": True, "live_nearby_mountain": False},
        "FLOOD_AND_SLIDING": {"live_nearby_river": True, "live_nearby_mountain": True},
    }

    # TODO: find a better way to display the texts
    VALUES = {
        "NOT_SPECIFIED": """Atenção! A sua região apresenta previsão para chuvas fortes. 
                   
                   Se você mora em região de encostas ou próximo a um rio ou córrego, reúna seus pertences mais importantes 
                   (documentos, dinheiro ou cartões) e se encaminhe para o ponto de apoio da Defesa Civil mais próximo.""",
        "EARTH_SLIDING": """Atenção! A sua região apresenta previsão para chuvas fortes. 
                   Você corre risco iminente de deslizamento de terra e possível desabamento. 

                   Se ainda não começou a chover, reúna seus pertences mais importantes (documentos, dinheiro ou cartões) e 
                   se encaminhe para o ponto de apoio da Defesa Civil mais próximo.""",
        "FLOOD": """Atenção! A sua região apresenta previsão para chuvas forte. 
                   Você corre risco iminente de deslizamento de terra e possível desabamento. 

                   Se ainda não começou a chover, reúna seus pertences mais importantes (documentos, dinheiro ou cartões) e 
                   se encaminhe para o ponto de apoio da Defesa Civil mais próximo.""",
        "FLOOD_AND_SLIDING": """Atenção! A sua região apresenta previsão para chuvas fortes. 
                   Você corre risco iminente de deslizamento de terra, desabamento e alagamento. 

                   Se ainda não começou a chover, reúna seus pertences mais importantes (documentos, dinheiro ou cartões) e 
                   se encaminhe para o ponto de apoio da Defesa Civil mais próximo.""",
    }
