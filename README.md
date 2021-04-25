## [/Analyzing_tone_of_comments][1] - Сервис анализа тональности русскоязычных комментариев.
- Стек: NLTK, TFIDF, Pymorphy2, Flask
- В рамках проекта была найдена оптимальня модель, создан единый пайплан обработки(очистка текста, лемматизация), модель была сохранена и в дальнейшем использовалась в Flask-приложении для анализа токсичности.
1. Selecting_model.ipynb - анализ данных, создание обработчиков(очистка данных, лемматизация), выбор лучшей модели, создание единого пайплайна, обучение и сохранение финальной модели
2. run_server - скрипт запуска сервера для приема запросов
3. request_example - пример простого запроса

## [/Scrapy_parser_mongodb_example][2] - Parsing data(product info, product images) of the store; saving in MongoDB. Парсинг данных(инфо о товаре, изображения товара) магазина с сохранением в MongoDB.
- Стек: MongoDB, scrapy

## [/MySQL_creating_and_requests_example][3] - Creating MySQL database for online store operations. Cоздание MySQL-базы данных для функционирования интернет-магазина
- Стек: SQL, MySQL 8

Данная база данных представляет собой пример организации интренет-магазина (учебный проект). В базе данных хранится информация о товарах,заказах,данных пользователей,просмотрах,комментариях,данных доставки и т.д.

## [/CatBoostClassifier_model][4] - Classification of credit default occurrence. Классификация наступления кредитного дефолта(Прогнозирования невыполнения долговых обязательств по текущему кредиту)
- Модель: CatBoost
- Исходные данные приложены к решению

В подготовке данных применен анализ выборок по различным статистическим тестам и проверены гипотезы относительно распределения каждого параметра, на основании результатов которых принималось первичное решения о целесообразности использования признака.

## [/Voting_Regressor][5] -  Prediction apartment prices. Прогнозирование цен на квартиры при помощи VotingRegressor(CatBoost, RandomForestRegressor, GradientBoostingRegressor)
- https://www.kaggle.com/c/realestatepriceprediction

## [/Self_made_Stochastic(batch)_Gradient_Boosting][6] - Predicting average exam score. Прогнозирование среднего экзаменационного балла. 
- Самописный пакетный градиентный бустинг(Stochastic(batch) Gradient Boosting)
- https://www.kaggle.com/c/tutors-expected-math-exam-results/overview

## [/Gradient_Boosting_on_RegressionTrees][7] - Predicting average exam score.
- Самописный классический градиентный бустинг(Gradient Boosting on RegressionTrees)

## [/Self_made_LogisticRegression_model][8] - Predicting probability for a tutor to be a proper one for preparing for the math exam
- Самописная логистическая регрессия
- https://www.kaggle.com/c/choose-tutors/overview

---
[1]: https://github.com/mahhets/my_projects/tree/main/Analyzing_tone_of_comments
[2]: https://github.com/mahhets/portfolio/tree/main/Scrapy_parser_mongodb_example(Ogo.ru)
[3]: https://github.com/mahhets/portfolio/tree/main/MySQL_creating_and_requests_example(DNS.ru)
[4]: https://github.com/mahhets/portfolio/tree/main/CatBoostClassifier_model
[5]: https://github.com/mahhets/my_projects/tree/main/Voting_Regressor
[6]: https://github.com/mahhets/my_projects/tree/main/Self_made_Stochastic(batch)_Gradient_Boosting
[7]: https://github.com/mahhets/my_projects/tree/main/Gradient_Boosting_on_RegressionTrees
[8]: https://github.com/mahhets/my_projects/tree/main/Self_made_LogisticRegression_model

