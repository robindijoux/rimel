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

On trouve que pouvoir identifier l’expert d’une certaine fonctionnalité est intéressant pour les raisons suivantes :

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

Les sources que nous comptons exploiter afin de produire ce travail seront des bases de codes ainsi que les méta-données associées. Dans un premier temps nous utiliserons le miroir du code source de Mozilla. Nous utiliserons également les données annexes tel que la structure des répertoires et plus généralement la documentation fournie par Mozilla. De plus nous utiliserons l’api de Github afin de récupérer les informations tel que les insights, les contributeurs etc…

Pour effectuer nos expériences nous avons construit notre propre outil qui utilise git fame, cppstats et git blame afin de répondre aux questions cités ci-dessus. Nous les avons combiné à des filtres grep afin d’extraire les métriques que nous souhaitons.

Concernant les métriques, nous comptons nous baser sur les informations relatives au commits qui portent les directives ifdef contenues dans github, informations obtenues par les outils cités ci-dessus.

## IV. Hypothèse et expériences

---

1. Il s'agit ici d'**énoncer sous forme d'hypothèses** ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer/vérifier facilement._ Bien sûr, votre hypothèse devrait être construite de manière à _vous aider à répondre à votre question initiale_. Explicitez ces différents points.
2. Vous **explicitez les expérimentations que vous allez mener** pour vérifier si vos hypothèses sont vraies ou fausses. Il y a forcément des choix, des limites, explicitez-les.

   :bulb: Structurez cette partie à votre convenance : Hypothèse 1 => Expériences, Hypothèse 2 => Expériences ou l'ensemble des hypothèses et les expériences....

---

## V. Analyse des réultats et conclusion

1. Présentation des résultats
2. Interprétation/Analyse des résultats en fonction de vos hypothèses
3. Construction d’une conclusion

   :bulb: Vos résultats et donc votre analyse sont nécessairement limités. Préciser bien ces limites : par exemple, jeux de données insuffisants, analyse réduite à quelques critères, dépendance aux projets analysés, ...

## VI. References

[Debret 2020] Debret, J. (2020) La démarche scientifique : tout ce que vous devez savoir ! Available at: https://www.scribbr.fr/article-scientifique/demarche-scientifique/ (Accessed: 18 November 2022).
