from django.test import TestCase

from numberwords.forms import NumberForm

# testing is a bit silly with a single field like normally I would try check the models
class NumberFormTests(TestCase):
    def test_numbers_are_valid(self):
        form = NumberForm({
            'number': 1234,
        })
        self.assertTrue(form.is_valid())

    def test_strings_are_invalid(self):
        form = NumberForm({
            'number': "one hundred",
        })
        self.assertFalse(form.is_valid())


    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


    # I would generally also separate integration tests BUT there's just not much going on in the project
    def test_form_submit_resturns_words(self):
        data = {
            'number': 1234,
        }
        response = self.client.post("/", data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('one thousand, two hundred and thirty-four' in str(response.content))

