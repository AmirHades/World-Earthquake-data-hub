# World-Earthquake-data-hub
Question: Why is the fetching script pulling out monthly data instead of yearly?
Answer: There are two reasons for it:
* The USGS archive would not return more than 20,000 results per query.
* Fetching on a monthly basis bypasses the need to write pagination logic in the fetching script.
