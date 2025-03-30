import os

from sherlock_project.notify import QueryNotifyPrint
from sherlock_project.sherlock import sherlock
from sherlock_project.sites import SitesInformation


def social_media_lookup_by_username(username: str) -> None:
    query_notify = QueryNotifyPrint()
    site_data = SitesInformation(os.path.join(os.path.dirname(__file__), "resources/data.json"))
    site_data_all = {site.name: site.information for site in site_data}
    print(sherlock(username, site_data_all, query_notify))
