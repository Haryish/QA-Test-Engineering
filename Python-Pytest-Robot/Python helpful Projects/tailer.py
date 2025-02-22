import numpy as np

# Define reasonable ranges for uniform measurements based on class level
measurement_ranges = {
    "தோள் பட்டை": (24, 44),
    "உயரம்": (80, 140),
    "மார்பு சுற்றளவு": (50, 90),
    "கை நீளம்": (30, 60),
    "கை சுற்றளவு": (14, 30),
    "இடுப்பு சுற்றளவு": (50, 90),
    "கால் உயரம்": (50, 90),
    "தொடை சுற்றளவு": (30, 60)
}

# Function to generate even numbers within a range
def even_rand(lower, upper):
    return np.random.choice(np.arange(lower, upper+1, 2))

# Filter the student rows (starting after the headers)
data_start_row = 4  # Based on observed structure
student_data = df.iloc[data_start_row:].reset_index(drop=True)

# Extract class and section columns
class_column = student_data.columns[3]  # "Class"
section_column = student_data.columns[4]  # "Section"

# Generate values for each measurement
for col, (low, high) in measurement_ranges.items():
    student_data[col] = [even_rand(low, high) for _ in range(len(student_data))]

# Keep only relevant columns
final_df = student_data[[class_column, section_column] + list(measurement_ranges.keys())]

# Show the first few rows of the cleaned dataset
final_df.head()
