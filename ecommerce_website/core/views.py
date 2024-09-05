from django.shortcuts import render

def fontpage(request):
    return  render(request,'core/fontpage.html')
def about(requet):
    return render(requet,'core/about.html')
