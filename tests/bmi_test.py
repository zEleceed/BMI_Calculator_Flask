def test_bmi_calc_get(client):  #testing the GET method for /bmi route
    response = client.get('/bmi')
    assert response.status_code == 200
    assert b'Height' in response.data
    assert b'Weight' in response.data


def test_bmi_calc_post(client):  #testing POST method
    response = client.post("/bmi", data={"number1": '1.80', "number2": '60'})
    assert response.status_code == 200
    assert b'Your BMI is : 18.52' in response.data

