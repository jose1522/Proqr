from app import app  # Imports the "app" object from __init__.py, located in the app folder.

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # runs the flask app through "Lazy loading" (not through a real server)
