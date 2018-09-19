# from django.conf.urls import patterns, url
from django.urls import path, re_path, include
from django.contrib.auth.decorators import permission_required

from design_products.views import index   # GoodsListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete, RssGoodsListFeed, AtomGoodsListFeed



urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', index, name = "goods_index"),
]