#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, unique=True)

class LinkEnum(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()

class ParentLink(models.Model):
    p1 = models.ForeignKey(Parent, related_name='links1')
    p2 = models.ForeignKey(Parent, related_name='links2')
    quality = models.ForeignKey(LinkEnum)

class Application(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    homonyms = models.ManyToManyField('self', null=True, blank=True)

class Host(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    ip = models.IPAddressField(null=True, blank=True)
    is_suffix = models.BooleanField(default=False)

class Calendar(models.Model):
    sun = models.CharField(max_length=24, default='0'*24)
    mon = models.CharField(max_length=24, default='0'*24)
    tue = models.CharField(max_length=24, default='0'*24)
    wes = models.CharField(max_length=24, default='0'*24)
    thu = models.CharField(max_length=24, default='0'*24)
    fri = models.CharField(max_length=24, default='0'*24)
    sat = models.CharField(max_length=24, default='0'*24)

class Authorization(models.Model):
    applications = models.ManyToManyField(Application, null=True, blank=True)
    hosts = models.ManyToManyField(Host, null=True, blank=True)
    calendar = models.ForeignKey(Calendar, null=True, blank=True)
    max_week = models.IntegerField(null=True, blank=True)
    max_day = models.IntegerField(null=True, blank=True)


class ChildProfile(models.Model):
    base = models.ForeignKey('self', null=True, blank=True)
    owner = models.ForeignKey(Parent)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    authorizations = models.ManyToManyField(Authorization, null=True, blank=True)


class Child(models.Model):
    user = models.OneToOneField(User, unique=True)
    parents = models.ManyToManyField(Parent)
    profiles = models.ManyToManyField(ChildProfile, null=True, blank=True, related_name='childs')
    active_profile = models.ForeignKey(ChildProfile, null=True, blank=True, related_name='active_childs')
    green_profile = models.ForeignKey(ChildProfile, related_name='green_childs', null=True, blank=True)
    orange_profile = models.ForeignKey(ChildProfile, related_name='orange_childs', null=True, blank=True)
    red_profile = models.ForeignKey(ChildProfile, related_name='red_childs', null=True, blank=True)
