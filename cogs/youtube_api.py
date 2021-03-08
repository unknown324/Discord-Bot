import requests
import json
#scribblenot unmasked
from pprint import pprint
headers = {
    'authority': 'www.youtube.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20210304.08.01',
    #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9'
    #'cookie': 'GPS=1; YSC=59tEyVljWuQ; VISITOR_INFO1_LIVE=fdjomRBIwAk; PREF=tz=Asia.Karachi; ST-lw4sd=oq=tupac&gs_l=youtube.3..0i131k1l2j0l2j0i131k1l4j0l2j0i131k1l4.16578.17727.0.18141.7.7.0.0.0.0.501.501.5-1.3.0.yt24008602%2Ctlf%3D1%2Ccfro%3D1%2Ctlf%3D0...0...1ac.1.64.youtube..4.1.501.0...506.4N3hU_kmY6c&itct=CBcQ7VAiEwiN3ZWZ6pnvAhVN4RYKHZYJAbA%3D&csn=MC4yNzc0ODA0Njc4MjcwNTI0&endpoint=%7B%22clickTrackingParams%22%3A%22CBcQ7VAiEwiN3ZWZ6pnvAhVN4RYKHZYJAbA%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fresults%3Fsearch_query%3Dtupac%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_SEARCH%22%2C%22rootVe%22%3A4724%7D%7D%2C%22searchEndpoint%22%3A%7B%22query%22%3A%22tupac%22%7D%7D',
}

params = (
    ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)
def getVideo(name):

    data1 = '{"context": {"client": {"hl": "en-GB","userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36,gzip(gfe)","clientName": "WEB","clientVersion": "2.20210304.08.01","originalUrl": "https://www.youtube.com/","browserName": "Chrome","timeZone": "Asia/Karachi"}},"query": "'+name+'"}'
    response = requests.post('https://www.youtube.com/youtubei/v1/search', headers=headers, params=params, data=data1)
    video = json.loads(response.content)['contents']["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["videoRenderer"]
    print("---------------------------------")
    print("Video ID : "+video["videoId"])
    print("Title : "+video["title"]["runs"][0]["text"])
    print("Description : "+video["descriptionSnippet"]['runs'][0]['text'])
    print("Video Length : "+video["lengthText"]["accessibility"]["accessibilityData"]["label"])
    print("Channel : "+video["ownerText"]["runs"][0]["text"])
    print("Publish Date : "+video["publishedTimeText"]["simpleText"])
    print("---------------------------------")
    return video["videoId"]