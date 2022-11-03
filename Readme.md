# Account Book

가계부 어플리케이션 API

## Installation

requirements.txt 파일을 이용하여 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

## Database

![database](./account_book.png)

## Feature

* 회원가입 및 로그인/로그아웃

    + 회원가입을 한 사용자는 로그인과 로그아웃이 가능합니다.
    + 로그인/로그아웃 과정에서 토큰 기반 인증을 적용하였습니다.

* 가계부 CRUD

    + 수입/지출금액 및 메모를 가계부에 등록할 수 있습니다.(Create)
    + 본인이 등록한 가계부에대해 목록 및 상세조회가 가능합니다.(Read)
    + 본인이 등록한 가계부를 수정 또는 삭제할 수 있습니다.(Update, Delete) 