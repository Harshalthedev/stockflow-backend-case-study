from stockflow import app, db
import stockflow.routes  # ✅ This line registers all routes

if __name__ == '__main__':
    app.run(debug=True)
