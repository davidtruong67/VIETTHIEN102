import requests

API_URL = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-EpbxftUE/endpoint"

def query_tidb(sql: str):
    try:
        res = requests.post(API_URL, json={"sql": sql})
        if res.status_code == 200:
            return res.json()
        else:
            return f"Lỗi: {res.status_code} - {res.text}"
    except Exception as e:
        return f"Exception: {str(e)}"
