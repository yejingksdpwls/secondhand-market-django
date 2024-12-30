# 🛒 중고마켓 웹 서비스
사용자가 중고 물품을 등록하고 거래할 수 있는 직관적이고 편리한 중고거래 플랫폼입니다.

----

## 목차
[ 1. 개요 ](#📌-개요)

[ 2. 개발 기간 ](#📅-개발-기간)

[ 3. 기능 ](#✨-기능)

---

## 📌 개요
** 중고마켓 웹 서비스** 는 중고 거래를 쉽고 안전하게 진행할 수 있는 환경을 제공합니다.
회원 가입부터 상품 등록, 검색, 그리고 거래까지, 직관적인 UI와 강력한 기능을 제공합니다.

#### 기술 스택
**Backend:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white), 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
**Database:**
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white)

---

## 📅 개발 기간
프로젝트 기간: 2024년 12월 11일 ~ 2024년 12월 27일
팀 구성: 개인 프로젝트 (1인 개발)

---

## ✨ 기능
#### 1️⃣ 회원 기능
* **회원가입 / 로그인 / 로그아웃**
  사용자는 이메일, 사용자 이름(username), 비밀번호를 입력해 회원가입을 할 수 있습니다.
  로그인 및 로그아웃 기능을 통해 사용자 계정 관리가 가능합니다.

* **프로필 관리**
  * 각 유저는 자신만의 프로필 페이지를 가집니다.
  * 프로필 페이지에서 유저 정보(username, 가입일, 내가 등록한 물품 목록, 찜한 물건 목록)를 확인할 수 있습니다.
  * **프로필 사진 관리 기능**:
    * 사용자는 프로필 사진을 자유롭게 등록 및 수정할 수 있습니다.
    * 프로필 사진이 없는 사용자는 기본 프로필 이미지가 설정됩니다.

* **팔로우(Follow)**
  * 각 유저의 프로필 페이지에서 다른 유저를 팔로우하거나 언팔로우할 수 있습니다.
  * 프로필 페이지에 팔로우/팔로워 숫자를 표시합니다.

#### 2️⃣ 게시 기능
* **물건 게시 및 관리**
  * 사용자는 물건 **등록 / 수정 / 삭제 / 조회** 기능을 활용할 수 있습니다.
  * 물건 페이지는 **물건 목록 페이지**와 **개별 물건 상세 페이지**로 나뉘어 구성됩니다.

* **찜하기(Like)**
  * 사용자는 원하는 물건에 대해 '찜하기'를 할 수 있으며, 각 물건의 찜 횟수를 확인할 수 있습니다.

**조회수**
  * 각 물건의 조회수를 표시하여 인기 있는 게시물을 확인할 수 있습니다.

* **정렬 기능**
* 물건 목록은 다음 두 가지 기준으로 정렬할 수 있습니다:
  1. **최신순 정렬**
  2. **인기도순 정렬** (찜한 횟수에 따라 정렬, 동일한 찜 횟수인 경우 최신순으로 정렬)

#### 3️⃣ 검색 기능
* **물건 검색**
  물건 목록 페이지에서 검색 기능을 제공합니다.
  검색 결과는 다음 조건 중 하나라도 일치할 경우 해당 물건을 노출합니다:
    * **물건 제목(title)**
    * **물건 설명(content)**
    * **판매자 유저네임(username)**

