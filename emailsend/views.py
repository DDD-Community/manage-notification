from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from notification.models import Notification
from notification.serializers import NotificationSerializer
from project.utils import custom_response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

class SendEmailView(APIView):
    
    @swagger_auto_schema(
        operation_description="이메일 발송 API",
        operation_summary="이메일 발송 API",
        responses={
            200: NotificationSerializer(many=True),  # 성공 시 발송된 Notification 객체 리스트 반환
            400: "Bad Request"  # 실패 시 응답 코드
        }
    )
    def post(self, request):
        # email_sent가 0인 Notification 객체들 조회
        notifications = Notification.objects.filter(email_sent=0)

        # 이메일 발송
        for notification in notifications:
            send_mail(
                subject="Notification",
                message=f"안녕하세요, {notification.name}님. 여기 당신의 알림이 있습니다.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[notification.email],
            )
            # email_sent 필드를 1로 업데이트
            notification.email_sent = 1
            notification.save()

        # 발송된 객체들을 시리얼라이즈하여 반환
        serializer = NotificationSerializer(notifications, many=True)
        return custom_response(data=serializer.data, status_code=status.HTTP_200_OK)