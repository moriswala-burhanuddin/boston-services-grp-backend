from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Lead, LeadPhoto
from .serializers import LeadSerializer, LeadAdminSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        lead = serializer.save()
        photos = self.request.FILES.getlist('photos')
        for photo in photos:
            LeadPhoto.objects.create(lead=lead, image=photo)
    
    def get_serializer_class(self):
        # Use admin serializer for non-create actions (allows status updates)
        if self.action == 'create':
            return LeadSerializer
        return LeadAdminSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Anyone can submit a lead
            permission_classes = [AllowAny]
        else:
            # Only authenticated admin can view/update/delete leads
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        lead = self.get_object()
        subject = request.data.get('subject', 'Message regarding your Service Request')
        message = request.data.get('message', '')

        if not message:
            return Response({'error': 'Message content is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Context for the templates
        context = {
            'lead': lead,
            'admin_message': message,
        }

        # Render HTML and plain text templates
        text_content = render_to_string('leads/email_quotation.txt', context)
        html_content = render_to_string('leads/email_quotation.html', context)

        # Create the email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'hello@bostonservices.com'),
            to=[lead.email],
        )
        email.attach_alternative(html_content, "text/html")

        try:
            email.send()
            # Optionally update the status automatically when an email is sent
            if lead.status == 'NEW':
                lead.status = 'CONTACTED'
                lead.save()
            return Response({'status': 'email sent successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

