from http import HTTPStatus

from flask import request
from flask_jwt_extended import decode_token, jwt_required
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.user_exc import UserNotFound
from app.exceptions.generic_exc import ObjNotFoundError
from app.models.risk_model import RiskModel
from app.models.user_model import UserModel


@jwt_required()
def create_user_risk_profile():
    data = request.get_json()
    session: Session = db.session
    token = request.headers.get("Authorization").split()[-1]
    decoded_jwt = decode_token(token)
    user_id = decoded_jwt.get("sub")
    user: UserModel = UserModel.query.get(user_id)

    if not user:
        raise ObjNotFoundError("user")

    selected_case = ""

    for case_key, case_value in RiskModel.CASES.items():
        # TODO: find a better name to count variable
        count = 0
        for key, value in data.items():
            if value == case_value[key]:
                count += 1
            if count == 2:
                selected_case = case_key

    message = RiskModel.VALUES[selected_case]
    risk_query: Query = session.query(RiskModel)

    risk: RiskModel = risk_query.filter_by(title=selected_case).first()

    if not risk:

        risk_data = {"title": selected_case, "text": message}

        risk = RiskModel(**risk_data)

    if user.risks:
        user.risks = []

    risk.users.append(user)
    session.add(risk)
    session.commit()

    serialized_user = {
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "risks": user.risks,
    }

    return serialized_user, HTTPStatus.CREATED
