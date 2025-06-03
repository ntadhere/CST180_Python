from BookStatistic import BookStatistic

def Main():
    # Prompt the user for the CSV‐formatted book file
    csv_filename = input("Enter the input CSV filename: ").strip()

    # We’ll write the report into “book_report.txt” by default
    output_filename = "book_report.txt"

    # Call the BookStatistic function
    BookStatistic(csv_filename, output_filename)

    print(f"\nReport written to '{output_filename}'")


Main()
