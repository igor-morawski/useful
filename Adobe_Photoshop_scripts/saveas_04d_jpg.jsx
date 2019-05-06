/************************************************************************
Adobe Photoshop Script: Save an image in %04d.jpg in the 
script's parent directory
If %04d.jpg exist script continues the existing numeration.
 ***********************************************************************/


var save_path = File($.fileName).parent + "/";

var reg = new RegExp('[0-9][0-9][0-9][0-9]\\.jpg')

var filecounter = -1;

var tmp;
var tmp0;

var f = Folder(save_path);
var allFiles = f.getFiles();
for (var i = 0; i < allFiles.length; i++) {
    tmp = allFiles[i];
    tmp = decodeURI(tmp.name)
    if (tmp.match(reg)) {
        tmp0 = parseInt(tmp, 10)
        if (tmp0 > filecounter) {
            filecounter = tmp0
        }
    }
}

filecounter += 1

/************************************************************************
foreach(glob(save_path + "[0-9][0-9][0-9][0-9].jpg") as $filename) {
    $p = pathinfo($filename);
}
alert($p)
 ***********************************************************************/
//jpg options
jpgSaveOptions = new JPEGSaveOptions();
jpgSaveOptions.embedColorProfile = true;
jpgSaveOptions.formatOptions = FormatOptions.STANDARDBASELINE;
jpgSaveOptions.matte = MatteType.NONE;
jpgSaveOptions.quality = 12;
filecounter.toString()
var myfname = filecounter.toString()
while (myfname.length < 4) myfname = '0' + myfname;
jpgFile = new File(save_path + myfname + ".jpg");
app.activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);
