# poc-classificação

### python classificacao.py
 ```
[-1  1 -1]
[0 0 0]
100.0
```

### python classificacao_acessos.py
 ```
88.8888888889
9
```

### python classifica_buscas.py
 ```
Taxa de acerto do MultinomialNB: 82.0
Taxa de acerto do AdaBoostClassifier: 84.0
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 85.0
Taxa de acerto base: 82.000000
Total de testes: 100
 ```

### python classifica_buscas2.py
 ```
Taxa de acerto do MultinomialNB: 82.0
Taxa de acerto do AdaBoostClassifier: 84.0
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 85.0
Taxa de acerto base algoritmo que chuta : 82.000000
Taxa de acerto base: 82.000000
Total de testes: 100
 ```

### python situacao_do_cliente.py
 ```
Taxa de acerto do OneVsRest: 100.0
Taxa de acerto do OneVsOne: 100.0
Taxa de acerto do MultinomialNB: 100.0
Taxa de acerto do AdaBoostClassifier: 100.0
{100.0: AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)}
Vencedor: 
AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 80.0
Taxa de acerto base: 80.000000
Total de testes: 5
 ```

### python situacao_do_cliente_kfold.py
 ```
Taxa de acerto do OneVsRest: 0.829365079365
Taxa de acerto do OneVsOne: 0.928571428571
Taxa de acerto do MultinomialNB: 0.777777777778
Taxa de acerto do AdaBoostClassifier: 0.797619047619
{0.82936507936507942: OneVsRestClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1), 0.77777777777777779: MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True), 0.79761904761904756: AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None), 0.92857142857142849: OneVsOneClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1)}
Vencedor: 
OneVsOneClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1)
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 90.0
Taxa de acerto base: 90.000000
Total de testes: 10
 ```

### python classificando_emails.py
 ```
total de Palavras : 365
Tamanho do treino : 34
Taxa de acerto do OneVsRest: 0.723333333333
Taxa de acerto do OneVsOne: 0.656666666667
Taxa de acerto do MultinomialNB: 0.69
Taxa de acerto do AdaBoostClassifier: 0.423333333333
{0.65666666666666662: OneVsOneClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1), 0.72333333333333338: OneVsRestClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1), 0.69000000000000006: MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True), 0.42333333333333323: AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)}
Vencedor: 
OneVsRestClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1)
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 88.8888888889
Taxa de acerto base: 44.444444
Total de testes: 9
 ```

### python classificando_emails_limpos.py
 ```
total de Palavras : 230
Tamanho do treino : 34
Taxa de acerto do OneVsRest: 0.801666666667
Taxa de acerto do OneVsOne: 0.801666666667
Taxa de acerto do MultinomialNB: 0.83
Taxa de acerto do AdaBoostClassifier: 0.593333333333
{0.80166666666666653: OneVsOneClassifier(estimator=LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0),
          n_jobs=1), 0.83000000000000007: MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True), 0.59333333333333327: AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)}
Vencedor: 
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
[3 1 3 3 1 3 3 1 3]
Taxa de acerto do vencedor entre os dois algoritmos no mundo real: 77.7777777778
Taxa de acerto base: 44.444444
Total de testes: 9 
Valida a frase -> : tenho direito a desconto?
[1]
Valida as 2 frase abaixo: 
 Frase 1 : - Gostaria de receber informações sobre o curso de java! 
 Frase 2 : - Como trocar o player?
[3 2]
```
