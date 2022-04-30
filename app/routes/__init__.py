from flask import Flask

def init_app(app: Flask):

    from .address_blueprint import bp_address 
    app.register_blueprint(bp_address)

    from .message_blueprint import bp_message
    app.register_blueprint(bp_message)

    from .risk_blueprint import bp_risk
    app.register_blueprint(bp_risk)

    from .user_blueprint import bp_users
    app.register_blueprint(bp_users)

