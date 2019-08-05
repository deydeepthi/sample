from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChromoForm
from django.views import View

#FBV
def chromosomePage(request):
	form = ChromoForm()
	return render(request, "index.html", {"chromoForm": form})

def postChromo(request):
	if request.method == "POST" and request.is_ajax():
		form = ChromoForm(request.POST)
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

class ChromoAjax(View):
	form_class = ChromoForm
	template_name = "index.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"chromoForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)