# ECE444-F2022-Lab6

## Add test cases to your group project
Please see the 6 tests I wrote for my project. Here I tested my own feature checking if the course check qualification is working as expected. All test cases passed after testing.

https://github.com/ECE444-2022Fall/project-1-web-application-design-education-pathways-group-8-8ball/blob/1cb8e038ce08f4599c60a7dbb22fb17958c7bd4a/Education_Pathways/tests/test_app.py#L70-L128

## Pros and Cons of TTD

### Pros
1. Able to make sure that the new changes did not affect your old testcases, if old testcases fail this makes it easier to debug
2. Able to achieve high test coverage of the code
3. Forces your code to be more modular
4. When submitting a pull request and you include what your test cases are and how they have passed makes it easier for others to quickly understand what the new changes are doing
5. Can catch small mistakes instantly
6. Testing becomes automated, no longer need to manually test everything by clicking through everything
7. Able to be refactored easily, since every new feature is throuogly unit tested

### Cons
1. Development becomes much slower because you always need to write the test first before jumping into developing
2. Requires more brainpower to come up with the test instead of writing the code immediately
3. Sometimes it is difficult / tedious to write tests depending on what the program is doing
4. Even the written test cannot catch all errors, manually testing extensively usually will gurantee the user would not see any weird errors
