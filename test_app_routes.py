# test_app_routes.py
import io
from unittest.mock import patch


def test_home_page(client):
    # home page should just load
    response = client.get("/")
    assert response.status_code == 200


def test_text_file_upload(client):
    # a .txt file isn't an image, so we expect the error message
    fake_file = (io.BytesIO(b"hello, not an image"), "notes.txt")
    response = client.post("/prediction", data={"file": fake_file},
                           content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data


def test_prediction_with_mock(client):
    # mock the model functions so we don't need a real image or the full model
    fake_file = (io.BytesIO(b"pretend image"), "digit.png")
    with patch("app.preprocess_img", return_value="array"), \
         patch("app.predict_result", return_value=7):
        response = client.post("/prediction", data={"file": fake_file},
                               content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed" not in response.data


def test_get_prediction_not_allowed(client):
    # /prediction only takes POST
    response = client.get("/prediction")
    assert response.status_code == 405
