#Models, modelagem dos arquivos que vao entrar no banco

from django.db import models

class CreateUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, db_index=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    date_birth = models.DateField(null=False)