from app import app


def test_prediction_rejects_post_without_csrf_token():
    app.config["WTF_CSRF_ENABLED"] = True
    try:
        with app.test_client() as client:
            response = client.post("/prediction", data={})
        assert response.status_code == 400
    finally:
        app.config["WTF_CSRF_ENABLED"] = False
