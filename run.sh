
#echo "Moving into the source folder:"
cd src
#echo "Executing program - check README files for assumptions about the h1b_input.csv"
python3 h1b_counting.py
#echo "Returning to calling location"
cd ..
