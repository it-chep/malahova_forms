from django.test import SimpleTestCase

from business_forms.forms import NewProductForm


class NewProductFormTests(SimpleTestCase):
    def test_contact_fields_are_required(self):
        form = NewProductForm()

        for field_name in ("full_name", "instagram", "telegram_channel", "telegram", "phone", "email"):
            self.assertTrue(form.fields[field_name].required, field_name)
