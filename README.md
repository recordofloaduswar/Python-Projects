# Python-Projects
Scripts and small projects of the Python variety.

## Lockbox Transfer
This script is used to organize file images received from a bank lockbox. The bank sends a folder with TIFF images and an index file. The index file indicates which images are part of the same transaction. In this case, each transaction contains an image of a check and any accompanying documents (i.e. appeals, notes, check stubs). After running the Python script in the same folder as the images and index file, in summary, the script does the following:
- Creates a timestamped folder
- Reads the index file
- Concatenates the respective images together into one TIFF file
- Names the file according to check number and check amount
- Saves the file into the timestamped folder
- Repeats the process until it is done with the index file
