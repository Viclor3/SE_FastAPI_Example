from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title="Refactor",
        docs_url="/api/docs",
        debug=True
    )

    from app.routes.classifier import register_routes
    register_routes(app)

    return app
