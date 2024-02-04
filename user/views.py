from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from user.forms import AccountForm, DepositeForm, ReviewForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from books.models import BookModel
from borrow_books.models import BorrowModel
from user.models import Review
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

def user_email(user, amount, mail_subject, template):
    message = render_to_string(template,{
        'user' : user,
        'amount' : amount,
    })

    send_email = EmailMultiAlternatives(mail_subject, '', to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()


class SignUpView(FormView):
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_class = AccountForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'SignUp'
        return context

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def deposite(request):
    form = DepositeForm(request.POST)
    if form.is_valid():
        amount = form.cleaned_data['amount']
        user = request.user.account
        user.balance += amount
        user.save(
            update_fields = ['balance']
        )

        user_email(request.user, amount, 'Deposite Message', 'deposite_email.html')

    return render(request, 'deposite.html', {'form':form, 'type':'Deposite'})

@login_required
def borrow(request, book_id):
    book = BookModel.objects.get(id=book_id)
    user = request.user.account
    if user.balance > book.price:
        user.balance -= book.price
        user.save(
            update_fields = ['balance']
        )
        try:
            obj = BorrowModel.objects.get(book_title=book)
            messages.error(request, f' {obj.book_title} - this book already you borrowed!')
            return redirect('profile')
        except BorrowModel.DoesNotExist:
            BorrowModel.objects.create(
                user = request.user,
                book_id = book_id,
                book_title = book.title,
                borrow_price = book.price,
            )

            message = render_to_string('borrow_email.html',{
                'user' : request.user,
                'book' : book.title,
                'price' : book.price
            })
            send_email = EmailMultiAlternatives('Borrow Book', '', to=[request.user.email])
            send_email.attach_alternative(message,"text/html")
            send_email.send()

    else:
        messages.error(request, f'You have not enough money to borrow this book')
    return redirect('profile')

@login_required
def profile(request):
    borrow_report = BorrowModel.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user':request.user, 'borrow_report': borrow_report})

@login_required
def review(request, book_id):
    book = BookModel.objects.get(id=book_id)
    initial_data = {'user':request.user, 'book':book}
    form = ReviewForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ReviewForm(initial=initial_data)
    review = Review.objects.filter(book=book)
    form.fields['user'].widget.attrs['disabled'] = 'disabled'
    form.fields['book'].widget.attrs['disabled'] = 'disabled'
    return render(request, 'book_review.html', {'form':form, 'reviews':review, 'type': book.title})

@login_required
def return_book(request, book_id):
    book = BookModel.objects.get(id=book_id)
    report = BorrowModel.objects.get(book_title=book)
    account = request.user.account
    account.balance += report.borrow_price 
    account.save(
        update_fields = ['balance']
    )
    messages.success(request, f'Returned a book successfully! your balance also returned to your account')
    report.delete()
    return redirect('profile')