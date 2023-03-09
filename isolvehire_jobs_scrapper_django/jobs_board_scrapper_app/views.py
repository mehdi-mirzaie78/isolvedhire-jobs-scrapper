from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator, EmptyPage
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
        jobs = Job.objects.filter(is_removed=False)
        form = self.form_class(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in cd.items():
                if value:
                    if key == 'title':
                        jobs = jobs.filter(title__contains=value)
                    elif key == 'location':
                        jobs = jobs.filter(location__contains=value)
                    elif key == 'payment_start':
                        jobs = jobs.filter(pay__gte=value)
                        print(value, type(value))
                    elif key == 'payment_end':
                        jobs = jobs.filter(pay__lt=value)
                    elif key == 'payment_type':
                        jobs = jobs.filter(pay_type__contains=value)
                    elif key == 'employment_type':
                        jobs = jobs.filter(employment_type__contains=value)
                    elif key == 'start_date':
                        jobs = jobs.filter(modified__gte=value)
                    elif key == 'end_date':
                        jobs = jobs.filter(modified__lte=value)
        
        p = Paginator(jobs, 2)
        page = request.GET.get('page')
        page_jobs = p.get_page(page)
        nums = "a" * page_jobs.paginator.num_pages
        return render(request, self.template_name, {'page_jobs': page_jobs, 'nums': nums, 'form': form})

   