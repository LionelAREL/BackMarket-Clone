console.log("welcome to home page")

var swiper = new Swiper(".carouselle-1", {
    navigation: {
      nextEl: ".next",
      prevEl: ".previous",
    },
    loop:true,
    slidesPerView: 1,
    spaceBetween: 500,
});

var swiper2 = new Swiper(".carouselle-2", {
    slidesPerView:'auto',
    spaceBetween: 20,
    slidesPerGroup: 4,
    loop: true,
    loopFillGroupWithBlank: true,
    navigation: {
      nextEl: ".next",
      prevEl: ".previous",
    },
  });