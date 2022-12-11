<h1 align="center">Simple Ecommerce</h1>

Simple Ecommerce website with all major features of normal Ecommerce ! 
<br>
Contains CRUD, advanced patterns and try to respect clean architecture. 📂
<br>

<p align="center">
  <img width="800" src="" alt=""/>
</p>

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
`python3 manage.py makemigrations` launch migrations <br>
`python3 manage.py migrate` apply migration on database <br>
`python3 manage.py runserver` run server <br>

## Creator
**Lionel AREL**
- <https://github.com/lionelAREL>
## Copyright and license
Code and documentation copyright 2021 the authors. Code released under the
[MIT License].
