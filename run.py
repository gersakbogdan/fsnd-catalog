#!flask/bin/python
from catalog import app

app.debug = True
app.run(host='0.0.0.0', port=8000)