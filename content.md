# Détection de la paternité grâce aux directives #ifdef

**_Février 2023_**

## Auteurs

Nous sommes 4 étudiants en dernière année à Polytech Nice Sophia en spécialisation Architecture Logicielle:

- CHOUHABI Amine (email)
- BOUZOUBAA Fahde (email)
- GROSS Paul (email)
- DIJOUX Robin (robin.dijoux@etu.unice.fr)

## I. Contexte

---

Préciser ici votre contexte et Pourquoi il est intéressant.

---

## II. Question générale et décomposition en sous-questions

La question générale est :
**Comment identifier la paternité d’une fonctionnalité en se basant sur la variabilité exprimée par les directives #ifdef ?**

Selon nous pouvoir identifier l’expert d’une certaine fonctionnalité est intéressant pour différentes raisons:

- Le solliciter dans le cas d’une régression ou un bug signalé sur cette fonctionnalité.

- Toute personne ayant accès aux outils qui permettent d'identifier l’expert peuvent le solliciter directement, au lieu de demander au chef d’équipe par exemple qui lui demandera. Ce qui accélère la communication au sein d’une équipe.

- Si une nouvelle recrue commence à travailler sur un sujet en relation avec la fonctionnalité, il pourra facilement identifier l’expert et lui demander des pistes par exemple. Cela peut faciliter la montée en compétence des nouvelles recrues.

- L’expert pourrait faire des revues de code plus rapide et plus efficace des nouvelles extensions implémentées par des personnes qui ne connaissent pas bien la fonctionnalité.

De cette question générale découlent des sous-questions :

- Comment définir la paternité et la variabilité en se basant sur notre vision du sujet ?

- Faut-il se limiter à la contribution de chaque personne pour déterminer la paternité ?

- Pour calculer le ratio de paternité des différents contributeurs, est ce qu’il faut prendre en compte l’importance des contributions? C'est-à-dire, nous pouvons avoir une personne avec 20 commits et une autre avec 10, mais la personne avec 10 commits a contribué dans des parties plus critiques que celle avec 20 commits. Donc la personne avec 10 commits aura un ratio de paternité plus grand que celle avec 20 commits.

- Faut-il compter les personnes ayant des petites contributions dans la paternité d’une fonctionnalité ? En d’autres termes, est ce que le fait de compter les personnes avec des contributions minimales dans la patérnité a une valeur pour le sujet.

- Pour généraliser quels sont les critères les plus importants pour définir la paternité ?

- Jusqu’à quel niveau de précision la variabilité nous permet de résoudre le problème. Peut être qu’il faut prendre en compte d’autres critères pour mieux répondre à la problématique. Et dans ce cas quels seront ces critères.

## III. Sources d'informations et outils de travail

---

Préciser vos zones de recherches en fonction de votre projet, les informations dont vous disposez, ... :

1. les articles ou documents utiles à votre projet
2. les outils
3. les jeux de données/codes que vous allez utiliser, pourquoi ceux-ci, ...

   :bulb: Cette étape est fortement liée à la suivante. Vous ne pouvez émettre d'hypothèses à vérifier que si vous avez les informations, inversement, vous cherchez à recueillir des informations en fonction de vos hypothèses.

---

Les sources que nous comptons exploiter afin de produire ce travail seront des bases de codes ainsi que les méta-données associées. Dans un premier temps nous utiliserons les code source de différents projets. Notre choix s'est porté sur:

- [BusyBox](link)
- [GeckoDev (mirroir de Mozilla Firefox)](link)
-

Ces projets ont été séléctionné de manière précise, car ils:

- ont fréquences de contribution diverses (ces projets vont de ... à ... commits)
- sont développés en C/C++, contenant des points de variabilités _#ifdef_
- sont open-source, pour avoir libre accès au code et aux contributions de chacun
- ont dans leur documentation des noms identifiés (parents de modules, propriétaires, etc.)

Nous utiliserons également les données annexes tel que la structure des répertoires et plus généralement la documentation. De plus nous utiliserons l’api de Github afin de récupérer les informations tel que les insights, les contributeurs etc…

Pour effectuer nos expériences nous avons construit notre propre outil qui utilise git fame, cppstats et git blame afin de répondre aux questions cités ci-dessus. Nous les avons combiné à des filtres grep afin d’extraire les métriques que nous souhaitons.

Concernant les métriques, nous comptons nous baser sur les informations relatives au commits qui portent les directives ifdef contenues dans github, informations obtenues par les outils cités ci-dessus.

## IV. Hypothèse et expériences

---

1. Il s'agit ici d'**énoncer sous forme d'hypothèses** ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer/vérifier facilement._ Bien sûr, votre hypothèse devrait être construite de manière à _vous aider à répondre à votre question initiale_. Explicitez ces différents points.
2. Vous **explicitez les expérimentations que vous allez mener** pour vérifier si vos hypothèses sont vraies ou fausses. Il y a forcément des choix, des limites, explicitez-les.

   :bulb: Structurez cette partie à votre convenance : Hypothèse 1 => Expériences, Hypothèse 2 => Expériences ou l'ensemble des hypothèses et les expériences....

---

Dans notre démarche nous partons de l'hypothèse suivante:

**La paternité se traduit par la dernière modification du contenu d'un _#ifDef_, couplé à la quantité de code modifié. En reformulant: le dernier contributeur ayant modifié le plus de code à l'intérieur d'un bloc _#ifdef_ est considéré comme le parent. C'est ce critère que notre outil va permettre de faire ressortir.**

Pour valider ou réfuter notre hypothèse, et répondre aux différentes questions que nous avons établi, nous comptons:

1. Analyser le nombre de commits à l'intérieur d'un bloc “ifdef” pour chaque personne dans le projet.
2. Déterminer pour chaque contributeur du projet et chaque point de variabilité (“ifdef”), combien de fois a-t-il contribué.
3. Comparer ces résultats avec les informations connues sur le projet (le choix des projets testés est fait en partie sur le critère de la présence de ce genre d’informations).

Cette expérience sera utile dans notre questionnement car:

- Nous pourront savoir si les plus gros contributeurs sur les points de variabilité sont les parents de cette variabilité.
- Nous pourront facilement déterminer l’ensemble des personnes possiblement compétentes sur telle ou telle fonctionnalité.
- Nous auront un aperçu de s’il existe une relation **propriétaire du projet <-> plus gros contributeur <-> parent de la variabilité**.

Les limites de notre raisonnement et de notre outil sont la temporalité. Comme dit précédemment, nous nous intéressons aux dernières modification sur chaque ligne à l'intérieur d'un bloc _#ifdef_. Cette démarche est plus ou moins réaliste, car à l’instant T, nous avons des données sur tout le projet dans sa toute dernière version. Il serait cependant intéressant d’analyser sur l’évolution du projet, pour que les resultats ne soient pas biaisés.

## V. Analyse des réultats et conclusion

---

1. Présentation des résultats
2. Interprétation/Analyse des résultats en fonction de vos hypothèses
3. Construction d’une conclusion

   :bulb: Vos résultats et donc votre analyse sont nécessairement limités. Préciser bien ces limites : par exemple, jeux de données insuffisants, analyse réduite à quelques critères, dépendance aux projets analysés, ...

---

## VI. Références

[Documentation de git blame.](https://git-scm.com/docs/git-blame)

[Documentation de git fame.](https://github.com/casperdcl/git)
