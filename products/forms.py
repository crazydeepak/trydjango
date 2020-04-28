from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title= forms.CharField(label='Title',widget= forms.TextInput(attrs={"placeholder":"Your Title"})) #default is True
    email=forms.EmailField()
    description= forms.CharField(required=False,widget=forms.Textarea(attrs=
                            {
                                "placeholder" : "Your Description is",
                                "class" : "new-class-name",
                                "id" : "my-id",
                                "rows":20,
                                "columns":120

                            }
                            ))
    price= forms.DecimalField(initial=100.00)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
       ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        print("--------"+ title)
        if not 'abc' in title:
            raise forms.ValidationError("This is not a valid title")
        if not 'def' in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title

    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        if not email.endswith("Edu"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email


class RawProductForm(forms.Form):
    title= forms.CharField(label='Title',widget= forms.TextInput(attrs={"placeholder":"Your Title"})) #default is True
    description= forms.CharField(required=False,widget=forms.Textarea(attrs=
                            {
                                "placeholder" : "Your Description",
                                "class" : "new-class-name",
                                "id" : "my-id",
                                "rows":20,
                                "columns":120

                            }
    
                            ))
    price= forms.DecimalField(initial=100.00)