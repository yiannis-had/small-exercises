import requests
import sys


def get_manufacturer_details(manufacturer):
    url = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetManufacturerDetails/"
        + manufacturer
        + "?format=json"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} \n")
        print(response.text)
        sys.exit(0)
    return response.json()


def get_manufacturer_makes(manufacturer):
    url = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakeForManufacturer/"
        + manufacturer
        + "?format=json"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} \n")
        print(response.text)
        sys.exit(0)
    return response.json()


def get_model_details(make):
    url = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/"
        + make
        + "?format=json"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} \n")
        print(response.text)
        sys.exit(0)
    return response.json()


porsche_response = get_model_details("Porsche")
porsche_models = porsche_response["Results"]
with open("porsches.csv", "w") as porsche_csv:
    for model in porsche_models:
        porsche_csv.write(str(model["Model_ID"]) + "," + model["Model_Name"])
        porsche_csv.write("\n")
