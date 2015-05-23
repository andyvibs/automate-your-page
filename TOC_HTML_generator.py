TEST_TEXT = """
Lesson 1: The Basics of the Web and HTML

TITLE: How the Web Works

DESCRIPTION: The web is a bunch of computers that communicate with each other. When a person goes to a web page like www.google.com, their computer sends a HTTP Request to a server. The server finds the appropriate HTML document and sends it back to the user's computer where a web browser interprets the page and displays it on the user's screen. This video does a good job of explaining more.

TITLE: HTML

DESCRIPTION: HTML stands for Hypertext Markup Language. HTML documents form the majority of the content on the web. HTML documents contain text content which describes "what you see" and markup which describes "how it looks". This video gives a good overview.

TITLE: Tags and Elements

DESCRIPTION: HTML documents are made of HTML elements. When writing HTML, we tell browsers the type of each element by using HTML tags. This video explains the distinction well.

TITLE: Why Computers are Stupid

DESCRIPTION: Computers are stupid because they interpret instructions literally. This makes them very unforgiving since a small mistake by a programmer can cause huge problems in a program.

TITLE: Inline vs Block Elements

DESCRIPTION: HTML elements are either inline or block. Block elements form an "invisible box" around the content inside of them.

Lesson 2: Creating a Structured Document with HTML

TITLE: Developer Tools (in the Browser)

DESCRIPTION: HTML elements are either inline or block. Block elements form an "invisible box" around the content inside of them.

TITLE: The "tree-like structure" of HTML

DESCRIPTION: The "tree-like structure" comes from the fact that HTML elements can have other elements inside of them. You can draw this relationship like a family tree. My mother had multiple children. So did her mother, and so on... 
In a browser, this structure shows up as a series of nested boxes. There are oxes inside of boxes inside of boxes, and so on...

TITLE: The relationship between indented HTML and boxes

DESCRIPTION: When you read an HTML document as text, you see a wave of changing indentations going up and down the left side of the document. The more indented an element is, the more deeply nested it's corresponding "box" is.

TITLE: Text Editors (for programming)

DESCRIPTION: When writing code, programmers use special text editors (like Sublime Text for example). These editors make the programmer's life easier. For example, some text editors will automatically generate a closing HTML tag when you write an opening tag.

When adding an Image to a webpage by referencing an image file on your computer, the image file (or folder which includes the image) must be saved in the same file as the HTML code.

Lesson 3: Adding CSS Style to HTML Structure

TITLE: Avoid Repitition

DESCRIPTION: Repitition can create headaches, and even major problems, in the future. The structure and organization of the code you write can help avoid repitition. 
Quote from the example notes - "Consistency: In this web page, I wanted every lesson to look the same. Instead of manually giving each one the same style, I was able to assign each lesson div the same class and then specify the style for that class in only one place! By avoiding repetion, it's now very easy for me to make changes to this style."

Avoiding repitition can mean avoiding unnecessary copy and paste errors. If you're repeating yourself, there's likely a more efficient, safer (lower chance of bug) way to write the code.

TITLE: CSS

DESCRIPTION: CSS (Cascading Style Sheets) allows programmers to control the style of HTML elements. By giving similar elements the same class name, the programmer can apply a style change across the entire class, affecting each element in the class.

cascading - most specific rule applies
Inheritance - style applied to an element will be applied to all descendant elements

TITLE: Additional Notes

DESCRIPTION: Terms

Computer
Machine which can run programs to perform tasks much quicker and more efficiently than humans.
Program
Instructions for a computer, written in a code or language that it can understand
Programming Languages
Just like in the normal world, there are many sets of rules which communication can take place by (languages). Different people are programmed (learn) different sets of rules, or languages, and can therefore understand and use only those languages. This is similar to the idea of programming languages, some computers run different rules.
Interpreter
Telling a computer to do something requires many basic assumptions, too many to think about each time we write code. An interpreter like Python simplifies the language, and allows us to write a program which gets translated into a language the computer can understand.

Python
An example of an Interpreter.
Grammar
The rules by which a code (or language) exist and run by. While humans can be forgiving of grammar mistakes (if I say "Me going to store 2 o'clock" people will be confused, but likely understand what I'm saying. Computers are standardized, which means it does not forgive grammar mistakes
Python Expressions
Legal Python statements that follow Python's grammar rules.
Python

TITLE: Variables

DESCRIPTION: Variables in Python and other computer codes are similar to any type of variable - the variable represents something else, so we can easily change that value. It also helps make code much easier to read.

TITLE: Variable Assignment

DESCRIPTION: The process of giving a variable a new value is called "Assignment." This is done by entering the name of the variable, an equals (=) sign, and then the desired value.

TITLE: Equals Sign Clarification

DESCRIPTION: Traditionally, we think of (=) to mean "equals" as in math, like 2+3=5. In Python, = is more like an arrow (pointing from right to left) showing that the value on the right side will be assigned to the name on the left side.

TITLE: Common Uses of Variables

DESCRIPTION: Variables can be useful when there is a good chance you will change a value. 
Variables (should) make it easier to understand the function of the code. 
Variables can be used to reference other values to make very complex calculations and perform very complex tasks.

TITLE: What is the difference between 2+2 and "2"+"2"?

DESCRIPTION: In Python, print 2+2 will show the value 4, while print "2"+"2" will show the value 22. In the first example, Python does the math, in the second, it concatenates the two strings, showing a result of 22.

TITLE: Functions

DESCRIPTION: A Function or Procedure is an operation or task that a computer can be programmed to do. 
Important Distinction - Making a function involved defining what the function does, essentially telling the computer what it will do when you eventually call it to perform the function. Using a function is the act of calling the computer to perform it. 
Functions can help a programmer avoid repitition by making tedious tasks automated. For example, instead of creating a unique user ID for a customer manually, a progrmamer can write a function which automatically takes a few inputs (ie name, ss#, etc) and creates a unique identifier based on the parameters of the function.
The return keyword is used to tell Python what the output of the function is. Without it, the function will not know what you are asking for when you call the function.

TITLE: Structured Data

DESCRIPTION: Data that is placed into related fields, or sorted in some manner. ie, this string '24 35 75 93 745 02 787 monday tuesday wednesday thursday friday saturday sunday' is technically data, but because it has no structure, it is not very useful. [[monday, 24], [tuesday, 35], [wednesday, 75], [thursday, 93], [friday, 745], [saturday, 02], [sunday, 787] has more structure, and is more powerful and more useful.

TITLE: Mutability

DESCRIPTION: Strings and Lists behave differently. When you've assigned a string to a variable, and then change the string in that variable, you do not actually alter the string itself. Instead, you make an entirely new string, and reassign the variable to the new string. Strings are therefore 'imutable.' Lists, however, are 'mutable.' Rather than creating a new list and reassigning the variable to it, you can change individual elements within the list, which would affect all the variables which refer to the list.

TITLE: difference between APPEND and +

DESCRIPTION: Append adds a new element to the end of the list (changes the original list) whereas + creates a new list, and concatenates the original list and the new element or list into 1 new list.

TITLE: Lists

DESCRIPTION: Lists are a powerful way of structuring data. Unlike strings, which can only contain characters, lists can contain any element, including other lists. Nested lists are a great way of storing and accessing related data.

TITLE: For Loops

DESCRIPTION: structure - for (name) in (list) (indented block)

TITLE: Index Method

DESCRIPTION: This is almost a 'find element' function. When you invoke .index on a list, and pass in a value, .index finds the first occurence of the element in the list and gives you the index position of that occurence.

"""







def generate_concept_tag(concept_number, title):
	current_concept_number = 1
	concept = get_concept_by_number(text, current_concept_number)
	concept_tag = '<a href="#concept-' + concept_number + '">' + title + '</a>'

	return concept_tag



def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-2]
    return title

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept

def generate_TOC_HTML(text):
	current_concept_number = 1
	concept = get_concept_by_number(text, current_concept_number)
	TOC_HTML = ''
	while concept != '':
		title = get_title(concept)
		concept_number = current_concept_number
		concept_tag = generate_concept_tag(concept_number, title)
		current_concept_number += 1
	return TOC_HTML


print generate_TOC_HTML(TEST_TEXT)
