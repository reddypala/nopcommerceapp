pytest -s -v -m "sanity" --html=Reports\sanityReport.html TestCases --browser chrome

rem pytest -s -v -m "sanity or regression" --html=./Reports/sanOrRegReport.html TestCases/ --browser chrome


rem pytest -s -v -m "sanity and regression" --html=./Reports/san&RegReport.html TestCases/ --browser chrome

rem pytest -s -v -m "regression" --html=./Reports/regressionReport.html TestCases/ --browser chrome