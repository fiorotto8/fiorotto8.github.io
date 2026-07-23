/*
 * Greedy Navigation
 *
 * Adapted from http://codepen.io/lukejacksonn/pen/PwmwWV
 */

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');

var breaks = [];

function setMenuState(isOpen, returnFocus) {
  $hlinks.toggleClass('hidden', !isOpen);
  $btn.toggleClass('close', isOpen);
  $btn.attr('aria-expanded', isOpen ? 'true' : 'false');
  $btn.attr('aria-label', isOpen ? 'Close navigation' : 'Open navigation');

  if (returnFocus) {
    $btn.trigger('focus');
  }
}

function updateNav() {
  var availableSpace = $btn.hasClass('hidden') ? $nav.width() : $nav.width() - $btn.width() - 30;

  if ($vlinks.width() > availableSpace) {
    breaks.push($vlinks.width());
    $vlinks.children().last().prependTo($hlinks);
    $btn.removeClass('hidden');
  } else if (availableSpace > breaks[breaks.length - 1]) {
    $hlinks.children().first().appendTo($vlinks);
    breaks.pop();
    updateNav();
    return;
  }

  if (breaks.length < 1) {
    $btn.addClass('hidden');
    setMenuState(false, false);
  }

  $btn.attr('count', breaks.length);

  if ($vlinks.width() > availableSpace) {
    updateNav();
  }
}

$(window).on('resize', function() {
  setMenuState(false, false);
  updateNav();
});

$btn.on('click', function() {
  setMenuState($btn.attr('aria-expanded') !== 'true', false);
});

$hlinks.on('click', 'a', function() {
  setMenuState(false, false);
});

$(document).on('keydown', function(event) {
  if (event.key === 'Escape' && $btn.attr('aria-expanded') === 'true') {
    setMenuState(false, true);
  }
});

$(document).on('click', function(event) {
  if ($btn.attr('aria-expanded') === 'true' && !$(event.target).closest('#site-nav').length) {
    setMenuState(false, false);
  }
});

updateNav();
