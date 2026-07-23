(function () {
  "use strict";

  var nav = document.getElementById("site-nav");
  if (!nav) {
    return;
  }

  var button = nav.querySelector("button");
  var visibleLinks = nav.querySelector(".visible-links");
  var hiddenLinks = nav.querySelector(".hidden-links");
  var breaks = [];
  var resizeFrame;

  function setMenuState(isOpen, returnFocus) {
    hiddenLinks.classList.toggle("hidden", !isOpen);
    button.classList.toggle("close", isOpen);
    button.setAttribute("aria-expanded", isOpen ? "true" : "false");
    button.setAttribute(
      "aria-label",
      isOpen ? "Close navigation" : "Open navigation"
    );

    if (returnFocus) {
      button.focus();
    }
  }

  function availableSpace() {
    return (
      nav.clientWidth -
      (button.classList.contains("hidden") ? 0 : button.offsetWidth + 30)
    );
  }

  function updateNav() {
    setMenuState(false, false);

    while (
      visibleLinks.scrollWidth > availableSpace() &&
      visibleLinks.children.length > 1
    ) {
      breaks.push(visibleLinks.scrollWidth);
      hiddenLinks.insertBefore(
        visibleLinks.lastElementChild,
        hiddenLinks.firstElementChild
      );
      button.classList.remove("hidden");
    }

    while (
      hiddenLinks.children.length &&
      breaks.length &&
      availableSpace() > breaks[breaks.length - 1]
    ) {
      visibleLinks.appendChild(hiddenLinks.firstElementChild);
      breaks.pop();
    }

    if (!hiddenLinks.children.length) {
      button.classList.add("hidden");
      breaks = [];
    } else {
      button.classList.remove("hidden");
    }

    button.setAttribute("count", hiddenLinks.children.length);
  }

  button.addEventListener("click", function () {
    setMenuState(button.getAttribute("aria-expanded") !== "true", false);
  });

  hiddenLinks.addEventListener("click", function (event) {
    if (event.target.closest("a")) {
      setMenuState(false, false);
    }
  });

  document.addEventListener("keydown", function (event) {
    if (
      event.key === "Escape" &&
      button.getAttribute("aria-expanded") === "true"
    ) {
      setMenuState(false, true);
    }
  });

  document.addEventListener("click", function (event) {
    if (
      button.getAttribute("aria-expanded") === "true" &&
      !nav.contains(event.target)
    ) {
      setMenuState(false, false);
    }
  });

  window.addEventListener("resize", function () {
    window.cancelAnimationFrame(resizeFrame);
    resizeFrame = window.requestAnimationFrame(updateNav);
  });

  updateNav();

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(updateNav);
  }
})();
