from django.shortcuts import render

# Create your views here.

def encouragement(request):
    phrase = "Keep going, you’re doing great! 💪"
    show_image = request.GET.get("show_image", False)
    return render(request, "encouragement.html", {"phrase": phrase, "show_image": show_image})
