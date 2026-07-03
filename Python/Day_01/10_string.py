sample_text = "PYTHON"

# Positive Indexing
print(sample_text[0])   # Output: P
print(sample_text[2])   # Output: T

# Negative Indexing (Kadaisila irundhu reverse tracking)
print(sample_text[-1])  # Output: N (Last letter)
print(sample_text[-4])  # Output: T55

data_stream = "DATA_SCIENCE"

# 1. Basic Slice (0ல irundhu 4th index-ku munnadi varai)
print(data_stream[0:4])   # Output: DATA

# 2. Default Shortcuts (Start skip panna 0, Stop skip panna end varai)
print(data_stream[:4])    # Output: DATA (0 automatic-ah eduthukum)
print(data_stream[5:])    # Output: SCIENCE (5th indexல irundhu end varai)

# 3. Negative Slicing
print(data_stream[-7:])   # Output: SCIENCE

# Ovvoru 2 leters jump panni print pannu:
print(data_stream[0:12:2])  # Output: DT_CEN

# 🤯 Interview Ultimate Hack: Reversing a String
# Step-la '-1' pota Python right-to-left reverse jumps perform pannum:
print(data_stream[::-1])    # Output: ECNEICS_ATAD (String reversed instantly!)

# Scenario: Raw database text filled with messy spaces
dirty_input = "   Data Analyst Role   "

# 1. strip() -> Left & Right side unnecessary spaces clean pannidum
clean_input = dirty_input.strip()
print(f"'{clean_input}'") # Output: 'Data Analyst Role'

# 2. split() -> Data items breaking pattern
log_entry = "2026-07-03,ERROR,Database_Timeout"
parsed_list = log_entry.split(",") 
print(parsed_list) # Output: ['2026-07-03', 'ERROR', 'Database_Timeout']
# (Data streams comma analytics filters split panna idhu semma tool!)

# 3. replace() -> Data anomalies cleaning
dirty_phone = "9876-543-210"
clean_phone = dirty_phone.replace("-", "")
print(clean_phone) # Output: 9876543210


raw_transaction = "TXN_ID:992834_STATUS:SUCCESS"
transaction_id = raw_transaction[7:13]
print(transaction_id)