for f in *.jpg; do
    filename=$(basename "$f")
    mv "$f" "tn_${filename}"
done
