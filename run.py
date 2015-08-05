# Run a test server.
from app import app

# for ec2 instance testing.
# app.run(host='0.0.0.0', port=8080, debug=True)

# for Windows local testing.
app.run(host='127.0.0.1', port=80, debug=True)

