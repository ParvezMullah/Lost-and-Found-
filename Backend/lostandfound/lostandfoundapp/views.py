from lostandfoundapp.models import LostAndFound
from lostandfoundapp.serializers import LostAndFoundSerializer
from rest_framework import generics



class LostAndFoundCreate(generics.CreateAPIView):
    """
    API for creating a post
    """
    queryset = LostAndFound.objects.all()
    serializer_class = LostAndFoundSerializer



class LostAndFoundList(generics.ListAPIView):
    """
    API for listing post
    """
    queryset = LostAndFound.objects.all()
    serializer_class = LostAndFoundSerializer



class LostAndFoundDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API for retrieving, updating and deleting post.
    """
    queryset = LostAndFound.objects.all()
    serializer_class = LostAndFoundSerializer


