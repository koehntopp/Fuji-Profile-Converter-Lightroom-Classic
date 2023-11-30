Fujifilm Profile Generator for Lightroom (Classic)

I stumbled upon https://foto-jan-lorenz.de/2019/07/fujifilm-profile-fuer-alle/ which is based on PowerShell.

The project does not seem to be actively maintained, and I wanted to create profile for newer cameras.

Original Github repository https://github.com/lichtzeichner/FujifilmCameraProfiles

I ported the code to Python on repl.it ( https://replit.com/@koehntopp/Fuji-Profile-Converter-Lightroom-Classic ) and have been creating profiles successfully since.

Here's how it works:

- find the <CAMERA_NAME> Adobe Standard.lcp file on your computer
- download https://helpx.adobe.com/de/camera-raw/digital-negative.html#Adobe_Lens_Profile_Creator
- convert the lcp to xml
- put the xml file into the AdobeStandardXML folder
- set the 'camera' variable in main.py to <CAMERA_NAME>
- run main.py
- convert the xml files in Output to lcp and import them into Lightroom
- done.