import time
from playwright.sync_api import sync_playwright

# Test load speed of the form site
def test_performance():
    network_speed = [
        ('3G', {
            'download_rate': 750 * 1024 / 8,
            'upload_rate': 250 * 1024 / 8,
            'latency': 100
        }),
        ('5G', {
            'download_rate': 30 * 1024 * 1024 / 8,
            'upload_rate': 15 * 1024 * 1024 / 8,
            'latency': 2
        })
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        for net_t, speed in network_speed:
            context = browser.new_context()

            context.route("**/*", lambda route: route.continue_())
            context.network_conditions = speed

            page = context.new_page()

            time_start = time.time()
            page.goto("https://securitycheck-rc.redamp.eu/")
            time_end = time.time()

            time_final = time_end - time_start
            print(f"Time to load page in {net_t} is {time_final:.2f} seconds")
            
            context.close()

        browser.close()
