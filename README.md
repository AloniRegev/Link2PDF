# Link2PDF
Automation to convert URL file from source directory to PDF file to target directory.

## Installations:
1. [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) execution file.
2. pdfkit - `pip install pdfkit`
3. watchdog - `pip install watchdog`
4. shutil - `pip install shutil`
5. pywintypes - `pip install pywin32`
6. win10toast - `pip instal win10toast`

## Run me:
### Befor your first run - find the `wkhtmltopdf.exe` path :
1. Install the `wkhtmltopdf` execution file.
2. Navigate to the `wkhtmltopdf.exe` file directory were wkhtmltopdf is installd, it shuld be somting like `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`, or wherever you install `wkhtmltopdf`.


### To run the code you need to pass the arguments in the order mentiond below:
1. Path of source directory.
2. Path of target directory.
3. Path of `wkhtmltopdf.exe` file, for defalt path `"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"`.  
