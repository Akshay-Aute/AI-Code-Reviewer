import ast
import tempfile
import pycodestyle


PEP8_HELP = {

    "E231": "Add a space after ','",

    "E225": "Add spaces around operators like + - * /",

    "E111": "Indent using 4 spaces.",

    "W292": "Add a newline at the end of the file.",

}

def analyze_code(code):
    issues = []

    # Empty input
    if not code.strip():
        return [{
            "line": "-",
            "type": "Error",
            "message": "No code provided."
        }]

    # -------------------------
    # Syntax Check
    # -------------------------
    try:
        ast.parse(code)
    except SyntaxError as e:
        issues.append({
            "line": e.lineno,
            "type": "Syntax Error",
            "message": e.msg
        })

    # -------------------------
    # PEP 8 Check
    # -------------------------
    class Report(pycodestyle.BaseReport):

        def __init__(self, options):
            super().__init__(options)
            self.errors = []

        def error(self, line_number, offset, text, check):
            code = text.split()[0]

            self.errors.append({

                "line": line_number,

                "type": "PEP8",

                "message": f"{code} : {' '.join(text.split()[1:])}",

                "suggestion": PEP8_HELP.get(
                code,
                "Refer to PEP8 documentation."
            )

})

            return super().error(line_number, offset, text, check)

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp:

        temp.write(code)
        filename = temp.name

    style = pycodestyle.StyleGuide(quiet=True)

    report = Report(style.options)

    checker = pycodestyle.Checker(
        filename=filename,
        options=style.options,
        report=report
    )

    checker.check_all()

    issues.extend(report.errors)

    if not issues:
        issues.append({
            "line": "-",
            "type": "Success",
            "message": "Code follows basic syntax and PEP 8 guidelines."
        })

    return issues