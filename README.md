# Link2PDF
Automation to convert URL file from source directory to PDF file to target directory.

## Installations:
1. [wkhtmltopdf](https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe) execution file.
2. pdfkit - `pip install pdfkit`
3. watchdog - `pip install watchdog`
4. shutil - `pip install shutil`

## Befor your first run:
1. Set the `wkhtmltopdf.exe` path 
    1. Install the `wkhtmltopdf` execution file.
    2. Navigate to the directory were wkhtmltopdf is installd, go to `bin` folder and copy the path ot the `wkhtmltopdf.exe` file.
    3. past the path in the `<path of wkhtmltopdf 'bin' directory\wkhtmltopdf.exe>` section in the code.
2. Enter the path of the source folder where the url files are located in `<path of source directory>`.
3. Enter the path of the target folder where the url files are located in `<path of target directory>`.

## Run me:
to run the code you need to pass the arguments in the order mentiond below:
1. Path of source directory.
2. Path of target directory.
3. Path of `wkhtmltopdf.exe` file.  
