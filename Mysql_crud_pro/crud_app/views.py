from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from crud_app import models, serializers
from crud_app.models import stud_table
from crud_app.serializers import serialdata,getpost


class Fetchview(GenericAPIView):
    serializer_class = serializers.serialdata
    queryset = stud_table

    def get(self, request):
        query_set = models.stud_table.objects.all()
        serializer_class = serializers.serialdata(query_set, many=True)
        return Response(serializer_class.data)

class FetchAllview(GenericAPIView):
    #serializer_class = serializers.serialdata
    def get(self, request,id):
        query_set = models.stud_table.objects.get(id=id)
        serializer_class = serializers.serialdata(query_set)
        return Response(serializer_class.data)


class Createview(GenericAPIView):
   serializer_class = serializers.serialdata
   def post(self, request):
        try:
            serializer_class = serializers.serialdata(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
            return Response(serializer_class.data)
        except Exception as k:
            print('invalid', k)
            return Response(k)


class updateview(GenericAPIView):
    serializer_class = serializers.serialdata

    def put(self,request,id):

            query_set = models.stud_table.objects.get(id=id)
            serializer_class = serializers.serialdata(instance=query_set,data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)



class  delview(GenericAPIView):
    serializer_class = serializers.serialdata
    def delete(self,request,id):
        try:
            query_set=models.stud_table.objects.get(id=id)
            query_set.delete()
            return Response('successfully deleted')
        except Exception as e:
            print('invalid data', e)
            return Response(e)


class getposttt(GenericAPIView):
    serializer_class = serializers.getpost
    queryset = stud_table
    def post(self,request):
        queryset = stud_table.objects.filter(name=request.data['name'])
        serializer = serialdata(queryset,many=True)
        datas = {'output':serializer.data}
        return Response(datas)


class DuplicatesView(GenericAPIView):
    serializer_class = serialdata
    queryset = stud_table
    def get(self, request):
        queryset = stud_table.objects.all()
        serializer_class = serializers.serialdata(queryset, many=True)
        for i in range(len(serializer_class)):
            data={'geography':serializer_class[i]['geography']}
        return Response(data)
