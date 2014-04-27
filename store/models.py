# -*- coding: UTF-8 -*-
from django.db import models
import os
import datetime

def get_icon_path(instance, filename):
	fname, ext = os.path.splitext(filename)	
	return 'icon/%s%s'%(datetime.datetime.now().strftime('%Y%m%d%H%m%s'), ext.lower())

class size(models.Model):
	s_title = models.CharField(verbose_name="名称", max_length=50)
	s_define = models.CharField(verbose_name="图标大小", max_length=50)
	s_icon = models.CharField(verbose_name="图标位置", max_length=50)
	class Meta:
		verbose_name = "图标大小定义"
		verbose_name_plural = "图标大小定义"
	def __unicode__(self):
		return self.s_title

class appspic(models.Model):
	s = models.ForeignKey(size, verbose_name="图标大小")
	p_title = models.CharField(verbose_name="图标名称", max_length=50)
	p_pic = models.FileField(verbose_name="图标图片", upload_to=get_icon_path)
	p_color = models.CharField(verbose_name="图标颜色", max_length=50)
	class Meta:
		verbose_name = "图标"
		verbose_name_plural = "图标列表"
	def __unicode__(self):
		return self.p_title
	
class appClass(models.Model):
	p = models.ForeignKey(appspic, verbose_name="图标列表")
	c_title = models.CharField(verbose_name="分类名称", max_length=50)
	c_path = models.CharField(verbose_name="分类路径", max_length=20)
	c_sort = models.IntegerField(verbose_name="分类排序", default=0)
	class Meta:
		verbose_name = "分类"
		verbose_name_plural = "分类列表"
	def __unicode__(self):
		return self.c_title

class apps(models.Model):
	c = models.ForeignKey(appClass, verbose_name="所属分类")
	p = models.ForeignKey(appspic, verbose_name="图标列表")
	a_title = models.CharField(verbose_name="应用名称", max_length=50)
	a_app = models.FileField(verbose_name="应用程序", upload_to="file/")
	a_sort = models.IntegerField(verbose_name="应用排序", default=0)
	class Meta:
		verbose_name = "应用"
		verbose_name_plural = "应用列表"
	def __unicode__(self):
		return self.a_title
