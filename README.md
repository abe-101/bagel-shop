# Bagel Shop
<!-- If you'd like to use a logo instead uncomment this code and remove the text above this line
-->
  ![Logo](https://github.com/abe-101/bagel-shop/blob/main/static/favicon-96x96.png)



Created by: [ABE](https://habet.dev/about)

![picture here](https://github.com/abe-101/bagel-shop/blob/main/static/bagel-shop.png)

#### Video Demo: https://youtu.be/upUSN8B-Ohc

## Description
**Breakfast Roster**

A simple secure web app for groups to submit food orders. Featuring OTP email confirmation. 

## Local Installation


Clone Project:

```console
git clone git@github.com:abe-101/bagel-shop.git
```

install dependency's :

```console
pip install cs50
pip install Flask
pip install Flask-Session
pip install psycopg2-binary
pip install requests
pip install Flask-mail
pip install requests
pip install markdown
pip install pygments
```
## Database ##
For this project we used Postgresql from Heroku.
You will need to retreive a secret URI by navigating to to you Heroku app -> Heroku Postgresql -> Settings -> View Credentials

copy the URI
```console
export DATABASE_URL=URI
```
replace URI with you db URI

## Flask Mail ##

You will need to export your username password and sender email:
```
export MAIL_DEFAULT_SENDER=bagel.shop.app@gmail.com
export MAIL_PASSWORD=YOUR SECRET PASSWORD HERE
export MAIL_USERNAME=bagel.shop.app
```

## Flask ##

Start flask:
```console
flask run
```


## Usage

* Password protected login
* Email confirmation with OTP
* Verification - Prevents malicious login attempts 
* Select daily menu
* Email bagel shop
* Request breakfast selection via email

## Configuration

This block of text should explain how to configure your application:

`Detail heroku set up`


## Information

Screenshots of your application below:

![Screenshot 1](https://github.com/abe-101/bagel-shop/blob/main/static/unverify.png)

![Screenshot 2](https://github.com/abe-101/bagel-shop/blob/main/static/otp.png)



## Known Issues

If you discover any bugs, feel free to create an issue on GitHub fork and
send us a pull request.

[Issues List](https://github.com/abe-101/bagel-shop/issues).

## Authors

* [Abe](https:github.com/abe-101)

## Credits

* [toastytortilla](https://github.com/toastytortilla)
* Blauelf



## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


## License

Your Licensing Information goes here. Example: MIT/X11.

## Road Map

### New Technologies
- [x] Flask-APScheduler
- [X] Flask-mail
- [x] Flask-Markdown
- [x] OTP Email verification

### Web Framework (Flask | Gunicorn)
- [x] Login
- [x] Logout
- [x] Register
- [x] index (users choice & update option
- [x] selection POST (update users choice)
- [x] Flask email (resister confirmation | daily menu)
    - [x] OTP email verification 
    - [ ] Weakly email to bagel shop
    - [x] Email me button
- [x] Flask-APScheduler (trigger daily menu email)
- [x] Render this README as about page
- [x] OTP email verification 

### Front-end (HTML | CSS | JS | Bootstrap)
- [x] login.html
- [x] Logout.html
- [x] Register.html
- [x] Index.html
	- [x] Table display of weekly Selection 
	- [x] Change selection (bagel type button | filling drop down menu)
- [x] Favicon (thank you [toastytortilla](https://github.com/toastytortilla))


### Database (Postgresql)
- [x] User table with selection
- [x] Menu table
- [x] Email confirmation column (OTP)

### Deployment (Github | Heroku | Cloudflare)
- [x] Github
- [x] Connect Github to Heroku
- [x] Auto deployment
- [x] Configure domain (Cloudflare)

### README
- [x] Name
- [x] Local Setup
- [x] Known Issues
- [x] Authors
- [x] Contributing
- [x] License
- [x] Road Map
