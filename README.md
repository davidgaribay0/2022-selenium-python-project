# Test Automation Selenium/Python Sample Project

## Running the project

1. At the root of the project run the command `pip install -r requirements.txt` to install all the requirements
2. Also, at the root of the project, run the command `pytest` this will automatically look for any testcase and run
   those

Example output after running pytest:

```

pytest

================================================================================================================== test session starts ==================================================================================================================
platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
collected 3 items                                                                                                                                                                                                                                       

tests/test_translation.py::TestTranslation::test_valid_translation_from_source_to_target_language 
-------------------------------------------------------------------------------------------------------------------- live log setup ---------------------------------------------------------------------------------------------------------------------
2022-10-30 11:02:20 [    INFO] ====== WebDriver manager ====== (logger.py:11)
2022-10-30 11:02:20 [    INFO] Get LATEST chromedriver version for google-chrome 107.0.5304 (logger.py:11)
--------------------------------------------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------------------------------------------
2022-10-30 11:02:25 [    INFO] Translation Value - la democracia (test_translation.py:51)
2022-10-30 11:02:25 [    INFO] Initial Value - Demokratie (test_translation.py:52)
PASSED                                                                                                                                                                                                                                            [ 33%]
tests/test_translation.py::TestTranslation::test_swap_language_feature 
-------------------------------------------------------------------------------------------------------------------- live log setup ---------------------------------------------------------------------------------------------------------------------
2022-10-30 11:02:25 [    INFO] ====== WebDriver manager ====== (logger.py:11)
2022-10-30 11:02:25 [    INFO] Get LATEST chromedriver version for google-chrome 107.0.5304 (logger.py:11)
--------------------------------------------------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------------------------------------------------
2022-10-30 11:02:32 [    INFO] Translation Value - Demokratie (test_translation.py:62)
2022-10-30 11:02:32 [    INFO] Initial Value - la democracia (test_translation.py:63)
PASSED                                                                                                                                                                                                                                            [ 66%]
tests/test_translation.py::TestTranslation::test_screen_keyboard 
-------------------------------------------------------------------------------------------------------------------- live log setup ---------------------------------------------------------------------------------------------------------------------
2022-10-30 11:02:32 [    INFO] ====== WebDriver manager ====== (logger.py:11)
2022-10-30 11:02:32 [    INFO] Get LATEST chromedriver version for google-chrome 107.0.5304 (logger.py:11)
PASSED                                                                                                                                                                                                                                            [100%]

================================================================================================================== 3 passed in 19.81s ===================================================================================================================

```
