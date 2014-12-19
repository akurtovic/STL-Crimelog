var request = require('request');
var cheerio = require('cheerio');
var moment = require('moment');

function getUniqueTime() {
  var time = new Date().getTime();
  while (time == new Date().getTime());
  return new Date().getTime();
}

function getPostDispatchFeaturedArticles() {
	request('http://www.stltoday.com/news/local/crime-and-courts/', function (error, response, html) {
	var title, link;
	var articles = [];
	if (!error && response.statusCode == 200) {
		var $ = cheerio.load(html);
		$('#blox-top-left h1 a').each(function(i, element){
			title = $(this).text();
			link = "http://www.stltoday.com" + $(this).attr('href');
			var id = getUniqueTime();
			var timestamp = moment().format();
			var article = {};
			article[id] = {};
			article[id]['title'] = title;
			article[id]['link'] = link;
			article[id]['source'] = "St. Louis Post Dispatch";
			article[id]['timestamp'] = timestamp;

			articles.push(article);
		});
	}
	//TODO: Save to Firebase
	console.log(articles);
	});
}

function getPostDispatchArticles() {
	request('http://www.stltoday.com/news/local/crime-and-courts/', function (error, response, html) {
	var title, link;
	var articles = [];
	if (!error && response.statusCode == 200) {
		var $ = cheerio.load(html);
		$('.bull-list li a').each(function(i, element){
			title = $(this).text();
			link = "http://www.stltoday.com" + $(this).attr('href');
			var id = getUniqueTime();
			var timestamp = moment().format();
			var article = {};
			article[id] = {};
			article[id]['title'] = title;
			article[id]['link'] = link;
			article[id]['source'] = "St. Louis Post Dispatch";
			article[id]['timestamp'] = timestamp;

			articles.push(article);
		});
	}
	//TODO: Save to Firebase
	console.log(articles);
	});

}

getPostDispatchFeaturedArticles();
getPostDispatchArticles();