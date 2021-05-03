from .models import add_user
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/v1/user/', methods=['POST'])
def create_user():
    # On recupere le corps (payload) de la requete
    payload = request.form.to_dict()
    result = models.add_user(**payload)

    if result:
        return jsonify(status='True', message='User created')
    return jsonify(status='False')

@app.route('/api/v1/user/', methods=['GET'])
def get_all_users():
    result = Models.get_all_users()
    if result:
        return jsonify(status="True",
        result= [
            {
            "id":user.id,
            "nom":user.nom,
            "prenom":user.prenom,
            "email":user.email,}
    for user in result.all() ])
    return jsonify(status="False")

@app.route('/api/v1/user/<email>', methods=['GET'])
def get_user(email):
    result = Models.get_user_by_email(email)
    if result:
        return jsonify(status="True",
                    result={"id":result.id,
                            "nom":result.nom,
                            "prenom":result.prenom,
                            "email":result.email,}
                        )
    return jsonify(status="False")

@app.route('/api/v1/user/<email>', methods=['PUT'])
def mofify_user(email):
    result = Models.update_attribute(email, request.form.to_dict())
    if result:
        return jsonify(status="True",
                        message= "updated",
                        result={
                            "id":result.id,
                            "nom":result.nom,
                            "prenom":result.prenom,
                            "email":result.email,}
                            )
    return jsonify(status= "False")


@app.route('/api/v1/user/<email>', methods=['DELETE'])
def delete_user(email):
    result = Models.delete_user_by_email(email)
    if result:
        return jsonify(status="True",
                        message= "Deleted",
                        email=email
                        )
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)