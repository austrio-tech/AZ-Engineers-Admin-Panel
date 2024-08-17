from my_pages.dashboard import show_dashboard


def OpenPage(page=show_dashboard, **kwargs):
    page(**kwargs)
