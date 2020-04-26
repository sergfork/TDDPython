from django.test import TestCase
from lists.forms import EMPTY_ITEM_ERROR, ItemForm

class ItemFormTest(TestCase):
    """item list form test"""

    def test_form_renders_item_text_input(self):
        """test: form displays input text field"""
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())
        # self.fail(form.as_p())

    def test_form_validation_for_blank_items(self):
        """form validation test for empty items"""
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'], [EMPTY_ITEM_ERROR]
        )
