from django import forms

from .models import NewProduct, ONE_TO_TEN_CHOICES


class NewProductForm(forms.ModelForm):
    class Meta:
        model = NewProduct
        fields = (
            'source',
            'bought_products',
            'city',
            'age',
            'specialization',
            'income_rub',
            'operations_status',
            'study_goal',
            'current_difficulties',
            'attempted_solutions',
            'subscription_info',
            'top_questions',
            'warmup_level',
            'workload_level',
            'full_name',
            'instagram',
            'telegram_channel',
            'telegram',
            'phone',
            'email',
            'policy_agreement',
        )
        widgets = {
            'source': forms.RadioSelect,
            'bought_products': forms.RadioSelect,
            'operations_status': forms.RadioSelect,
            'warmup_level': forms.RadioSelect,
            'workload_level': forms.RadioSelect,
            'city': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'age': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'specialization': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'income_rub': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'study_goal': forms.Textarea(attrs={'placeholder': 'Мой ответ', 'class': 'auto-resize-textarea', 'rows': 1}),
            'current_difficulties': forms.Textarea(attrs={'placeholder': 'Мой ответ', 'class': 'auto-resize-textarea', 'rows': 1}),
            'attempted_solutions': forms.Textarea(attrs={'placeholder': 'Мой ответ', 'class': 'auto-resize-textarea', 'rows': 1}),
            'subscription_info': forms.Textarea(attrs={'placeholder': 'Мой ответ', 'class': 'auto-resize-textarea', 'rows': 1}),
            'top_questions': forms.Textarea(attrs={'placeholder': 'Мой ответ', 'class': 'auto-resize-textarea', 'rows': 1}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'telegram_channel': forms.TextInput(attrs={'placeholder': 'Мой ответ'}),
            'telegram': forms.TextInput(attrs={'placeholder': 'https://t.me/doc_malahova или @username'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (999) 999-99-99'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'policy_agreement': forms.CheckboxInput(attrs={'style': 'display:none'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = True
            field.error_messages.update({'required': 'Обязательное поле'})

        self.fields['source'].choices = list(NewProduct.SOURCE_CHOICES)
        self.fields['bought_products'].choices = list(NewProduct.BOUGHT_PRODUCTS_CHOICES)
        self.fields['operations_status'].choices = list(NewProduct.OPERATIONS_STATUS_CHOICES)
        self.fields['warmup_level'].choices = list(ONE_TO_TEN_CHOICES)
        self.fields['workload_level'].choices = list(ONE_TO_TEN_CHOICES)
