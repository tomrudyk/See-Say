import os
import subprocess


hebrew_lines = """
שלום עולם
הכדור הוא עגול
זהו יום יפה ללמוד משהו חדש
נא להמתין רגע
לילה טוב לכולם
שרה שרה שיר שמח
שיר שמח שרה שרה
אל על הכי בבית בעולם
לטוס אל על עם החברה הכי טובה בעולם אל על
"""

No_Nikud_Path = "No_Nikud.txt"

with open(No_Nikud_Path, "w", encoding="utf-8") as f:
    f.write(hebrew_lines)

print("input.txt created with the following content:")
print(hebrew_lines)
print("")

# Save the current directory
original_dir = os.getcwd()

# Change to D_Nikud directory
dn_path = os.path.join(original_dir, "D_Nikud")
os.chdir(dn_path)

# Run main.py with arguments
subprocess.run(["python", "main.py", "predict", "../No_Nikud.txt", "../output.txt"])

# Go back to original directory
os.chdir(original_dir)

print("main.py has completed. Check 'output.txt' for the result.")