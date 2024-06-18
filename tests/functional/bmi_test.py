def test_bmi_calc_get(client):
    """
       GIVEN a testing client
       WHEN the '/bmi' endpoint is requested via GET
       THEN check that the response is valid and contains the expected fields
    """
    response = client.get('/bmi')
    assert response.status_code == 200
    assert b'Height' in response.data
    assert b'Weight' in response.data


def test_bmi_calc_post(client):
    """
    GIVEN a testing client
    WHEN the '/bmi' endpoint is posted to with height and weight data
    THEN check that the response gives correct calculations
    """
    response = client.post("/bmi", data={"number1": '1.80', "number2": '60'})
    assert response.status_code == 200
    assert b'Your BMI is : 18.52' in response.data

