for f in *.TIF; do
    basenm="${f%.TIF}"
    sips -s format JPEG -s formatOptions best $f --out "$basenm.JPG"
    exiftool  -ImageDescription=  -Description=  "$basenm.JPG"
    jhead -di -ft "$basenm.JPG"
    rm "$basenm.JPG_original"
done
