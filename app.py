from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    # REAL WORLD TRAP: Pulling a secret from an Environment Variable (injected by Vault later)
    db_password = os.getenv('DB_PASSWORD', 'Not Set')
    return f"Asset Manager is Running! DB Pass is: {db_password[:2]}***"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
