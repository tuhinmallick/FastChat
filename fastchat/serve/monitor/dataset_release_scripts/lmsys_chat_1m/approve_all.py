import requests

headers = {"authorization": "Bearer hf_XXX"}

url = "https://huggingface.co/api/datasets/lmsys/lmsys-chat-1m/user-access-request/pending"
a = requests.get(url, headers=headers)

url = "https://huggingface.co/api/datasets/lmsys/lmsys-chat-1m/user-access-request/grant"
for u in a.json():
    user = u["user"]["user"]
    ret = requests.post(url, headers=headers, json={"user": user})
    print(user, ret.status_code)
    assert ret.status_code == 200
