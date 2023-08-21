import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cpu_temperature', methods=['GET'])
def get_cpu_temperature():
    temps = psutil.sensors_temperatures()

    # Typically, 'coretemp' is the key for CPU temperature, but this may vary depending on the platform and hardware
    if 'coretemp' in temps:
        core_temp = temps['coretemp']
        if core_temp:
            # Assuming you want the first sensor's current temp
            current_temp = core_temp[0].current
            return jsonify({"success": True, "temperature": current_temp}), 200
    return jsonify({"success": False, "message": "Cannot fetch CPU temperature."}), 500

if __name__ == "__main__":
    app.run(debug=True)
