country_names = ["India", "United States", "United Kingdom", "Canada", "Australia","spain","singapore"]
country_lengths = [len(country) for country in country_names]
country_dict = dict(zip(country_names, country_lengths))
sorted_dict = dict(sorted(country_dict.items(), key=lambda item: item[1])) 
print(sorted_dict)