import json

import requests

__author__ = "Andreas Bernöcker"
__version__ = "1.0"
__maintainer__ = "Manfred von Teichman"
__email__ = "bernoecker.and-tit14@it.dhbw-ravensburg.de"
__status__ = "Development"

blackBoardName = "test"
blackBoardName1 = "test1"
blackBoardName2 = "test2"
blackBoardName3 = "test3"
payload = {'message': 'test'}
payload1 = {'messagee': 'test'}
payload2 = {'message': ''}
payload3 = {
    'message': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'}
payload4 = {'message': ''}
payload5 = {'message': 'is not empty'}

# Must be changed based on configuration
url = 'http://127.0.0.1:1337/api/v1/blackboard/'

# CLEAR DATABASE
r = requests.delete(url)


def test_create_blackboard():
    file.write("ID: 100 Name: CREATE_BLACKBOARD \n")
    # Test ID: 110
    put_request = requests.put(url + blackBoardName)
    response = json.loads(put_request.text)
    file.write(
        "ID: 110    Response code: " + str(put_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 120
    put_request = requests.put(url + blackBoardName)
    response = json.loads(put_request.text)
    file.write(
        "ID: 120    Response code: " + str(put_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 130
    put_request = requests.put(url + blackBoardName)
    response = json.loads(put_request.text)
    file.write(
        "ID: 130    Response code: " + str(put_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


def test_display_blackboard():
    file.write("ID: 200 Name: DISPLAY_BLACKBOARD \n")
    # Test ID: 211
    post_request = requests.post(url + blackBoardName, json=payload)
    response = json.loads(post_request.text)
    file.write(
        "ID: 211    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 212
    post_request = requests.post(url + blackBoardName, json=payload1)
    response = json.loads(post_request.text)
    file.write(
        "ID: 212    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'message'] + "\n")

    # Test ID: 213
    post_request = requests.post(url + blackBoardName, json=payload2)
    response = json.loads(post_request.text)
    file.write(
        "ID: 213    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'message'] + "\n")

    # Test ID: 214
    post_request = requests.post(url + blackBoardName, json=payload3)
    response = json.loads(post_request.text)
    file.write(
        "ID: 214    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'message'] + "\n")

    # Test ID: 215 (got stashed)
    # post_request = requests.post(url + blackBoardName, payload4)
    # response = json.loads(r.text)
    # file.write(
    #     "ID: 250    Response code: " + str(post_request.status_code) + "    Response message: " + response[
    #          'message'] + "\n")

    # Test ID: 216
    post_request = requests.get(url + blackBoardName)
    response = json.loads(post_request.text)
    file.write(
        "ID: 216    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'message'] + "\n")

    post_request = requests.post(url + blackBoardName, json=payload5)
    response = json.loads(post_request.text)
    file.write(
        "ID: 216    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    post_request = requests.get(url + blackBoardName)
    response = json.loads(post_request.text)
    file.write(
        "ID: 216    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'message'] + "\n")

    # 220
    post_request = requests.post(url + blackBoardName1, json=payload)
    response = json.loads(post_request.text)
    file.write(
        "ID: 220    Response code: " + str(post_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


def test_read_blackboard():
    file.write("ID: 300 Name: READ_BLACKBOARD \n")
    # Test ID: 311
    get_request = requests.get(url + blackBoardName)
    response = json.loads(get_request.text)
    file.write(
        "ID: 311    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 312
    get_request = requests.put(url + blackBoardName2)
    response = json.loads(get_request.text)
    file.write(
        "ID: 312    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    get_request = requests.get(url + blackBoardName2)
    response = json.loads(get_request.text)
    file.write(
        "ID: 312    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 320
    get_request = requests.get(url + blackBoardName3)
    response = json.loads(get_request.text)
    file.write(
        "ID: 320    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


def test_clear_blackboard():
    file.write("ID: 400 Name: CLEAR_BLACKBOARD \n")
    # Test ID: 411
    get_request = requests.get(url + blackBoardName)
    response = json.loads(get_request.text)
    file.write(
        "ID: 411    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    get_request = requests.patch(url + blackBoardName + "/clear")
    response = json.loads(get_request.text)
    file.write(
        "ID: 411    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 412
    get_request = requests.get(url + blackBoardName)
    response = json.loads(get_request.text)
    file.write(
        "ID: 412    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    get_request = requests.patch(url + blackBoardName + "/clear")
    response = json.loads(get_request.text)
    file.write(
        "ID: 412    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n")

    # Test ID: 413
    get_request = requests.patch(url + blackBoardName3 + "/clear")
    response = json.loads(get_request.text)
    file.write(
        "ID: 413    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


def test_get_blackboard_status():
    file.write("ID: 500 Name: STATUS_BLACKBOARD \n")
    # Test ID: 510
    get_request = requests.get(url + blackBoardName + "/status")
    response = json.loads(get_request.text)
    file.write("ID: 510    Response code: " + str(get_request.status_code) + "    Response message: " + response[
        'response'] + "        isEmpty: " + str(response['isEmpty']) + "\n")
    # Test ID: 520
    get_request = requests.get(url + blackBoardName3 + "/status")
    response = json.loads(get_request.text)
    file.write(
        "ID: 520    Response code: " + str(get_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


def test_delete_blackboard():
    file.write("ID: 600 Name: DELETE_BLACKBOARD \n")
    # Test ID: 610
    delete_request = requests.delete(url + blackBoardName)
    response = json.loads(delete_request.text)
    file.write(
        "ID: 610    Response code: " + str(delete_request.status_code) + "    Response message: " + response[
            'response'] + "\n")
    # Test ID: 620
    delete_request = requests.delete(url + blackBoardName3)
    response = json.loads(delete_request.text)
    file.write(
        "ID: 620    Response code: " + str(delete_request.status_code) + "    Response message: " + response[
            'response'] + "\n\n")


file = open("result.txt", "w")
test_create_blackboard()
test_display_blackboard()
test_read_blackboard()
test_clear_blackboard()
test_get_blackboard_status()
test_delete_blackboard()
file.close()
