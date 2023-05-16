from flask import Flask
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

# Create a counter metric
counter_metric = Counter("my_counter", "A counter metric")

# Endpoint to increment the counter
@app.route("/increment")
def increment_counter():
    counter_metric.inc()
    return "Counter incremented"

# Endpoint to export Prometheus metrics
@app.route("/metrics")
def export_metrics():
    return generate_latest(REGISTRY)

if __name__ == "__main__":
    app.run()