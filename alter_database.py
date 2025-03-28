from portfolio_projects.models import Project


def show_projects():
    print(Project.objects.all())


