from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import JobPosting, SavedJob
from .serializers import JobPostingSerializer, SavedJobSerializer
from .filters import SavedJobFilter, JobPostingFilter

class JobPostingListCreateView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class JobPostingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class SavedJobViewSet(viewsets.ModelViewSet):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SavedJobFilter
    search_fields = ['job_posting__title', 'job_seeker__user__email']
    ordering_fields = ['saved_at']
    ordering = ['-saved_at']

    def get_queryset(self):
        return SavedJob.objects.filter(job_seeker=self.request.user.jobseeker)

    def perform_create(self, serializer):
        serializer.save(job_seeker=self.request.user.jobseeker)
        
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.filter(is_active=True).order_by('-posted_date')
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JobPostingFilter
    search_fields = ['title', 'description', 'company__name', 'location']
    ordering_fields = ['posted_date', 'salary_min', 'salary_max']
    ordering = ['-posted_date']