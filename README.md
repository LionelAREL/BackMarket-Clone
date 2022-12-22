<h1 align="center">Black Market Clone</h1>
<p align="center">
  Be sure to ⭐ my repo so you can keep up to date on any daily progress ! ❤
</p>
<br>
<p align="center">
  <a href="https://ecommerce.lionel-arel.com" target="_blank">👋 demo here !</a>
</p>
<br>
Clone of BlackMarket ecommerce website with all major features ! 🚀
<br>
Contains CRUD, advanced patterns and try to respect clean architecture. 📂
<br>
<br>
<img width="800" src="https://github.com/LionelAREL/BlackMarket-Clone/blob/main/screenshots/screenshot-3.png" alt=""/>
<img width="800" src="https://github.com/LionelAREL/BlackMarket-Clone/blob/main/screenshots/screenshot-1.png" alt=""/>
<img width="800" src="https://github.com/LionelAREL/BlackMarket-Clone/blob/main/screenshots/screenshot-5.png" alt=""/>

## Stack
- React <br>

    > Redux
   
    > Mui
    
    > Styled-components
    
    >Typescript
- Django <br>

    > django Rest Framework

    > corsheaders

    > django_filters
- Html/Css
- Postgresql


## Features
- [x] CRUD: create, update and remove articles, users, cart
- [x] Authentication with cookie session
- [x] Admin page to manage backend
- [x] Pagination of articles
- [x] Cart gestion and separation between anonymous users and authenticated users
- [x] Differents authorizations, only admin users can access to the admin page
- [x] Manage your cart
- [x] Redirect to the Stripe payment with the details of your cart
- [x] After paiement, update the stocks
- [x] Login and Register Page to authenticate users 
- [x] Password forgot Page where users enter their address mail and will receive on their mailbox a link to reset their password

## Setup
#### Frontend
`npm install` install dependency  <br>

`npm start` run locally the project <br>
#### Backend
`python3 manage.py makemigrations` launch migrations <br>

`python3 manage.py migrate` apply migration on database <br>

`python3 manage.py runserver` run server <br>

## Creator
**Lionel AREL**
- <https://github.com/lionelAREL>
## Copyright and license
Code and documentation copyright 2021 the authors. Code released under the
[MIT License](https://github.com/LionelAREL/BlackMarket-Clone/blob/main/LICENSE.md).
