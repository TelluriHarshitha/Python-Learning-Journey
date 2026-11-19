''' python executes the statements from top to bottom .
Transferflow statements are used to alter the flow of execution of the program.

the transferflow statements contains 3 looping transfer statements and 1 functional transfer statement
1.break
2.continue
3.pass
4.return--functional transfer statement

break--when the particular condition is met,it stops the iteration ,comes out of the loop.
it should not be without loops.

ex--if user=='yes':
   break
output--syntax error raises --it says if is a condition but break needs loop to terminiate.


2.continue---it skips the current iiteration and does not stop loop.
this also should not work if we use without loops.

example: if user=="none":
  continue
  output:synatx error: says it requires looop to skip

3.pass---allows us to write an intentionally empty block without getting any syntax errors
pass-- do nothing, empty statement it  avoid the errors by creating like empty blocks.
Imagine you're developing an employee management application. You have planned three functions, but haven't implemented their logic yet.
then pass will work here

where to use pass
we can use pass wherever python needs a empty statement--in loops,if,if-else,functions,class,exception handling
it can be used a outside loop ,anywhere in program


4.return--is used in functions,without functions  we can't use the return statement.
purpose--send the result of the function and gives return back to caller

if we wrrite just return --it takes result as none
