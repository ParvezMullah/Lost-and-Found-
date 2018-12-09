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
    
    serializer_class = LostAndFoundSerializer

    def get_queryset(self):
        search_text = self.request.GET.get('searchText', None)
        lost_or_found = self.request.GET.get('lostOrFound', None)
        queryset = LostAndFound.objects.filter(status='pending')

        if search_text != None and lost_or_found != None:
            queryset = queryset.filter(lost_or_found= lost_or_found, title__icontains=search_text)
        elif lost_or_found != None:
            queryset = queryset.filter(lost_or_found= lost_or_found)
        elif search_text!= None:
            queryset = queryset.filter(title__icontains=search_text)

        return queryset 



class LostAndFoundDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API for retrieving, updating and deleting post.
    """
    queryset = LostAndFound.objects.all()
    serializer_class = LostAndFoundSerializer
    print('detail is called.')


