#!/bin/bash

"Имя гена:" NAME
"Уровень экспрессии гена:" EXPRESSION

if [ $# -lt 2 ]; then
echo "Недостаток входящих данны"
else
echo "Экспрессия гена $NAME составляет $EXPRESSION единиц"
fi
