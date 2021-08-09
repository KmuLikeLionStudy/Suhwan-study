def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

