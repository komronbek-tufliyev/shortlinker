# ShortLinker

**ShortLinker** is a URL shortening website that allows users to create shortened URLs that redirect to the original URLs. Users can view statistics on the number of times a shortened URL has been accessed and see visualizations of recent activity.

## Features

- **URL Shortening**: Enter a long URL and get a short, unique URL in return.
- **Redirection**: Clicking on a shortened URL redirects to the original URL.
- **Usage Statistics**: Track the number of clicks for each shortened URL.
- **Activity Visualization**: View a chart of recent activity (e.g., daily clicks) for each shortened URL.
- **Responsive Design**: Clean and responsive UI powered by Flowbite components.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (with Flowbite for UI components)
- **Database**: SQLite (default, configurable to others like PostgreSQL or MySQL)
- **Charts**: ApexCharts for displaying URL activity

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/komronbek-tufliyev/shortlinker.git
    cd shortlinker
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the website**:
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Usage

### Creating a Shortened URL

1. Navigate to the homepage.
2. Enter a long URL in the provided form and submit.
3. The shortened URL will be displayed on the screen.

### Tracking URL Usage

1. Click on any shortened URL to be redirected to the original URL.
2. After a redirect, the view count for the shortened URL will update.
3. View detailed statistics and a chart of recent activity on the statistics page.

### Redirect URL View Example

Here is how a shortened URL redirect and logging feature is handled in the Django view:

```python
def redirect_url_view(request, shortened_part):
    shortener = get_object_or_404(UrlShortener, short_url=shortened_part)
    shortener.times_followed += 1
    shortener.save()
    
    # Log access for statistics
    today = timezone.now().date()
    access_log, created = AccessLog.objects.get_or_create(url_shortener=shortener, date=today)
    if not created:
        access_log.count += 1
        access_log.save()
    
    return HttpResponseRedirect(shortener.url)
```

## Endpoints

- **Homepage**: `/` - Create a shortened URL.
- **Redirect and Statistics**: `/<str:shortened_part>/` - Redirects to the original URL and updates statistics.Shows detailed access statistics and a chart.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

Happy shortening with **ShortLinker**!
```
