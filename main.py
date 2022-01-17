import requests
from bs4 import BeautifulSoup

worknet_result = requests.get("https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?&resultCnt=50&keyword=python")

worknet_soup = BeautifulSoup(worknet_result.text, "html.parser")

pagination = worknet_soup.find("nav", {"class":"pagination"})

pages = pagination.find_all('a')
spans = []

for page in pages:
  spans.append(page)

print(spans)