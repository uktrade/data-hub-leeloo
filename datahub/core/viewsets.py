from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class ArchiveNoDeleteViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    """Implement the archive route and the read/write serializers."""

    read_serializer_class = None
    write_serializer_class = None

    @detail_route(methods=['post'])
    def archive(self, request, pk):
        """Archive the object."""
        reason = request.data.get('reason', '')
        obj = self.get_object()
        obj.archive(user=request.user, reason=reason)
        serializer = self.read_serializer_class(obj)
        return Response(data=serializer.data)

    @detail_route(methods=['get'])
    def unarchive(self, request, pk):
        """Unarchive the object."""
        obj = self.get_object()
        obj.unarchive()
        serializer = self.read_serializer_class(obj)
        return Response(data=serializer.data)

    def get_serializer_class(self):
        """Return a different serializer class for reading or writing, if defined."""
        if self.action in ('list', 'retrieve', 'archive'):
            return self.read_serializer_class
        elif self.action in ('create', 'update', 'partial_update'):
            return self.write_serializer_class

    def get_object(self):
        """Force the update from korben."""
        object = super(ArchiveNoDeleteViewSet, self).get_object()
        object = object.update_from_korben()
        return object
