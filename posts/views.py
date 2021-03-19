from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    # テンプレートで参照する名前を分かりやすい名前に変更
    context_object_name = 'all_posts_list'
