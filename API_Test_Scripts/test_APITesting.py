import pytest
import requests
import json

putPaylaod = {

        "name": "API",
        "job": "API Tester"
    }
patch_payload={
    "job": "API Tester"
}
@pytest.mark.regession
@pytest.mark.all
def test_getRequestCode():
    response = requests.get("https://reqres.in/api/users?page=2")
    code = response.status_code
    assert code == 200, "code does'nt match"

@pytest.mark.regession
@pytest.mark.all
def test_getRequestData():
    response = requests.get("https://reqres.in/api/users?page=2")
    jsonResponse = response.json()
    length_of_data = len(jsonResponse['data'])
    print(length_of_data)
    x = 0
    for i in jsonResponse['data']:
        print(x)
        id = i["id"]
        print(id)
        assert id != "", "id not assinged"

        email_id = i["email"]
        print(email_id)
        assert email_id.endswith("@reqres.in"), "email format does'nt match"
        f_name = i["first_name"]
        print(f_name)
        assert f_name != None, "first name not mentioned"
        l_name = i["last_name"]
        print(l_name)
        assert l_name != None, "last name not mentioned"
        avatar = i["avatar"]
        print(avatar)
        assert avatar.endswith(".jpg"), "required image"
        x = x + 1

@pytest.mark.smoke
@pytest.mark.all
def test_postRequest():
    payload_data = open(r'API_Test_Scripts/payload.json', "r").read()
    json_data = json.loads(payload_data)
    print(json_data['name'])
    print(type(json_data))
    print(payload_data)
    post_response = requests.post("https://reqres.in/api/users", data=json.loads(payload_data))
    assert post_response.status_code == 201, "response code not expected"
    print(post_response)
    assert post_response.json()['name'] == json_data['name']
    assert post_response.json()['job'] == json_data['job']
    assert post_response.json()['id'] != None, "id not assinged"
    assert post_response.json()['createdAt'] != None, "date not assinged"
    print(post_response.json())

@pytest.mark.smoke
@pytest.mark.all
def test_putRequest():
    print(putPaylaod['name'])
    put_response = requests.put("https://reqres.in/api/users/2", data=putPaylaod)
    assert put_response.status_code == 200, "request code is expected"
    print(put_response.json()['name'])
    print(type(put_response.json()['updatedAt']))
    updatedat = put_response.json()['updatedAt']
    updatedat.find(':')
    assert put_response.json()['name'] == putPaylaod['name'], "name updated successfully"
    assert put_response.json()['job'] == putPaylaod['job'], "job updated successfully"
    assert put_response.json()['updatedAt'].find('-'), "didn'nt get updated date"
    print(put_response.json())

@pytest.mark.smoke
@pytest.mark.all
def test_patchRequest():
    patch_resp = requests.patch("https://reqres.in/api/users/2", data=patch_payload)
    print(patch_resp.json())
    print(patch_resp.json()['updatedAt'])
    assert patch_resp.json()['updatedAt'] != None, "updated successfully"








