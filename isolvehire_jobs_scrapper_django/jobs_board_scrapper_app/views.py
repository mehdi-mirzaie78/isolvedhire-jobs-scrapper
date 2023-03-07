from django.shortcuts import render
from jobs_board_scrapper_app.utils import sync_db
# Create your views here.
def sync_db_view(request):
    print("Hey")
    sync_db()
    