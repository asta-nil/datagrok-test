import psutil
from flask import Flask, jsonify

app = Flask(__name__)


def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    network_io_counters = psutil.net_io_counters()

    metrics = {
        "cpu_percent": cpu_percent,
        "memory_percent": memory.percent,
        "disk_usage_percent": disk_usage.percent,
        "network_bytes_sent": network_io_counters.bytes_sent,
        "network_bytes_recv": network_io_counters.bytes_recv
    }

    return jsonify(metrics)


@app.route('/')
def metrics():
    return get_metrics()


@app.route('/heath-check', methods=['GET'])
def healthcheck_ok():
    return jsonify('Everything is fine'), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
