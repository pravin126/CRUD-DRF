from .models import Post
from rest_framework.decorators import authentication_classes,permission_classes 
from .serializers import PostSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .cpp import MyPermission

class LCPostAPI(GenericAPIView,ListModelMixin,CreateModelMixin):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[MyPermission]

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    

#RUD
class RUDPostAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)



# class PostList(GenericAPIView,ListModelMixin):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)
    

# #Create
# class PostCreate(GenericAPIView,CreateModelMixin):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args,**kwargs)
    
# #Retriv
# class PostRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
# #Update
# class PostUpdate(GenericAPIView,UpdateModelMixin):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)
    

# #Distroy
# class PostDestroy(GenericAPIView,DestroyModelMixin):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request,*args,**kwargs)