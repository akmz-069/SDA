from flask import Flask, request, jsonify
import random

app = Flask(__name__)

servers = ["http://server1:8000", "http://server2:8000", "http://server3:8000"]

def is_server_healthy(server_url):
  return True  

@app.route("/load_balancer", methods=["GET"])
def load_balancer():
  healthy_servers = [server for server in servers if is_server_healthy(server)]

  if not healthy_servers:
    return jsonify({"error": "No healthy servers found"}), 503

  # Select a random server from healthy servers
  server = random.choice(healthy_servers)
  return jsonify({"redirect_to": server})

if __name__ == "__main__":
  app.run(debug=True)