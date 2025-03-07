from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialzer import ConversionSerializer
from django.http import JsonResponse


class WeightConversionView(APIView):

    def post(self, request):
        if request.method == "OPTIONS":
            response = JsonResponse({"message": "CORS preflight response"})
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            return response
        if request.method == "POST":
            serializer = ConversionSerializer(data=request.data)

            if serializer.is_valid():
                value = serializer.validated_data["value"]
                unit_to = serializer.validated_data["unit_to"]

                if unit_to == "kg":
                    converted_value = value / 1000
                elif unit_to == "mg":
                    converted_value = value * 1000
                elif unit_to == "ton":
                    converted_value = value / 1000000
                elif unit_to == "lb":
                    converted_value = value / 453.592
                elif unit_to == "oz":
                    converted_value = value / 28.3495
                else:
                    converted_value = value

                return Response(
                    {converted_value}, status=status.HTTP_200_OK
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
