#!/bin/bash

read -p "Вес (кг) :" WEIGHT
read -p "Рост (м) :" HEIGHT

result=$(echo "scale=2; $WEIGHT/($HEIGHT**2)" | bc)

echo "Ваш ИМТ: $result"
