import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?&resultCnt=50&keyword=python&pageIndex=1"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("nav", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page