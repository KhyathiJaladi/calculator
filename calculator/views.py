from django.shortcuts import render

# Create your views here.
def calculatorgame(request):
    result=None
    expression=''

    if request.method=='POST':
        expression=request.POST.get('expression')
        result=eval(expression)
    return render(request,'calculator.html',{'result':result,})

