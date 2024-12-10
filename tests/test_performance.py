import time
from playwright.sync_api import sync_playwright

# Test if the page takes longer than 5 seconds to load
def test_performance():
    # network types
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

        for speed in network_speed:
            context = browser.new_context()
            
            # set the network conditions
            context.network_conditions = speed

            page = context.new_page()

            # calculate the time to load the page
            time_start = time.time()
            page.goto("https://securitycheck-rc.redamp.eu/")
            time_end = time.time()

            time_final = time_end - time_start
            assert time_final <= 5.0
            
            context.close()

        browser.close()
