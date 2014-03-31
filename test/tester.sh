#!/bin/bash

PROJDIR=$(dirname $PWD)
TESTDIR="$PWD"
export PYTHONPATH=$PROJDIR

PYTIMER="$PWD/timer.py"
PNUM="$1"
USRN="$2"

cd ../src/solutions/$PNUM
echo 'Starting Test...'


echo 'Validating solution...'
USROUT=$(python "$PNUM"_"$USRN".py)
ANSOUT=$(cat answer.txt)
if [ $USROUT == $ANSOUT ]; then
        echo 'Valid Output!'
else
        echo 'Invalid Output!'
        echo 'Test Failed...'
        exit
fi

echo 'Timing solutions...'
for PYFILE in $(ls -f *.py | grep $PNUM)
do
        echo "Timing $PYFILE..."
        EXECINFO=$(python $PYTIMER $PYFILE)
        echo "$EXECINFO" >> timings.txt
done
echo 'Finished timing!'

echo 'Solution Times:'
cat timings.txt
echo 'Finished test...'