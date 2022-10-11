from . import *

if __name__ == '__main__':
  app = create_app()
  app.run(host="localhost", port=8000, debug=False)
