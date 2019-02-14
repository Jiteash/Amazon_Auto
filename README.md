# Amazon_Auto
Code reusability, has the input is defined outside the class in a list

By default the input is “Books ” and “data catalog” and code works fine as well when you the input from the same category “Books”
    Ex: “Books” = “Data analytics” also produces same result

Code fails when you change the category that too only because the ” Book” category alone is having kindle and paperback tag whereas if you comment those two tags it will appropriate title output for all categories.
        
The output of the result is printed in Python console as well as in a spreadsheet

By default, Spreadsheet will be saved by a file name “output.xls” in your default Python file location

 
Future Improvements:
•	Since, input is already given through list. By inserting a for loop in the function we can search and print multiple items  in the spreadsheet
