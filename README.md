# Bagel Shop
<!-- If you'd like to use a logo instead uncomment this code and remove the text above this line

  ![Logo](URL to logo img file goes here)

-->

Created by: [ABE](https://habet.dev/about) & [add your name](link)

[![picture here]()

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

### Web Framework (Flask | Gunicorn)
- [x] Login
- [x] Logout
- [x] Register
- [ ] index

### Front-end (HTML | CSS | JS | Bootstrap)
- [ ] login.html
- [ ] Logout.html
- [ ] Register.html
- [ ] Index.html
	* Table display of weekly Selection 
	* Change selection (bagel type button | filling drop down menu)
- [ ] Admin Pannel
	* Aproave new user
	* Change the menu
	* View/Print the weekly menu


### Database (Postgresql)
- [x] User table
- [ ] Menu table
- [ ] Selection table


### Deployment (Github | Heroku | Cloudflare)
- [x] github
- [x] Connect github to heroku
- [x] Auto deployment
- [ ] Configure domain
