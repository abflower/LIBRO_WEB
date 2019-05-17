### What is Libro ###

Libro is a desktop utility for the creation and consultation of a library catalogue. 
It is written in Python and use a SQLite database. The GUI is written using the Tkinter module.

For the existing release ses: https://alessandrobellafiore.com/projects/libro-1-0/.

Some key features of the existing release are:
- ability to add entries to the catalogue
- ability to perform searches based on any of the fields identifing a publication
- native support for Dewey decimal, with some automation like the creation of triliteral code for each author
- available as an installable file for Win OS.

Some features written but not released:
- ability to retrieve details of a publication simply giving the ISBN code (based on ISBNdb, https://isbndb.com/).

Some limitations of the existing release:
- inability to modify/delete existing entries in the catalogue
- lack of support for publications with more than one author
- lack of mechanism for catalogue import/export
- only runs locally
- GUI functional although a bit dull.


### What's next? ###

The is large room for improvement in this project and there is little good software available for the private
book collector or the small library.

Ideas for development are:
- Libro running as a web app, or to be run locally on a server.
- Use of Flask to provide a better user experience and more a pleasant GUI

Features to be added (some of the mentioned above as current limitation):
- ability to modify/delete existing entries in the catalogue
- add support for publications with more than one author
- add support for catalogue import/export

Features needed for the use as web application:
- credential based access
- multi-user access
- creation of users with specific privileges

Features which could be useful:
- ability to read/generate barcodes/QR code labels


### Looking ahead (very much ahead) ###

Should the project grow and become interesting for small-medium libraries, some features might be added, like:
- creation/management of end users
- distinction between admin and end users
- support for loans


This are just some first thoughts.
Anyone who would like to give some contribution or suggestions is more than welcome.
Thanks!!!

