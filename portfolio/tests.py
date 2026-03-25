from django.test import TestCase

class HomeRedirectTest(TestCase):
    def test_home_redirect(self):
        response = self.client.get("/")
        # We expect a redirect to the project admin page.
        # This will further redirect to login if not authenticated (hence target_status_code=302).
        self.assertRedirects(response, "/admin/portfolio/project/", status_code=302, target_status_code=302)
