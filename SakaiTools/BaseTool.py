#!/usr/bin/python
# -*- coding: utf-8 -*-
import RequestGenerator


class BaseTool(object):

	def __init__(self,rq):
		self.requestor=rq