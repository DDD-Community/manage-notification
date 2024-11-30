from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from notification.models import Notification
from notification.serializers import NotificationSerializer
from project.utils import custom_response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from emailsend.models import EmailTemplate

class SendEmailView(APIView):
    
    @swagger_auto_schema(
        operation_description="이메일 발송 API",
        operation_summary="이메일 발송 API",
        responses={
            200: NotificationSerializer(many=True),
            400: "Bad Request"
        }
    )
    def post(self, request):
        notifications = Notification.objects.filter(email_sent=0)

        email_template = EmailTemplate.objects.order_by('-created_at').first()
        if not email_template:
            return custom_response(
                data={"error": "사용할 수 있는 이메일 템플릿이 없습니다."},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        for notification in notifications:
            subject = email_template.title
            html_message = email_template.body.replace("{name}", notification.name)  # body에서 {name} 변환

            send_mail(
                subject=subject,
                message="HTML 지원이 필요합니다. HTML 템플릿을 확인하세요.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[notification.email],
                html_message=html_message
            )
            notification.email_sent = 1
            notification.save()

        serializer = NotificationSerializer(notifications, many=True)
        return custom_response(data=serializer.data, status_code=status.HTTP_200_OK)