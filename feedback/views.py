# Influenced majorly by Codewouter and CI Boutique Ado Tutorial#

from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Menu
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.


def view_feedback(request, menu_id):
    """"
    Gets specific menu and displays comment
    """
    menu = get_object_or_404(Menu, pk=menu_id)
    feedback_list = Feedback.objects.all().filter(menu=menu)

    template = 'feedback/comments.html'
    context = {
        'feedback_list': feedback_list,
        'menu': menu
    }

    return render(request, template, context)


def add_feedback(request, menu_id):

    menu = get_object_or_404(Menu, pk=menu_id)
    print('menu_id={}'.format(str(menu_id)))
    print(str(menu))
    feedback_list = Feedback.objects.all().filter(menu=menu)
    """
    This function is called when the comment button is clicked
    Checks if form is valid and the comment is added to the database.
    """

    if request.method == "POST":
        new_comment = FeedbackForm(request.POST)
        if new_comment.is_valid():
            feedback = Feedback(
                menu=menu,
                name=request.POST.get('name'),
                comment=request.POST.get('comment')
            )
            print(str(feedback))
            feedback.save()
            
            template = 'feedback/comments.html'
            context = {
                'feedback_list': feedback_list,
                'menu': menu
            }

            return render(request, template, context)
        else:
            print('invalid')
    else:
        new_comment = FeedbackForm()

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
