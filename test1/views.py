from django.shortcuts import render
from .models import *
from utils.wrappers import *
from django.http import HttpResponse


def index(request):
    cags = Category.objects.all()
    return render(request, 'test_page.html', locals())


def add_handle(request):
    # 先获取cag_name,去数据库查询是否存在
    cags_name = post(request, 'cag_name')
    good_name = post(request, 'goods_name')
    # 健壮性判断，减少服务器压力
    if cags_name == '' or good_name == '':
        return
    # cag_name默认不存在
    flag = False
    cag = Category.objects.get_caginfo_by_name(cags_name)
    if cag:
        flag = True

    # cag_name 存在，只新增商品信息
    if flag:
        goods = GoodsList()
        goods.goods_name = good_name
        goods.goods_link = good_name
        goods.goods_cag_id = cag.id
        goods.save()
        return HttpResponse('新增{}类商品成功!'.format(cags_name))
    else:
        cag = Category()
        goods = GoodsList()
        cag.cag_name = cags_name
        cag.cag_link = 'By ' + cags_name
        cag.save()
        goods.goods_name = good_name
        goods.goods_link = good_name
        goods.goods_cag_id = cag.id
        goods.save()
        return HttpResponse('新增类别商品成功！')