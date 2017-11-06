# PUI2017 HW 4.

## Assignment 1: Review your classmate's Citibike project proposal

I did assignment 1 by myself.I reviewed Imran Khan's homework(iuk202, iuk0162).

## Assignment 2: Literature choices of statistical tests

I worked with Guobing Chen. I read and summarized the artical used multiple regression. We discussed about the variable types and control variable.

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi-square test	| 1, Vertebral situation | ordinal | 1, Proportion of aggressive horses| Numeric | 2, activities and housing conditions | categorical | 	In horses, aggression towards humans (a common source of accidents for professionals) could be linked to regularly reported vertebral problems of riding horses. | Horses with different Vertebral situations have similar Proportions of aggressive horses. | 0.05 | [Partners with Bad Temper: Reject or Cure? A Study of Chronic Pain and Aggression in Horses](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0012434) |
Multiple regression	|  8, No. of suicide films (total), No. of suicide films (%), Suicide film rating, Genre: Film noir, Milieu drama, Genre: Fantasy, Sci-Fi, Genre: Adventure, Western, Genre: Tragicomedy, Tragedy, Melodrama, Genre: Thriller, Horror| categorical, continuous | 4, Suicidal ideation, Depression, Life satisfaction, Psychoticism, respectively| continuous| 3, Sex, Age, Education | categorical, continuous| The study investigates that if film genre preference is associated with risk factors for suicide. | Film genre preferences have no influence on risk factors of suicide. | 0.05 | [Associations between Film Preferences and Risk Factors for Suicide: An Online Survey](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0102293) |
Logistic regression	| 1, Source of dental knowledge| Categorical | 1, Oral health behavior| categorical | 1, gender| Categorical  | 	The aim of this study was to investigate the associations between the source of dental knowledge and oral health behavior in a group of students at a university in Japan. |The source of dental knowledge does not influence oral health behavior | 0.05 | [Associations between dental knowledge, source of dental knowledge and oral health behavior in Japanese university students: A cross-sectional study](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0179298) |
  |||||||||

# FBB good, interesting papers too

## Assignment 3: Reproduce the analysis of the Hard to Employ program in NY:

I did assignment 3 by myself.

I did Z test and chi-sq test for two cases.

1: "Ever employed in a CEO transitional job" data

2: "Convicted of a felony after 3 years" data.

## Assignment 4: Tests of correlation using the scipy package with citibike data.

I used KS, Pearson's, Spearman's tests to examine if the distributions in the cases listed below are different.

1) trip duration of bikers that ride during the day vs night

2) age of bikers for trips originating in Manhattan and in Brooklyn

Thanks to Zhiao Zhou and Yukun Wan who introduced the methods of filtering the coordinates that fall into the polygon of different boroughs by importing shapefile and the citibike data to ArcGIS. MN.csv and BK,csv are filted data using ArcGIS.


