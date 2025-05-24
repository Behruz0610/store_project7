from django import forms
from .models import Order, Comment

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'quantity']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content', 'rating']