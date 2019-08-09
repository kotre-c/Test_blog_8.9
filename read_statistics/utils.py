# -*- coding: utf-8 -*-
# @Time    : 18-11-17 下午10:03
# @Author  : Felix Wang
import datetime
from django.db.models import Sum
from django.utils import timezone
from .models import ReadDetail, ReadNum
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum


def read_statistics_once_read(requests, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '{}_{}_read'.format(ct.model, obj.pk)

    # 获取并处理阅读计数
    if not requests.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # 处理阅读量
        readnum.read_num += 1
        readnum.save()


        # 当天阅读量+1
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums
