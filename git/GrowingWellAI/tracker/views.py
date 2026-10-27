
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DailyRecord
from .serializers import DailyRecordSerializer
from .ai_service import generate_daily_summary

class DailyRecordListAPIView(APIView):

    def post(self, request):
        records = DailyRecord.objects.all().order_by("-record_date")
        serializer = DailyRecordSerializer(records, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# class DailyRecordCreateAPIView(APIView):

#     def post(self, request):
#         record_date = request.data.get("record_date")

#         if not record_date:
#             return Response(
#                 {"error": "Record date is required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         if DailyRecord.objects.filter(record_date=record_date).exists():
#             return Response(
#                 {"error": "A daily record already exists for this date."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = DailyRecordSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )



class DailyRecordUpdateAPIView(APIView):
    def post(self, request):
        record_id = request.data.get('record_id')

        if not record_id:
            return Response(
                {'error': 'record_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            record = DailyRecord.objects.get(id=record_id)
        except DailyRecord.DoesNotExist:
            return Response(
                {'error': 'Daily record not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.data.copy()
        data.pop('record_id', None)

        serializer = DailyRecordSerializer(
            record,
            data=data,
            partial=True
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Update the existing database record
        record = serializer.save()

        # 2. Generate a NEW AI response using updated data
        ai_summary = generate_daily_summary(record)

        # 3. Save the new AI response to the same record
        record.ai_response = ai_summary
        record.save(update_fields=['ai_response'])

        # 4. Return the updated record and new AI response
        updated_serializer = DailyRecordSerializer(record)

        return Response({
            'message': 'Daily record updated successfully',
            'record': updated_serializer.data,
            'ai_summary': ai_summary
        }, status=status.HTTP_200_OK)


class DailyRecordCreateAPIView(APIView):
    def post(self, request):
        record_date = request.data.get("record_date")
        print("record_date .........",record_date)

        if not record_date:
            return Response(
                {"error": "Record date is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if DailyRecord.objects.filter(record_date=record_date).exists():
            return Response(
                {"error": "A daily record already exists for this date."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DailyRecordSerializer(data=request.data)

        if serializer.is_valid():
            
            print("Request date:", request.data.get("record_date"))
            print("Validated date:", serializer.validated_data.get("record_date"))

    
            record = serializer.save()

            ai_summary = generate_daily_summary(record)
            record.ai_response = ai_summary
            record.save(update_fields=['ai_response'])  
            return Response(
                {
                    "message": "Daily record created successfully.",
                    "record": DailyRecordSerializer(record).data,
                    "ai_summary": ai_summary,
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class DailyRecordRetrieveAPIView(APIView):
    def post(self, request):
        record_id = request.data.get('record_id')

        if not record_id:
            return Response(
                {'error': 'record_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            record = DailyRecord.objects.get(id=record_id)
        except DailyRecord.DoesNotExist:
            return Response(
                {'error': 'Daily record not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DailyRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)



class DailyRecordDeleteAPIView(APIView):
    def post(self, request):
        record_id = request.data.get('record_id')

        if not record_id:
            return Response(
                {'error': 'record_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            record = DailyRecord.objects.get(id=record_id)
        except DailyRecord.DoesNotExist:
            return Response(
                {'error': 'Daily record not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        record.delete()

        return Response(
            {'message': 'Daily record deleted successfully'},
            status=status.HTTP_200_OK
        )
