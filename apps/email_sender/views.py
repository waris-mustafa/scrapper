from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .send_email_task import send_email_task


class SendEmailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        send_email_task.delay(request.user.id)
        return Response({'status': 'Emails are being sent'})
