from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List


class ItemModelTest(TestCase):
    """Item model test"""

    def test_default_text(self):
        """test for default text"""
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        """test: item linked with text"""
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_cannot_save_empty_list_items(self):
        """test: cannot add empty list item"""

        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_are_invalid(self):
        """test: not unique item is forbidden"""
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            itew = Item(list=list_, text='bla')
            itew.full_clean()
            # itew.save()

    def test_CAN_save_same_iterm_to_different_lists(self):
        """test: CAN save same item in different lists"""
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() # shouldn't rise an Exception

    def test_list_ordering(self):
        """test ordered list"""
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )

    def test_string_representation(self):
        """test string view"""
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')


class ListModelTest(TestCase):
    """List model test"""

    def test_get_absolute_url(self):
        """test: get absolute url"""

        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')
