from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Use environment variable to get the username
    username = os.environ.get('USER', 'Unknown User')

    # Get the server time in IST
    server_time = datetime.now().astimezone().isoformat()

    # Get the output of the 'top' command
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    response = f"""
    <h1>System Information</h1>
    <p>Name: Shoaib Imran</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
