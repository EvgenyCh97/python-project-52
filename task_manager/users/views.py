from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = [{'id': 1, 'name': 'Alex', 'full_name': 'Alex Petrov',
                  'created_at': '2023-12-22'},
                 {'id': 2, 'name': 'Sansa', 'full_name': 'Sansa Stark',
                  'created_at': '2023-12-20'},
                 {'id': 3, 'name': 'Lev', 'full_name': 'Lev Tolstoy',
                  'created_at': '1950-10-24'}
                 ]
        return render(request, 'users/index.html', context={
            'users': users,
        })
