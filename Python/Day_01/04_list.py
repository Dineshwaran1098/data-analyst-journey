data_points = [10, 20, 30, 40, 50, 60]

# 1. Accessing via positive/negative pointers
print(data_points[0])   # Output: 10
print(data_points[-1])  # Output: 60 (Tail element tracking)

# 2. Slicing formula rules matrix: [start:stop:step]
print(data_points[1:4]) # Output: [20, 30, 40] (Stop bounds exclusive!)
print(data_points[::-1]) # Output: [60, 50, 40, 30, 20, 10] (Complete array flip!)

# Un python file-la open panni type panni run pannu bro:
my_analysis_tools = ["Python", "SQL", "PowerBI", "Excel"]
mixed_payload = [2026, "Data Analyst", 94.5, True]

print(type(my_analysis_tools)) # Output: <class 'list'>
print(mixed_payload)

# Let's verify the live difference:
languages = ["Python", "SQL"]

# 1. append single token check
languages.append("R")
print(languages) # Output: ['Python', 'SQL', 'R']

# 2. extend multi-elements array check
languages.extend(["BI", "Spark"])
print(languages) # Output: ['Python', 'SQL', 'R', 'BI', 'Spark']

# 3. insert target index injection
languages.insert(1, "Tableau") # 1st position injection
print(languages) # Output: ['Python', 'Tableau', 'SQL', 'R', 'BI', 'Spark']


metrics = [45, 99, 12, 78, 56]

# Ascending sort ordering override update
metrics.sort()
print(f"Ascending: {metrics}") # Output: [12, 45, 56, 78, 99]

# Descending parameters alignment config
metrics.sort(reverse=True)
print(f"Descending: {metrics}") # Output: [99, 78, 56, 45, 12]

# Occurrence count analytics tracking properties metrics check
log_signals = ["ERR", "INFO", "ERR", "WARN"]
print(log_signals.count("ERR")) # Output: 2

analytics_stack = ["Python", "SQL", "Excel", "SAS", "Excel"]

# 1. remove values clean tracking check
analytics_stack.remove("Excel") # First duplicate entry remove aairum
print(analytics_stack) # Output: ['Python', 'SQL', 'SAS', 'Excel']

# 2. pop index extraction check
popped_item = analytics_stack.pop(2) # SAS index 2 arrays elements remove validation return execution
print(f"Removed: {popped_item}") # Removed: SAS
print(analytics_stack) # Output: ['Python', 'SQL', 'Excel']
del analytics_stack[1]
print(analytics_stack)