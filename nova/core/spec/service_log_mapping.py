from collections import OrderedDict


class ServiceLogMapping(object):

    def __init__(self, log_file, group_name, datetime_format):
        self.log_file = log_file
        self.group_name = group_name
        self.datetime_format = datetime_format

    def yaml(self):
        data = OrderedDict([
            ('file', self.log_file),
            ('group_name', self.group_name),
            ('datetime_format', self.datetime_format)
        ])
        return OrderedDict((k,v) for k,v in data.iteritems() if v is not None)

    @staticmethod
    def load(values):
        return ServiceLogMapping(
            values.get("file"),
            values.get("group_name"),
            values.get("datetime_format")
        )
