import random
secret="".join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
print("export SECRET_KEY='{0}'".format(secret))
print("export DJANGO_SUPERUSER_PASSWORD='{0}'".format("adminadmin"))
print("export DJANGO_SUPERUSER_EMAIL='{0}'".format("n.mazacerda@uandresbello.edu"))
print("export DJANGO_SUPERUSER_USERNAME='{0}'".format("admin"))
