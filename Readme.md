This Sudoko code is implemented via backtracking  Algorithm, In this case it recursively goes back to each cell to abandon its value which it had earlier found,
if it is not able to find valid value for next cell. 

You can get working of backtracking mechanism in 

https://www.tutorialspoint.com/introduction-to-backtracking


This implementation is using pytest framework for testing and pipenv for package management

To execute this code, you will need to install all package requirement with following commands

1.pipenv install 

To go to virtual env you can give

2.pipenv shell

To execute the sudoko puzzle, you will need to provide all 81 numbers of Sudoko in the following format

python src/working.py --board_input  0,0,0,0,7,4,3,1,6,0,0,0,6,0,3,8,4,0,0,0,0,0,0,8,5,0,0,7,2,5,8,0,0,0,3,4,0,0,0,0,3,0,0,5,0,0,0,0,0,0,2,7,9,8,0,0,8,9,4,0,0,0,0,0,4,0,0,8,5,9,0,0,9,7,1,3,2,6,4,8,5


Excepted output would be 

solved suduko :

[5, 8, 9, 2, 7, 4, 3, 1, 6]

[2, 1, 7, 6, 5, 3, 8, 4, 9]

[4, 6, 3, 1, 9, 8, 5, 2, 7]

[7, 2, 5, 8, 1, 9, 6, 3, 4]

[8, 9, 6, 4, 3, 7, 1, 5, 2]

[1, 3, 4, 5, 6, 2, 7, 9, 8]

[6, 5, 8, 9, 4, 1, 2, 7, 3]

[3, 4, 2, 7, 8, 5, 9, 6, 1]

[9, 7, 1, 3, 2, 6, 4, 8, 5]

