from django.shortcuts import render, redirect
from django.views import View
from .models import Job
from .forms import JobForm
from jobs_board_scrapper_app.utils import sync_db


def sync_db_view(request):
    print("Hey")
    sync_db()
    return redirect('home')


class JobsView(View):
    form_class = JobForm
    template_name = 'home.html'

    def get(self, request):
        # sync_db()     # we can sync each time we want to get all jobs
        jobs = Job.objects.all()
        return render(request, self.template_name, {'jobs': jobs, 'form': self.form_class})

    def post(self, request):
        jobs = Job.objects.all()
        form = self.form_class(request.POST)
        if form.is_valid():
            print('here')
            cd = form.cleaned_data
            title, start_date, end_date = cd['title'], cd['start_date'], cd['end_date']
            if all([start_date, end_date, title]):
                jobs = Job.objects.filter(
                    title=title, modified__range=(start_date, end_date))
            elif all([start_date, end_date]):
                jobs = Job.objects.filter(
                    modified__range=(start_date, end_date))
            elif title:
                jobs = Job.objects.filter(title__contains=title)
            elif start_date:
                jobs = Job.objects.filter(modified__gte=start_date)
            elif end_date:
                jobs = Job.objects.filter(modified__lte=end_date)
            print(jobs)
            return render(request, self.template_name, {'jobs': jobs, 'form': form})
        return render(request, self.template_name, {'form': form, 'jobs': jobs})
