"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const navItems = document.querySelectorAll(".nav-item");

  console.log(navItems);
  navItems.forEach((item) => {
    item.addEventListener("click", function () {
      navItems.forEach((navItem) => navItem.classList.remove("active"));
      this.classList.add("active");
      console.log(12);
    });
  });
});
