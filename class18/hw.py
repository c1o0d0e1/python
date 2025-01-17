from datetime import datetime, timedelta

now = datetime.now()
delta = timedelta(days=5)
future_date = now + delta
print(future_date)  # 例如：2025-01-15
