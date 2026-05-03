## Run everything using single command -->
# nohup bash -c 'source activate rasa && python manage.py runserver && rasa run actions && rasa run -m models --enable-api --cors "*"  --endpoints endpoints.yml'
# add & at the end to finally exit or without & to quit all process using ctrl+c as per user choice
# ext 0 - to kill the process
# fg - run process in fourground

source activate rasa
nohup python manage.py runserver &
echo "1: DJANGO SERVER running................."
source activate rasa
nohup rasa run actions &
echo "2: RASA ACTION SERVER running............"
source activate rasa
nohup rasa run -m models --enable-api --cors "*"  --endpoints endpoints.yml &
echo "3: RASA SERVER running..................."
tail -f nohup.out
# tail -f nohup.out &
# echo "ALL SERVERS ARE UP & RUNNING ..................................."
# ps

## Show Runing Porcess -->
# ps --help
# Usage: ps [-aefls] [-u UID] [-p PID]

## Kill Running Process -->
# kill PID

## to run this script --
## open git bash terminal
## bash rasa_script.sh