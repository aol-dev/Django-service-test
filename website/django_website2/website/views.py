from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "伊藤"
        return ctxt

class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"] = 2
        ctxt["service_names"] = [
            "aol(自己学習)",
            "ioasis(会社)",
        ]
        ctxt["skills"] = [
            "Python",
            "java",
        ]
        return ctxt