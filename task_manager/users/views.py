from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = ['Ivan', 'Alex', 'Sansa']
        return render(request, 'users/index.html', context={
            'users': users,
        })
