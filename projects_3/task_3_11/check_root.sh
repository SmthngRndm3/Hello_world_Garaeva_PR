check_root() {

if [ $EUID -eq 0 ]; then
   echo "Ошибка"
fi
}

check_root 
