from mango_db_app import models, serializers
from.models import PlacementDetails
from.serializers import ass_serial
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

######################################################post method #########################################################################
class Postdetails(GenericAPIView):
    serializer_class = serializers.ass_serial
    def post(self,request):
        try:
            serializer_class=serializers.ass_serial(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
        except Exception as e:
            return Response(e)


#######################################get details using particular name (custom serializer)####################################################

class Getname_details(GenericAPIView):
    serializer_class = serializers.Candidate
    queryset = models.PlacementDetails
    def post(self,request):
        try:
            query_set=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'])
            serializer_class = serializers.ass_serial(query_set,many=True)
            return Response(serializer_class.data)
        except Exception as e:
            return Response(e)

############################################get all details #############################################################
class Getall_details(GenericAPIView):
    serializer_class = serializers.Candidate
    queryset = models.PlacementDetails
    def get(self,request):
        try:
            query_set=models.PlacementDetails.objects.all()
            serializer_class = serializers.ass_serial(query_set,many=True)
            return Response(serializer_class.data)
        except Exception as e:
            return Response(e)


############################################### update using primary key  method #################################################
class UpdateView(GenericAPIView):
    serializer_class = serializers.ass_serial

    def put(self, request, work_order_no):
        try:
            query_set = models.PlacementDetails.objects.get(work_order_no=work_order_no)
            serializer_instance = serializers.ass_serial(instance=query_set, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data)

        except Exception as e:
            return Response(e)



###################################################delete all details ####################################################

class Delete_all(GenericAPIView):
    serializer_class = serializers.ass_serial
    def delete(self,request):
        try:
            query_set = models.PlacementDetails.objects.all().delete()
            return Response("successfully deleted")
        except Exception as e:
            return Response(e)



#################################################delete particular row using primary key##################################33

class delelet_single(GenericAPIView):
    serializer_class = serializers.ass_serial
    def delete(self,request,candidate_name):
        try:
            query_set = models.PlacementDetails.objects.filter(candidate_name=candidate_name).delete()
            return Response('successfully deleted')
        except Exception as e:
            return Response(e)


#-----------------------------------------------------------------------------------------------------------------------








