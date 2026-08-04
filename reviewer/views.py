from django.shortcuts import render
from .forms import CodeReviewForm
from .analyzer import analyze_code


def home(request):

    form = CodeReviewForm()

    issues = None

    total = 0
    syntax = 0
    pep8 = 0
    score = 100          # Default score

    if request.method == "POST":

        form = CodeReviewForm(request.POST)

        if form.is_valid():

            code = form.cleaned_data["code"]

            issues = analyze_code(code)

            total = len(issues)

            syntax = len([
                i for i in issues
                if i["type"] == "Syntax Error"
            ])

            pep8 = len([
                i for i in issues
                if i["type"] == "PEP8"
            ])

            score = max(0, 100 - (total * 5))

    return render(request, "home.html", {
        "form": form,
        "issues": issues,
        "total": total,
        "syntax": syntax,
        "pep8": pep8,
        "score": score,
    })