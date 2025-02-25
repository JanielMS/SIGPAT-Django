from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name  = 'home.html'

class IsDeveloperOrAdminMixin(UserPassesTestMixin):
    """
    Permite acesso apenas para desenvolvedores e admins.
    """
    def test_func(self):
        return self.request.user.groups.filter(name__in=["Admin", "Desenvolvedor"]).exists() or self.request.user.is_superuser

class DocumentationView(LoginRequiredMixin, IsDeveloperOrAdminMixin, TemplateView):
    """
    View para exibir a documentação dentro do Django.
    """
    template_name = "docs/documentation.html"


def custom_403(request, exception):
    """
    View para exibir a página de acesso negado (403).
    """
    return render(request, "core/403.html", status=403)
