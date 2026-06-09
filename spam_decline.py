import requests,json
import re
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tep

__formate_coki__ = lambda x: {cookie.split('=', 1)[0].strip(): cookie.split('=', 1)[1].strip() for cookie in x.split(';') if '=' in cookie}
coki='ps_l=1;ps_n=1;datr=NLwRj1mLu-'
headers 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'dpr': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.122", "Chromium";v="137.0.7151.122", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'viewport-width': '589',
}
group_id ='1944912799181203'

def main(story_id, member_id):
    global spam
    av= re.search('"actorID":"(.*?)"', str(response)).group(1)
    __hs= re.search('"haste_session":"(.*?)",', str(response)).group(1)
    __rev= re.search('{"rev":(.*?)}', str(response)).group(1)
    __hsi= re.search('"hsi":"(.*?)",', str(response)).group(1)
    fb_dtsg= re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"', str(response)).group(1)
    jazoest= re.search('&jazoest=(.*?)",', str(response)).group(1)
    lsd= re.search(r'"LSD",\[\],{"token":"(.*?)"', str(response)).group(1)
    __spin_r= re.search('"__spin_r":(.*?),', str(response)).group(1)
    __spin_t= re.search('"__spin_t":(.*?),', str(response)).group(1)
    __comet_req = re.search('__comet_req=(.*?)&', str(response)).group(1)
    _req =  re.search('_req=(.*?)&', str(response)).group(1)
    data = {
        'av':av,
        '__aaid': '0',
        '__user': av,
        '__a': '1',
        '__req': 'y',
        '__hs': __hs,
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': __rev,
        '__hsi': __hsi,
        '__comet_req': __comet_req,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': lsd,
        '__spin_r': __spin_r,
        '__spin_t': __spin_t,
        '__crn': 'comet.fbweb.CometGroupModminReviewFolderRoute',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupsCometModminReviewFolderDeclineContentMutation',
        'variables': json.dumps({"input":{"action_source":"GROUP_MODMIN_REVIEW_FOLDER","group_id":group_id,"story_id":story_id,"actor_id":av,"client_mutation_id":"1"},"contentType":"GROUP_POST","member_id":member_id}),
        'server_timestamps': 'true',
        'doc_id': '30216535437945305',
    }

    responsea = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    spam= re.search(r'"spam_count":{"count":(\d+)}', responsea.text).group(1)
    print(spam )

cookies =__formate_coki__(coki)
spam=0

while True:
    response = requests.get(f'https://www.facebook.com/groups/{group_id}/pending_posts', cookies=cookies, headers=headers).text.replace('\\','')
    story_id = re.findall(r'"story":{"id":"(.*?)"(.*?)"User","id":"(\d+)"', response)
    story_id = list(set((s[0], s[2]) for s in story_id))
    print(story_id)
    with tep(max_workers=5) as executor:
        for story_id, member_id in story_id:
            executor.submit(main, story_id, member_id)
    response = requests.get(f'https://www.facebook.com/groups/{group_id}/spam', cookies=cookies, headers=headers).text.replace('\\','')
    story_id = re.findall(r'"story":{"id":"(.*?)"(.*?)"User","id":"(\d+)"', response)
    story_id = list(set((s[0], s[2]) for s in story_id))
    print(story_id)
    with tep(max_workers=5) as executor:
        for story_id, member_id in story_id:
            executor.submit(main, story_id, member_id)
    sleep_time=180
    for _ in range(sleep_time):
        print(f'Wating for {sleep_time-_}',end='\r')
        sleep(1)
