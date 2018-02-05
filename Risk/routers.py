"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from rest_framework import routers

# Django Dynamic Models Stuff
from Risk.users.auth.api import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', AuthViewSet, base_name='auth')
