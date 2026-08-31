# pip install aqora  ·  aqora login
from aqora import ProviderJob

job = ProviderJob.from_id("AFByb3ZpZGVySm9iAaBW7Kn6fBCbkGI3kYQyJQ")
print(job.status())
result = job.results()

print(result)