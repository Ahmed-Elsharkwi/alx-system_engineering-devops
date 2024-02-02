dig google.de | awk -F ' ' 'NR>11 && NR<16 {print $5}'
