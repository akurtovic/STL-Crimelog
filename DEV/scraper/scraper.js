var request = require('request');
var cheerio = require('cheerio');
var moment = require('moment');

// Returns a unique id based on time since epoch
function getUniqueId() {
  var time = new Date().getTime();
  while (time == new Date().getTime());
  return new Date().getTime();
}

function saveArticle(title, link, source) {
	var article = {};
	var id = getUniqueId();
	var timestamp = moment().format();
	article[id] = {};
	article[id]['title'] = title;
	article[id]['link'] = link;
	article[id]['source'] = source;
	article[id]['timestamp'] = timestamp;
	article[id]['headShakes'] = 0;
	console.log(article);
}

function getPostDispatchFeaturedArticles() {
	request('http://www.stltoday.com/news/local/crime-and-courts/', function (error, response, html) {
		var title, link;
		if (!error && response.statusCode == 200) {
			var $ = cheerio.load(html);
			$('#blox-top-left h1 a').each(function(i, element){
				title = $(this).text();
				link = "http://www.stltoday.com" + $(this).attr('href');
				saveArticle(title, link, "St. Louis Post Dispatch" );
			});
		}
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
				saveArticle(title, link, "St. Louis Post Dispatch" );
			});
		}
	});
}

getPostDispatchFeaturedArticles();
getPostDispatchArticles();