var request = require('request');
var cheerio = require('cheerio');
var saveArticle = require('../saveArticle.js');

var getPostDispatchArticles = function () {
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

module.exports = getPostDispatchArticles;