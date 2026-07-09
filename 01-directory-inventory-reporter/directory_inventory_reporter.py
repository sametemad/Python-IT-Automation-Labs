import csv
import io


files = [
    {"filename": "resume.pdf", "size_kb": 245, "modified": "2026-07-09 10:30"},
    {"filename": "notes.txt", "size_kb": 12, "modified": "2026-07-09 11:05"},
    {"filename": "domains.xlsx", "size_kb": 880, "modified": "2026-07-08 16:20"},
    {"filename": "script.py", "size_kb": 6, "modified": "2026-07-09 14:30"}
]


def generate_file_report(files):
    total_size = 0
    largest_file = None

    csv_output = io.StringIO()
    writer = csv.writer(csv_output)

    writer.writerow([
        "Filename",
        "Extension",
        "Size_KB",
        "Last_Modified",
        "Category"
    ])

    for file in files:
        name = file["filename"]
        extension = name.split(".")[-1]
        size = file["size_kb"]
        modified = file["modified"]

        if extension == "pdf":
            category = "Document"
        elif extension == "txt":
            category = "Text"
        elif extension == "xlsx":
            category = "Spreadsheet"
        elif extension == "py":
            category = "Python Script"
        else:
            category = "Other"

        writer.writerow([
            name,
            extension,
            size,
            modified,
            category
        ])

        total_size += size

        if largest_file is None or size > largest_file["size_kb"]:
            largest_file = file

    print("--- CSV Output ---")
    print(csv_output.getvalue())

    print("--- Summary ---")
    print(f"Total Files: {len(files)}")
    print(f"Total Size: {total_size} KB")
    print(f"Largest File: {largest_file['filename']}")
    print(f"Largest File Size: {largest_file['size_kb']} KB")
