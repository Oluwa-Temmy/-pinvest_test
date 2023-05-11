window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("header-sticky-navbar").style.top = "0";
  } else {
    document.getElementById("header-sticky-navbar").style.top = "-100px";
  }
}
