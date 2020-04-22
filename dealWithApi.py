import base64, os, requests, json

env = os.environ

default_headers = {
    'app_id': env.get('APP_ID', 'xxxxxxxxxxxxx'), # repalce you own app_id and app_key
    'app_key': env.get('APP_KEY', 'xxxxxxxxxxxx'),
    'Content-type': 'application/json'
}
service = 'https://api.mathpix.com/v3/latex'


def image_uri(filename):
    image_data = open(filename, "rb").read()
    return "data:image/jpg;base64," + base64.b64encode(image_data).decode()


def latex(args, headers=default_headers, timeout=30):
    r = requests.post(service, data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)


def convertMath(path):
    r = latex({"src": image_uri(path),
               "ocr": ["math", "text"],
               "formats": ['latex_styled'],
               "format_options": {
                   "latex_styled": {"transforms": ["rm_spaces"]}
               }})
    return r['latex_styled']

