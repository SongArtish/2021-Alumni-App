# README

2020.12.30 ~

---

[TOC]

---



## 배경

> 2020년 12월 23일 10명의 차관급 인사가 있었는데 그 중 외교부 차관을 '특정대학 - 특정학과'가 독식하여서 논란이 되었다. ([참고자료](https://www.hankyung.com/politics/article/202012230429i))
>
> 또한, 얼마 전 국토교통부 장관 후보자가 서울주택도시공사(SH) 사장 시절 SH 고위직 공모 때 대학 동문 및 지인을 대거 채용했던 것이 논란이 되기도 하였다. ([참고자료](https://www.chosun.com/politics/assembly/2020/12/22/Y4XHEYZZLFGNBANNCAIZ2BXBDQ/))
>
> 이러한 배경 속에서 학교/학과 별 유명인(인터넷 프로필 등재 기준)의 DB를 구축하여 특정 학교/학과별로 유명인 리스트를 조회할 수 있는 어플리케이션을 개발하면 위의 논란이 되었던 사안들에 조금 긍정적으로 기여할 수 있지 않을까라는 생각으로 이 프로젝트를 시작하게 되었다.



## 목표 서비스

- 학교별, 학과별 혹은 학교/학과별 인물 리스트를 조회할 수 있다.
- 학과별 검색을 통해 해당 학과 출신들이 어떠한 분야에서 활약을 하고 있는지 알 수 있다.
- 학교별 검색을 통해 해당 학교 출신들이 어떠한 분야에서 활약을 하고 있는지 알 수 있다.



## 설계

### 1단계: DB 구축

**사용도구**

- 웹 크롤러: `BeautifulSoup` 혹은 `Selenium`
- DB: `SQL`

**작업사항**

- **나무위키** 사이트로부터 인물들의 정보를 가져온다.
- 나무위키에서는 학교별 인물 리스트를 제공하는 간단한 페이지도 있다.
- 인물들의 출신 고교, 대학, 대학원, 학과, 그리고 현재의 직장 혹은 정부 부서의 데이터를 크롤링한다.
- 데이터 베이스로 저장하여 관리한다.
- 해당 데이터는 매일 아침 9시를 기준으로 업데이트해준다.



### 2단계: 어플리케이션 개발

**사용도구**

- 어플리케이션 개발도구: `Android Studio`
- 사용 언어: `Java`

**작업사항**

- Java와 Android Studio 사용법을 익힌다.
- 어플리케이션과 DB를 연결한다.
- 특정 조건에 따라 리스트를 조회할 수 있는 알고리즘을 작성한다.
- User-friendly한 UI를 개발한다.



***Copyright* © 2021 Song_Artish**