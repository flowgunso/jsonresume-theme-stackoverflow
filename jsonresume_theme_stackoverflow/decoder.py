from pprint import pprint
import json
import re
import datetime

class JSONResumeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        for key, item in obj.items():
            if isinstance(item, dict):
                obj = self.object_hook(item)
            elif isinstance(item, str):
              regex = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}})", item)
              if regex is not None:
                  obj[key] = datetime.date(regex.group("year"), regex.group("month"), regex.group("day"))
            else:
                print(f"\033[1mkey:\033[0m {key}\n\033[1mtype:\033[0m {str(type(item))}\n\033[1mitem:\033[0m {item}\n")
        return obj
