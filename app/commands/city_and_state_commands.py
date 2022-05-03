from flask.cli import AppGroup
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models.city_model import CityModel
from app.models.state_model import StateModel
from app.utils import city_state_info


def state_and_city_cli():
    state_city_group = AppGroup(
        "states_cities", help="Populate states and cities database"
    )

    @state_city_group.command("create")
    def create_states_and_cities():

        session: Session = db.session

        state_list = city_state_info.state_list

        print("=" * 60, "\n")
        print("Adding states to the database...")

        states = [StateModel(name=state) for state in state_list]

        session.add_all(states)
        session.commit()

        print("\n")
        print(f"Added {len(state_list)} states to the database successfully.", "\n")

        city_list = city_state_info.city_list

        print("~" * 60, "\n")
        print("Adding cities to the database...")

        for city_dict in city_list:
            session: Session = db.session
            city_name = city_dict.get("name")
            state_name = city_dict.get("state")

            state_query: Query = StateModel.query
            state: StateModel = state_query.filter_by(name=state_name).first()

            city_info = {"name": city_name, "state_id": state.id}

            city = CityModel(**city_info)

            session.add(city)
            session.commit()

        print("\n")
        print(f"Added {len(city_list)} cities to the database successfully.", "\n")
        print("=" * 60)

    return state_city_group
