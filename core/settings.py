import dj_database_url
INSTALLED_APPS = [
    'rest_framework',
    'api.apps.ApiConfig',
]
DATABASES = {
    'default': dj_database_url.parse('postgres://sxuszgkmgftinq:26e93186ad793b64a6ddb430f507d032f6d564b99412001a6c02d7a82268ffe0@ec2-44-199-52-133.compute-1.amazonaws.com:5432/ddkgsilnuogmu2')
}