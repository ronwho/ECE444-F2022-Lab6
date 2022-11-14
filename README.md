# ECE444-F2022-Lab6

## Add test cases to your group project
Please see the 6 tests I wrote for my project. The test cases I wrote is highlighted in the link and is wrapped with "START RON'S TEST CASES" and "END RON'S TEST CASES" comments. Here I tested my own feature checking if the course check qualification is working as expected. All test cases passed after testing.

https://github.com/ECE444-2022Fall/project-1-web-application-design-education-pathways-group-8-8ball/blob/dd493662b17686bc1bb2a4e62fe6e9c4b4025f82/Education_Pathways/tests/test_app.py#L70-L128

Test cases:
- test_minors_of_APS360()
- test_certificates_of_APS360()
- test_majors_of_APS360()
- test_minors_of_wrong_course_codes()
- test_certificates_of_wrong_course_codes()
- test_majors_of_wrong_course_codes()

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
