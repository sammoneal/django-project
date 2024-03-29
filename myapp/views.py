from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .default_data import load_default_data
from .models import Invention, Category
from .forms import InventionForm


# class from which all class based views inherit
class BaseView(TemplateView):
    default_title = "My Website"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", self.default_title)
        return context


class HomeView(BaseView):
    template_name = "bootswatch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Project Home",
                "page_heading": "Django Project Home",
                "page_content": "Welcome to my Django Project.",
            }
        )
        return context


class ClassView(BaseView):
    template_name = "bootswatch.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Class-Based View",
                "page_heading": "Welcome to the Class-Based View",
                "page_content": "This is the content generated by the class-based view.",
            }
        )
        return context


class ThemeView(BaseView):
    template_name = "theme.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data if needed
        return context

    def post(self, request, *args, **kwargs):
        theme = request.POST.get("theme")
        response = HttpResponseRedirect(reverse("theme"))
        response.set_cookie("theme", theme)
        return response


class InventionListView(ListView):
    model = Invention
    template_name = "invention_list.html"
    context_object_name = "inventions"


class InventionDetailView(DetailView):
    model = Invention
    template_name = "invention_view.html"
    context_object_name = "invention"


class InventionCreateView(LoginRequiredMixin, CreateView):
    model = Invention
    form_class = InventionForm
    template_name = "create_invention.html"
    success_url = reverse_lazy("invention-list")


class InventionUpdateView(LoginRequiredMixin, UpdateView):
    model = Invention
    form_class = InventionForm
    template_name = "update_invention.html"
    success_url = reverse_lazy("invention-list")


class InventionDeleteView(LoginRequiredMixin, DeleteView):
    model = Invention
    success_url = reverse_lazy("invention-list")


def about(request):
    context = {
        "page_title": "About Page",
        "page_heading": "About my Project",
        "page_content": "This is my project for learning Django.",
    }
    return render(request, "bootswatch.html", context)


def function_view(request):
    context = {
        "page_title": "Function-Based View",
        "page_heading": "Welcome to the Function-Based View",
        "page_content": "This is the content generated by the function-based view.",
    }
    return render(request, "bootswatch.html", context)


def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({"status": "success"})
