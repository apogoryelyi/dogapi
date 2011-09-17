from v1 import *

class SimpleClient(object):

    def __init__(self):
        self.api_key = None
        self.application_key = None
        self.datadog_host = 'https://app.datadoghq.com'

    def metric(self, name, value):
        pass

    #
    # Comment API

    def comment(self, handle, message, comment_id=None, related_event_id=None):
        if self.api_key is None or self.application_key is None:
            raise Exception("Comment API requires api and application keys")
        s = CommentService(self.api_key, self.application_key, self.datadog_host)
        if comment_id is None:
            return s.post(handle, message, related_event_id)
        else:
            return s.edit(comment_id, handle, message, related_event_id)

    def delete_comment(self, comment_id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Comment API requires api and application keys")
        s = CommentService(self.api_key, self.application_key, self.datadog_host)
        return s.delete(comment_id)

    #
    # Cluster API

    def all_clusters(self):
        if self.api_key is None or self.application_key is None:
            raise Exception("Cluster API requires api and application keys")
        s = ClusterService(self.api_key, self.application_key, self.datadog_host)
        return s.get_all()

    def host_clusters(self, host_id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Cluster API requires api and application keys")
        s = ClusterService(self.api_key, self.application_key, self.datadog_host)
        return s.get(host_id)

    def add_clusters(self, host_id, *args):
        if self.api_key is None or self.application_key is None:
            raise Exception("Cluster API requires api and application keys")
        s = ClusterService(self.api_key, self.application_key, self.datadog_host)
        return s.add(host_id, args)
    
    def change_clusters(self, host_id, *args):
        if self.api_key is None or self.application_key is None:
            raise Exception("Cluster API requires api and application keys")
        s = ClusterService(self.api_key, self.application_key, self.datadog_host)
        return s.update(host_id, args)
    
    def detatch_clusters(self, host_id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Cluster API requires api and application keys")
        s = ClusterService(self.api_key, self.application_key, self.datadog_host)
        return s.detatch(host_id)

    #
    # Stream API

    def stream(self, start, end, priority=None, sources=None, tags=None):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = EventService(self.api_key, self.application_key, self.datadog_host)
        return s.query(start, end, priority, sources, tags)

    def get_event(self, id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = EventService(self.api_key, self.application_key, self.datadog_host)
        return s.get(id)

    def event(self, title, text, date_happened=None, handle=None, priority=None, related_event_id=None, tags=None):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = EventService(self.api_key, self.application_key, self.datadog_host)
        return s.post(title, text, date_happened, handle, priority, related_event_id, tags)

    #
    # Dash API

    def dashboards(self):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = DashService(self.api_key, self.application_key, self.datadog_host)
        return s.get_all()

    def dashboard(self, dash_id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = DashService(self.api_key, self.application_key, self.datadog_host)
        return s.get(dash_id)

    def create_dashboard(self, title, description, graphs):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = DashService(self.api_key, self.application_key, self.datadog_host)
        return s.create(title, description, graphs)

    def update_dashboard(self, dash_id, title, description, graphs):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = DashService(self.api_key, self.application_key, self.datadog_host)
        return s.update(dash_id, title, description, graphs)

    def delete_dashboard(self, dash_id):
        if self.api_key is None or self.application_key is None:
            raise Exception("Event API requires api and application keys")
        s = DashService(self.api_key, self.application_key, self.datadog_host)
        return s.delete(dash_id)
