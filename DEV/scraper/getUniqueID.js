// Returns a unique id based on time since epoch
function getUniqueId() {
  var time = new Date().getTime();
  while (time == new Date().getTime());
  var tempId = new Date().getTime()
  var uniqueId = tempId - 1419100000000;
  return uniqueId;
}

module.exports = getUniqueId;