# Run a test server.
from app import app, db


# for ec2 instance testing.
app.run(host='0.0.0.0', port=8080, debug=True)
