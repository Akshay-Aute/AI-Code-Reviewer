from django import forms

class CodeReviewForm(forms.Form):
    
    code = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 20,
                "placeholder": "Paste your Python code here..."
            }
        )
    )

    python_file = forms.FileField(
        required=False,
        label="Upload Python File (.py)"
    )