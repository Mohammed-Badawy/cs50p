# Prompt for file name
fname = input("File name: ").strip().lower()

# Check file extensions using conditionals
if fname.endswith(".gif"):  # gif file
    print("image/gif")
elif fname.endswith(".jpg") or fname.endswith(".jpeg"):  # jpeg or jpg file
    print("image/jpeg")
elif fname.endswith(".png"):  # png file
    print("image/png")
elif fname.endswith(".pdf"):  # pdf file
    print("application/pdf")
elif fname.endswith(".txt"):  # text file
    print("text/plain")
elif fname.endswith(".zip"):  # zip archive file
    print("application/zip")
else:  # Other types
    print("application/octet-stream")