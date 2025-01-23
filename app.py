from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "your-database-host",
    "user": "your-database-user",
    "password": "your-database-password",
    "database": "dragonite"
}

@app.route("/api/geofences")
def get_geofences():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT name, geofence, enabled FROM area")
        geofences = cursor.fetchall()
        connection.close()
        return jsonify(geofences)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
