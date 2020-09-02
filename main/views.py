from django.shortcuts import render
from django.views.generic import TemplateView


class Main(TemplateView):
	template_name = "main.html"

	def get(self, response):
		return render(response, self.template_name)