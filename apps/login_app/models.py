# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models #import models for...
import re #import regex for verification
import bcrypt

class UserManager(models.Manager):
    def regVal(self, PostData):
        results = {"status": True, 'errors': []}
        if len(PostData['first_name']) < 3 :
            results['errors'].append('First name must be 3 characters long.')
        if len(PostData['last_name']) < 3 :
            results['errors'].append('Last name must be 3 characters long.')
        if not re.match('\w+[.|\w]*@(\w+[.])*\w+', PostData['email']):
            results['errors'].append('Please enter a vaild email.')
        if len(PostData['password']) < 5 :
            results['errors'].append('Your password must be at least 5 characters long')
        if PostData['password'] != PostData['c_password']:
            results['errors'].append('Your passwords must match')
        if len(self.filter(email = PostData['email'])) > 0:
            results['errors'].append('User already exists')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

    def creator(self, PostData):
        hashed = bcrypt.hashpw(PostData['password'].encode(), bcrypt.gensalt())
        print hashed
        user = User.objects.create(first_name = PostData['first_name'], last_name = PostData['last_name'], email = PostData['email'], password = hashed)

    def logVal(self, PostData):
        results = {'status': True, 'errors': [], 'user': None}
        user = User.objects.filter(email= PostData['email'])
        if len(user) < 1:
            results['errors'].append('User not found.')
        else:
            if bcrypt.checkpw(PostData['password'].encode(), user[0].password.encode()) == False:
                results['errors'].append('Passwords do not match.')
            if len(results['errors']) > 0:
                results['status'] = False
            else:
                results['user'] = user[0]
        return results


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()
