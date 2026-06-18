import logging
import random
import time

from flask import Flask, Response, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    force=True,
)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["endpoint"]
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - request.start_time
    endpoint = request.endpoint or "unknown"

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status_code=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)

    logging.info(
        "request_completed path=%s status=%s duration_ms=%s",
        request.path,
        response.status_code,
        round(duration * 1000, 2),
    )

    return response

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "status": "running",
        "message": "My first SRE project app is live",
        "endpoints": ["/health", "/order", "/slow", "/error", "/metrics"]
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/order")
def order():
    order_id = random.randint(10000, 99999)

    return jsonify({
        "status": "success",
        "order_id": order_id,
        "message": "Order created successfully"
    })

@app.route("/slow")
def slow():
    time.sleep(2)

    return jsonify({
        "status": "success",
        "message": "This request was intentionally slow"
    })

@app.route("/error")
def error():
    logging.error(
        "simulated_order_failure path=%s status=500 duration_ms=0",
        request.path,
    )

    return jsonify({
        "status": "error",
        "message": "This request intentionally failed"
    }), 500

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)