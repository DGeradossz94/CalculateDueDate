from datetime import timedelta
from math import floor


def calculate_due_date(submit_datetime, turnaround_time):
    if submit_datetime.hour >= 17 or submit_datetime.hour < 9:
        raise ValueError("The submit_datetime hour value must be between 9 and 17!")
    if submit_datetime.weekday() == 5 or submit_datetime.weekday() == 6:
        raise ValueError("The submit_datetime must be workday!")
    remaining_work_hours = turnaround_time % 8  # the remaining work hours after full workdays
    work_days = round((turnaround_time - remaining_work_hours) / 8)
    weeks = floor(work_days / 7)
    weekend_days = weeks * 2
    final_date = submit_datetime + timedelta(days=work_days+weekend_days) + timedelta(hours=remaining_work_hours)
    if weekend_days == 0 and (final_date.weekday() < submit_datetime.weekday() or final_date.weekday() in [5, 6]):
        final_date = final_date + timedelta(days=2)
    if final_date.hour >= 17:
        plus_hours = 16
        final_date = final_date + timedelta(hours=plus_hours)
    plus_days = 0
    if final_date.weekday() == 5:
        plus_days = 2
    elif final_date.weekday() == 6:
        plus_days = 1
    final_date = final_date + timedelta(days=plus_days)
    return final_date

