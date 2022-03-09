import requests

class SurflineGetter(object):
    def __init__(self):
        self.base_url = "https://services.surfline.com/kbyg/spots/forecasts/{}?spotId={}"


    def get_surfline_forecast(self, spot_id=None, product_type='wave'):
        url = self.base_url.format(product_type, spot_id)

        res = requests.get(url)
        return res.content


