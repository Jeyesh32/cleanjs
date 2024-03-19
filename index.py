from flask import Flask

app = Flask(__name__)

@app.route('/api/healthy', methods=['GET'])
def health_check():
  return "I'm healthy"

if __name__ == '__main__':
  app.run(debug=True)
