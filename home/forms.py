from django import forms

CATEGORIES = [
        ("Graphics", "Graphics"),
        ("Illustrations", "Illustrations"),
        ("Icons", "Icons"),
        ("Posters", "Posters"),
    ]    
DESIGN_SIZES = [
        ("Instagram", "Instagram"),
        ("Facebook", "Facebook"),
        ("X", "X"),
        ("YouTube", "YouTube"),
        ("Pinterest", "Pinterest"),
        ("Snapchat", "Snapchat"),
        ("Custom", "Custom"),
    ]


class QuoteForm(forms.Form):

    category = forms.ChoiceField(choices=CATEGORIES)

    name = forms.CharField(max_length=254)
    description = forms.CharField(widget=forms.Textarea(), max_length=254)
    size = forms.ChoiceField(choices=DESIGN_SIZES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
