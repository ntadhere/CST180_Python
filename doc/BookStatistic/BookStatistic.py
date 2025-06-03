import csv

def BookStatistic(csv_filename, output_filename):
    """
    Reads a CSV file (Title,Author,Year,Pages), computes:
      1. Average publication year
      2. Average number of pages
      3. Book with the most pages
      4. Book with the fewest pages
    Prints the results to the console and writes them into output_filename.
    """

    total_years = 0
    total_pages = 0
    count = 0

    book_most = None   # Tuple: (title, author, year, pages)
    book_least = None  # Tuple: (title, author, year, pages)

    with open(csv_filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Expect exactly 4 columns per row
            if len(row) != 4:
                continue

            title = row[0].strip()
            author = row[1].strip()

            try:
                year = int(row[2].strip())
                pages = int(row[3].strip())
            except ValueError:
                # Skip rows where year or pages are not valid integers
                continue

            total_years += year
            total_pages += pages
            count += 1

            # Update “most pages” tracker
            if (book_most is None) or (pages > book_most[3]):
                book_most = (title, author, year, pages)

            # Update “fewest pages” tracker
            if (book_least is None) or (pages < book_least[3]):
                book_least = (title, author, year, pages)

    if count == 0:
        print("No valid book records found.")
        return

    avg_year = total_years / count
    avg_pages = total_pages / count

    # Prepare the lines of output
    lines = [
        f"Average Publication Year: {avg_year}",
        f"Average Number of Pages: {avg_pages}",
        f"Book with Most Pages: Title: {book_most[0]}, Author: {book_most[1]}, Year: {book_most[2]}, Pages: {book_most[3]}",
        f"Book with Least Pages: Title: {book_least[0]}, Author: {book_least[1]}, Year: {book_least[2]}, Pages: {book_least[3]}"
    ]

    # Print to terminal
    for line in lines:
        print(line)

    # Write the same lines into the output file
    with open(output_filename, "w", encoding="utf-8") as outfile:
        for line in lines:
            outfile.write(line + "\n")
