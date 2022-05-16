from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.
def rental_review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thankyou'))

    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html',context={'form':form})


def thankyou(request):
    return render(request, 'cars/thankyou.html')