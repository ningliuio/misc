for f in *.MOV; do
    filename=$(basename "$f")
    ext="${filename##*.}"
    basenm="${filename%.*}"
    mv "$f" "${basenm}_$(stat -f "%Sm" -t "%Y%m%d_%H%M%S" "$f").${ext}"
done
