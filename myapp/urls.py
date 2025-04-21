from django.urls import path
from .views import hello_api, receive_post

urlpatterns = [
    path('hello/', hello_api),
    path('post/', receive_post), # ⟵ 여기에 동작코드를 작성하세요(2점)
]
