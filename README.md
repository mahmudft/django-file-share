# ***Django File Sharing***

- FIle permissions are applied with `django-guardian`
- File comments are written with `channels`
- The Files will be deleted after `7 days` with `celery`
- Static Files are serving with `WhiteNoise`

Run app with `daphne filesharing.asgi:application`
- Make sure redis is running