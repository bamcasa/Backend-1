from django.urls import path
from .views import (
    RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView, RestaurantListView,
    MenuCreateView, MenuUpdateView, MenuDeleteView, MenuListView,
    MenuDetailView, MenuDetailByIdView,     
    MenuSearchView, MenuSearchByTimeView
)

urlpatterns = [
    path('restaurant/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
    path('restaurant/all/', RestaurantListView.as_view(), name='restaurant-list'),
    
    path('menu/', MenuCreateView.as_view(), name='menu-create'),
    path('menu/<int:pk>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('menu/<int:pk>/delete/', MenuDeleteView.as_view(), name='menu-delete'),
    path('menu/all/', MenuListView.as_view(), name='menu-list'),

    path('menu/detail/namedate/', MenuDetailView.as_view(), name='menu-detail'),  # restaurant와 date는 query_params로 받음
    path('menu/detail/id/<int:pk>/', MenuDetailByIdView.as_view(), name='menu-detail-by-id'),  # 메뉴 ID로 세부정보 가져오기

    path('menu/detail/', MenuSearchView.as_view(), name='menu_search'),
    path('menu/detail/datetime/', MenuSearchByTimeView.as_view(), name='menu_search_by_time'),
]


# /menu/detail/namedate/?restaurant=레스토랑이름&date=YYYY-MM-DD
# 예시) GET /menu/detail/namedate/?restaurant=교직원식당&date=2024-10-28

# /menu/detail/?restaurant=레스토랑이름&date=2024-11-04&time=아침
# /menu/detail/datetime/?date=2024-11-04&time=중식

