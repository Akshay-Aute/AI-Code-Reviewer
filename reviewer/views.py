from django.shortcuts import render
from .forms import CodeReviewForm
from .analyzer import analyze_code
from .analyzer import analyze_code, fix_code


def home(request):

    form = CodeReviewForm()

    issues = None

    total = 0
    syntax = 0
    pep8 = 0
    score = 100  # Default score

    if request.method == "POST":

        form = CodeReviewForm(request.POST, request.FILES)

        if form.is_valid():

            code = form.cleaned_data["code"]

            uploaded_file = request.FILES.get("python_file")

            # If a file is uploaded, use its contents
            if uploaded_file:

                if not uploaded_file.name.endswith(".py"):

                    issues = [{
                        "line": "-",
                        "type": "Error",
                        "message": "Only Python (.py) files are allowed.",
                        "suggestion": "Please upload a .py file."
                    }]

                else:
                    code = uploaded_file.read().decode("utf-8")

            # Analyze only if there are no upload errors
            if issues is None:

                fixed_code = ""

                issues = analyze_code(code)

                fixed_code = fix_code(code)

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
        "fixed_code": fixed_code,
    })