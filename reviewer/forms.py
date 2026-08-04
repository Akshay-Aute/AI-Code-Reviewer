from django import forms

class CodeReviewForm(forms.Form):
    code = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 18,
                "placeholder": "Paste your Python code here..."
            }
        )
    )