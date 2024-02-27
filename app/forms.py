from django import forms


class Postform(forms.Form):
    title = froms.CharField(max_length=30, Label="タイトル")
    content = forms.CharField(Label="内容", widget=forms.Textarea())
