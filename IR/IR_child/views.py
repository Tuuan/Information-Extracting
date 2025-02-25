from django.shortcuts import render

# Create your views here.

def upload_file(request):
    if request.method == "POST" and request.FILES["file"]:
        uploaded_file = request.FILES["file"]
        #content là nội dung
        content = uploaded_file.read().decode("utf-8")
        print("result", content)
        return render(request, 'home.html', context = { 'data': content })
    return render(request, 'home.html')
