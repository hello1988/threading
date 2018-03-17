from django.shortcuts import render
from django.http import HttpResponse

import time
import threading
from linebot import LineBotApi
from linebot.models import TextSendMessage

def hello(request):
    return HttpResponse('hello Django')


def __push_test(line_ids):
        print('[__push_test] id count : {}'.format(len(line_ids)) )
        success_ids = []
        fail_ids = []
        start_time = time.time()
        line_bot_api = LineBotApi('ZZYgc/Ti/sR/yAXzwUAK4Hw466gd3E6629BE1IRSPCo7ZBfYgUHTjJZgdOlmtgfTGg1RngvqZ6Qaqm0dI9MwZwpgO0FAzi7IiCooL/26ej6HAHdn7vbfHUJEMzyzDpsNwIntrfzPMaKoAQrDd69s1wdB04t89/1O/w1cDnyilFU=')
        for line_id in line_ids:
            try:
                line_bot_api.push_message(line_id, TextSendMessage(text='send message'))
                success_ids.append(line_id)
            except:
                fail_ids.append(line_id)

        duration = time.time() - start_time
        print('duration : {duration}\nsuccess : {success}\nfail : {fail}'.format(duration=duration, success=len(success_ids), fail=len(fail_ids)))

def test(request):
    kwargs = {}
    line_ids = ['Uc77987f91d6b6d711338148328f379f4']*505

    groups = []
    if len(line_ids) <= 10:
        groups = [line_ids]

    else:
        thread_num = 10
        size = (len(line_ids) // thread_num) + 1
        for i in range(thread_num):
            groups.append(line_ids[i * size:(i + 1) * size])

    for ids in groups:
        kwargs['line_ids'] = ids
        try:
            thrd = threading.Thread(target=__push_test, kwargs=kwargs, name='text_push')
            thrd.start()
        except Exception as e:
            print(str(e))

    return HttpResponse('test')

