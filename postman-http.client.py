import http.client
import json

conn = http.client.HTTPConnection("nerp.dfgou.cn")
payload = json.dumps({
  "custIds": [
    "201411731576","200901110355"
  ],
  "uuid": "string"
})
headers = {
  'token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDE0OTciLCJhY2NvdW50SWQiOiIxMDE0OTciLCJzdGFmZlVzZXJJZCI6IjExNTY1NSIsImlzcyI6Im9jai1zdGFyc2t5IiwiZXhwIjoxNzQxNTkwNzE1LCJpYXQiOjE3NDE1ODcxMTV9.0Hl_K-rgrYDAn5KpQxDIPK8nttzu0XwLbXSV9QjO-vQ',
  'authCode': 'sem_memberPoints',
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/bom/member/point/PointWriteFacade/userPointRecalculate", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))