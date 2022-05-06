from random import choice

import click
from faker import Faker
from flask.cli import AppGroup
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models import AddressModel, CityModel, StateModel, UserModel
from app.services.user_risk_profile_services import select_risk_case
from app.utils import city_state_info


def populate_db_cli():
    fake = Faker("pt_BR")
    populate_db = AppGroup(
        "populate_db",
        help="Populate states, cities, addresses and users database, pass an amount of users to add.",
    )

    @populate_db.command("create")
    @click.argument("amount", type=int)
    def create_states_and_cities(amount):

        create_states_and_insert_into_db()
        create_cities_and_insert_into_db()
        create_user_addresses_and_insert_into_db(fake, amount)

    return populate_db


def create_states_and_insert_into_db():
    session: Session = db.session

    state_list = city_state_info.state_list

    print("=" * 60, "\n")
    print("Adding states to the database...")

    session: Session = db.session
    already_added_states = session.query(StateModel).all()

    states = [
        StateModel(name=state.get("name"), uf=state.get("UF"))
        for state in state_list
        if StateModel(name=state.get("name"), uf=state.get("UF"))
        not in already_added_states
    ]

    session.add_all(states)
    session.commit()

    if len(states) == 0:
        print(f"The states are already in your database.", "\n")
    elif len(states) == 1:
        print(f"Added {len(states)} state to the database successfully.", "\n")
    else:
        print(f"Added {len(states)} states to the database successfully.", "\n")


def create_cities_and_insert_into_db():

    names_and_states_cities_list = city_state_info.city_list

    print("~" * 60, "\n")
    print("Adding cities to the database...")

    cities_list = []

    session: Session = db.session
    already_added_cities = session.query(CityModel).all()

    for city_dict in names_and_states_cities_list:
        city_name = city_dict.get("name")
        state_name = city_dict.get("state")

        state_query: Query = StateModel.query
        state: StateModel = state_query.filter_by(name=state_name).first()

        city_info = {"name": city_name, "state_id": state.id}

        city = CityModel(**city_info)

        if city not in already_added_cities:
            cities_list.append(city)

    session.add_all(cities_list)
    session.commit()

    if len(cities_list) == 0:
        print(f"The cities are already in your database.", "\n")
    elif len(cities_list) == 1:
        print(f"Added {len(cities_list)} city to the database successfully.", "\n")
    else:
        print(f"Added {len(cities_list)} cities to the database successfully.", "\n")

    return cities_list


def create_user_addresses_and_insert_into_db(fake: Faker, amount: int):

    print("~" * 60, "\n")
    print("Adding users to the database...")

    for _ in range(amount):
        session: Session = db.session

        user_data = create_user_data(fake)
        user: UserModel = UserModel(**user_data)

        risk_data = {"live_nearby_river": False, "live_nearby_mountain": False}

        session.add(user)
        session.commit()

        select_risk_case(risk_data, user)

    if amount > 1:
        print(f"Added {amount} users to the database successfully.", "\n")
    else:
        print(f"Added {amount} user to the database successfully.", "\n")
    print("=" * 60)


def create_user_data(fake: Faker):

    name = f"{fake.first_name()} {fake.last_name()}"
    email = f"{name}@{fake.free_email_domain()}".lower().replace(" ", ".")
    phone_numer = fake.msisdn()[2:]
    phone = f"({phone_numer[:2]}) {phone_numer[2:7]}-{phone_numer[7:]}"

    address = create_address()

    user_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "password": "1234",
        "address_id": address.id,
    }

    return user_data


def create_address():

    session: Session = db.session
    cities = session.query(CityModel).all()

    city = choice(cities)

    names_states_cities_zip_code_list = city_state_info.city_list
    choosen_city_ceps = [
        choosen_city.get("cep")
        for choosen_city in names_states_cities_zip_code_list
        if choosen_city.get("name") == city.name
    ][0]

    cep_number = choice(choosen_city_ceps)

    address_data = {"cep": cep_number, "city_id": city.id}

    session: Session = db.session

    address = AddressModel(**address_data)

    session.add(address)
    session.commit()

    return address


def get_cities_list(names_and_states_cities_list):

    cities_list = []

    for city_dict in names_and_states_cities_list:
        city_name = city_dict.get("name")
        state_name = city_dict.get("state")

        state_query: Query = StateModel.query
        state: StateModel = state_query.filter_by(name=state_name).first()

        city_info = {"name": city_name, "state_id": state.id}

        city = CityModel(**city_info)

        cities_list.append(city)

    return cities_list
