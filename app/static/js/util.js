var nextUntil = function (elem, selector, filter) {
    // matches() polyfill
    if (!Element.prototype.matches) {
        Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector;
    }

    // Setup siblings array
    var siblings = [];

    // Get the next sibling element
    elem = elem.nextElementSibling;

    // As long as a sibling exists
    while (elem) {

        // If we've reached our match, bail
        if (elem.matches(selector)) break;

        // If filtering by a selector, check if the sibling matches
        if (filter && !elem.matches(filter)) {
            elem = elem.nextElementSibling;
            continue;
        }

        // Otherwise, push it to the siblings array
        siblings.push(elem);

        // Get the next sibling element
        elem = elem.nextElementSibling;

    }

    return siblings;

};


var killParent = function (selector) {
  var elems = document.querySelectorAll(selector);
  elems.forEach(function(elem) {
    var elem_par = elem.parentNode;
    elem_par.insertAdjacentElement("afterend", elem);
    elem_par.remove();
  });
};


var copyAttributes = function(target, source) {
  for (var i = 0; i < source.attributes.length; i++) {
    var a = source.attributes[i];
    target.setAttribute(a.name, a.value);
  }
}
