for i in {1..20}; do

if [ i -eq 15 ]; then
    break

elif [[ $((i%2)) -eq 0 || $i -gt 15 ]]; then
    continue
fi
echo "$i"
 
done
