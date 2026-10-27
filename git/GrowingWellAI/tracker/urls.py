
from django.urls import path
from .views import (
    DailyRecordListAPIView,
    DailyRecordCreateAPIView,
    DailyRecordUpdateAPIView,
    DailyRecordRetrieveAPIView,
    DailyRecordDeleteAPIView,
)

urlpatterns = [
    # View all daily records
    path(
        "daily-records/",
        DailyRecordListAPIView.as_view(),
        name="daily-record-list",
    ),

    # Create a daily record
    path(
        "daily-records/create/",
        DailyRecordCreateAPIView.as_view(),
        name="daily-record-create",
    ),

    # Update an existing daily record
    path(
        "daily-records/update/",
        DailyRecordUpdateAPIView.as_view(),
        name="daily-record-update",
    ),

    
    path(
        'daily-records/retrieve/',
        DailyRecordRetrieveAPIView.as_view(),
        name='daily-record-retrieve'
    ),
    path(
        'daily-records/delete/',
        DailyRecordDeleteAPIView.as_view(),
        name='daily-record-delete'
    ),

]
