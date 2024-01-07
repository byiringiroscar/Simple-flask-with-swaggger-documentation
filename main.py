from flask import Flask, jsonify
# from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# # Call factory function to create our blueprint
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )

# app.register_blueprint(swaggerui_blueprint)

@app.route('/')
def home():
    return jsonify({'message': 'Success'})


if __name__ == '__main__':
    app.run(debug=True)