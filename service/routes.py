from flask import Flask, jsonify, request, make_response
from service.models import Account

app = Flask(__name__)

@app.route("/accounts", methods=["POST"])
def create_accounts():
    data = request.get_json()
    # Pastikan data yang dikirim lengkap
    account = Account(data["name"], data["email"], data["address"])
    account.save()
    return jsonify({"id": account.id, "name": account.name}), 201

@app.route("/accounts", methods=["GET"])
def list_accounts():
    accounts = Account.all()
    results = [{"id": a.id, "name": a.name} for a in accounts]
    return jsonify(results), 200

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        return jsonify({"error": "Not Found"}), 404
    return jsonify({"id": account.id, "name": account.name}), 200

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        return jsonify({"error": "Not Found"}), 404
    data = request.get_json()
    account.name = data.get("name", account.name)
    account.email = data.get("email", account.email)
    account.address = data.get("address", account.address)
    return jsonify({"id": account.id, "name": account.name}), 200

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    account = Account.find(account_id)
    if account:
        Account.data.remove(account)
    return make_response("", 204)

if __name__ == "__main__":
    # Gunakan debug=True agar kalau ada error langsung kelihatan di terminal
    app.run(host="0.0.0.0", port=8080, debug=True)