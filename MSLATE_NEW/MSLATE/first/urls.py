
from django.urls import path, include
from .views import UserDetailsList, AscedingUserList, DescendingUserList
urlpatterns = [
    path('', UserDetailsList.as_view(), name="userdetails"),
    path('asc/', AscedingUserList.as_view(), name="asc"),
    path('desc/', DescendingUserList.as_view(), name="desc"),
]