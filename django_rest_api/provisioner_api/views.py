from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import PostgreSQLVM
from .serializers import GroupSerializer, UserSerializer, PostgreSQLVMSerializer

from pg_provisioner import PgProvisioner

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostgreSQLVMViewSet(viewsets.ModelViewSet):

    queryset = PostgreSQLVM.objects.all().order_by("-created_at")
    serializer_class = PostgreSQLVMSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        instance = serializer.save(status="Started")

        # here we use the Python CLI to trigger the Ansible provision

        pg_provisioner = PgProvisioner()

        pg_provisioner.start_pg_vm_provisioning()


