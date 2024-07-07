from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, decode_token
from flask import Flask

app = Flask(__name__)


with app.app_context():
    app.config['SECRET_KEY'] = 'f8cd36459b1fd3cca1ad410b3543b321'
    app.config["JWT_SECRET_KEY"] = '0d386d07e1201a76008d74334dab4a54'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.json.sort_keys = False
    jwt = JWTManager(app)
    access_token = create_access_token(identity="@Kenechi")
    decode_token = decode_token(access_token)
    print(access_token)
    print(decode_token)