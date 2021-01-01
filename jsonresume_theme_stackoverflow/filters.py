import datetime
import re

from .exceptions import ObjectIsNotADate


def format_date(value, format="%d %M %Y"):
    regex = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", value)
    if regex is not None:
        date = datetime.date(
            int(regex.group("year")),
            int(regex.group("month")),
            int(regex.group("day")))
    else:
        raise ObjectIsNotADate

    return date.strftime(format)
