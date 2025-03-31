from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()


duration = dt2 - dt1
print(duration)  # Difference e.g. 2646 days, 18:52:12.676607
print("days", duration.days)  # e.g. days 2646
print("seconds", duration.seconds)  # e.g. 67932
# e.g. total_seconds 228682428.076626
print("total_seconds", duration.total_seconds())
