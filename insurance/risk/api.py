# Third Party Stuff
from rest_framework import permissions, viewsets

from .models import Risk
from .permissions import IsOwnerOrReadOnly
from .serializers import RiskSerializer


class RiskViewSet(viewsets.ModelViewSet):
    '''
    Methods available to everyone
    -----------------------------
    LIST
    ====
    Gets all the risks ever added.
    Example:
    GET http://127.0.0.1:8000/api/risk

    {
        "name": "automobile",
        "insurer": "66af9719-46e0-4495-bd85-f78950c5081b",
        "riskfields": [
            {
                "name": "purchase date",
                "ftype": "dt"
            },
            {
                "name": "motor company",
                "ftype": "ch"
            }
        ]
    }

    RETRIEVE
    ========
    Gets a particular risk based on id provided in the url.
    Example:
    GET http://127.0.0.1:8000/api/risk/99c7a59c-2b7e-471d-b1b5-5eb6aa27948c

    {
        "name": "life",
        "insurer": "66af9719-46e0-4495-bd85-f78950c5081b",
        "riskfields": [
            {
                "name": "name of insuree",
                "ftype": "ch"
            }
        ]
    }
    '''
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
