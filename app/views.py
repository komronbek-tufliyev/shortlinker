from django.shortcuts import render
from django.http import Http404
from django.utils import timezone


from .models import UrlShortener, AccessLog
from .forms import UrlShortenerForm

def home_view(request):
    template = 'home.html'
    context = {}
    context['form'] = UrlShortenerForm()
    try:
        if request.method == 'GET':
            return render(request, template, context)
        elif request.method == 'POST':
            used_form = UrlShortenerForm(request.POST)
            if used_form.is_valid():
                shortened_object = used_form.save()
                new_url = request.build_absolute_uri('/') + shortened_object.short_url
                url = shortened_object.url

                context['new_url'] = new_url
                context['url'] = url 

                return render(request, template, context)
            context['error'] = used_form.errors

            return render(request, template, context)
    except Exception as e:
        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    template = 'shortened_url.html'
    try:
        shortener = UrlShortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()

        # Log today's access
        today = timezone.now().date()
        access_log, created = AccessLog.objects.get_or_create(url_shortener=shortener, date=today)
        if not created:
            access_log.count += 1
            access_log.save()

        # Get recent access logs for statistics
        recent_logs = AccessLog.objects.filter(url_shortener=shortener).order_by('-date')[:7]
        dates = [log.date.strftime('%Y-%m-%d') for log in recent_logs]
        follow_counts = [log.count for log in recent_logs]

        context = {
            'url': shortener.url,
            'times_followed': shortener.times_followed,
            'dates': dates[::-1],  # reverse to show oldest to newest
            'follow_counts': follow_counts[::-1]
        }
        return render(request, template, context)
    except UrlShortener.DoesNotExist:
        raise Http404('Sorry, this link is broken :(')