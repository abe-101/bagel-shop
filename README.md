# Bagel Shop
<!-- If you'd like to use a logo instead uncomment this code and remove the text above this line

  ![Logo](https://github.com/abe-101/bagel-shop/static/logo.png)

-->

Created by: [ABE](https://habet.dev/about) & [add your name](link)

![picture here](https://github.com/abe-101/bagel-shop/static/hompage.png)

## Description
**Breakfast Roster**


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
```

export postgresql env key(replace URI with you db URI):

```console
export DATABASE_URL=URI
```

Start flask:
```console
flask run
```


## Usage

Put the usage explanation here

```erb
<%= your_code_goes @here do |f| %>
  <%= f.input :example %>
  <%= f.input :example %>
  <%= f.button :example %>
<% end %>
```


## Configuration

This block of text should explain how to configure your application:

`Detail heroku set up`


## Information

Screenshots of your application below:

![Screenshot 1](http://placekitten.com/400/300)

![Screenshot 2](http://placekitten.com/400/300)



## Known Issues

If you discover any bugs, feel free to create an issue on GitHub fork and
send us a pull request.

[Issues List](https://github.com/abe-101/bagel-shop/issues).

## Authors

* [Abe](https:github.com/abe-101)
* Additional Author's name (Their Github URL goes here)
	

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
    - [ ] OTP email varification 
    - [ ] Weakly email to bagel shop
    - [x] Email me button
- [x] Flask-APScheduler (trigger daily menu email)
- [x] Render this README as about page
- [x] OTP email varification 

### Front-end (HTML | CSS | JS | Bootstrap)
- [x] login.html
- [x] Logout.html
- [x] Register.html
- [x] Index.html
	* Table display of weekly Selection 
	* Change selection (bagel type button | filling drop down menu)
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
- [ ] Name
- [ ] Local Setup
- [x] Known Issues
- [x] Authors
- [x] Contributing
- [ ] License
- [ ] Road Map
