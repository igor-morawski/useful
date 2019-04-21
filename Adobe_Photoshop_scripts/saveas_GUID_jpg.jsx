/************************************************************************
Save an image as an unique [GUID].jpg in the script's parent directory
 ***********************************************************************/

var save_path = File($.fileName).parent + "/";

//jpg options
jpgSaveOptions = new JPEGSaveOptions();
jpgSaveOptions.embedColorProfile = true;
jpgSaveOptions.formatOptions = FormatOptions.STANDARDBASELINE;
jpgSaveOptions.matte = MatteType.NONE;
jpgSaveOptions.quality = 12;
var myfname = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
})
jpgFile = new File(save_path + myfname + ".jpg");
app.activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);
