from django.shortcuts import render, HttpResponse
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


class UserFormUpdateView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request to users/{id}/update')
        # form = UserForm()
        # return render(request, 'users/create.html', context={
        #     'form': form,
        # })

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request to users/{id}/update')
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('users')
        # messages.warning(request, 'Incorrect data!')
        # return render(request, 'users/create.html', context={
        #     'form': form})


class UserFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request to users/{id}/delete')
        # user_id = kwargs.get('id')
        # user = User.objects.get(id=user_id)
        # if user:
        #     user.delete()
        #     messages.warning(request, 'Пользователь удален')
        # return redirect('users')
