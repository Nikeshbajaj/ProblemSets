
## Problem: Properly Nasted String

A string S consisting of N characters is considered to be properly nested if any of the following
conditions is true:
* S is empty;
* S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
* S has the form "VW" where V and W are properly nested strings.

The assumptions are:
* N is a positive integer (Obviously);
* String S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

For example, given S = "{[()()]}", the function should return 1.For S = "([)()]", the function should
return 0, as explained above.
