# url = 'https://www.example.com:8080/path/to/page/?name=John&age=30#section'


# from urllib.parse import urlparse

# print(urlparse(url).scheme)

import mlflow

mlflow.start_run()
mlflow.log_param('test','value')
mlflow.end_run()