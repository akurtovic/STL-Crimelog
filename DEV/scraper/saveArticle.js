var moment = require('moment');
var getUniqueId = require('./getUniqueId');

var saveArticle = function (title, link, source) {
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

module.exports = saveArticle;