from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm import Session

from app.configs.database import db
from app.models.risk_model import RiskModel

def risks():
    
    session: Session = db.session

    risks =  session.query(RiskModel).all()

    return jsonify(risks),HTTPStatus.OK
