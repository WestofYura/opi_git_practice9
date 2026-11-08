#!/bin/bash
# Перевірка поведінки Prakt9.py на трьох наборах вхідних даних.
#   bash behavior_check/check.sh before  - зберегти результати ДО рефакторингу
#   bash behavior_check/check.sh after   - порівняти поточні результати з ДО
cd "$(dirname "$0")/.." || exit 1
PY=$(command -v python || command -v python3 || command -v py)
export PYTHONUTF8=1
for i in 1 2 3; do
  if [ "$1" = "before" ]; then
    $PY Prakt9.py < behavior_check/in$i.txt > behavior_check/before$i.txt
    echo "Тест $i: результат ДО збережено"
  else
    if $PY Prakt9.py < behavior_check/in$i.txt | diff -q - behavior_check/before$i.txt > /dev/null; then
      echo "Тест $i: результат збігається з ДО"
    else
      echo "Тест $i: РЕЗУЛЬТАТ НЕ ЗБІГАЄТЬСЯ"
    fi
  fi
done
