for f in *.MTS; do
    filename=$(basename "$f")
    ext="${filename##*.}"
    basenm="${filename%.*}"
    mv "$f" "${basenm}_$(stat -f "%Sm" -t "%Y%m%d_%H%M%S" "$f").${ext}"
done
