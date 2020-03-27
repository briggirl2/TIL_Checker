import requests
import datetime
from bs4 import BeautifulSoup


def parse_github(id, start_date_input, end_date_input):
    res = requests.get("https://github.com/" + id)
    soup = BeautifulSoup(res.content, "html.parser")

    # # commit 안한 날 색 확인
    # no_mark = soup.select("div.contrib-legend ul.legend li")[0]
    # no_mark_color = no_mark["style"][18:]
    # # print(no_mark_color)

    # 검색 시작일 ~ 종료일 범위 리스트 구하기
    start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d")
    date_generated = [
        start_date + datetime.timedelta(days=x)
        for x in range(0, (end_date - start_date).days + 1)
    ]
    days_range = []
    for date in date_generated:
        days_range.append(date.strftime("%Y-%m-%d"))

    # 날짜별 커밋 정보 확인
    data = {}
    data["total_day_cnt"] = len(days_range)
    data["commit_day_cnt"] = 0 * 1
    data["commit_cnt"] = 0 * 1

    for date in days_range:
        day_rect = soup.find("rect", {"data-date": date})
        print(day_rect)
        try:
            if day_rect["data-count"] != "0":
                data["commit_day_cnt"] += 1
                data["commit_cnt"] = data["commit_cnt"] + int(day_rect["data-count"])
        except TypeError:
            continue

    return data
