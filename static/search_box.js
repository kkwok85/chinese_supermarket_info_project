 const search = document.querySelector(".col1 .search-box input"),
      images = document.querySelectorAll(".image-box");

search.addEventListener("keyup", e =>{
    if(e.key == "Enter"){
        let searcValue = search.value,
            value = searcValue.toLowerCase();
            images.forEach(image =>{
                if(value === image.dataset.name){ //matching value with getting attribute of images
                    return image.style.display = "block";
                }
                image.style.display = "none";
         });
    }
});

search.addEventListener("keyup", () =>{
    if(search.value != "") return;

    images.forEach(image =>{
        image.style.display = "block";
    })
})
 






document.getElementById("defaultOpen").click();

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}










const carImages = {
    "1": "/static/images/shop2.jpg", // toyota furtuner
    "2": "/static/images/shop3.jpg", // toyota rush
    "3": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/25/2888/nissan-terra-2021-50929.jpg", // nissan terra
    "4": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/24/1643/mitsubishi-montero-sport-67797.jpg", // mitsubishi
    "5": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/17/2677/kia-stonic-97542.jpg", // kia stonic
    "6": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/7/1886/ford-mustang-45686.jpg", // ford mustang
    "7": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/25/572/nissan-gt-r-69452.jpg", // nissan gt-r
    "8": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/51/2018/lamborghini-aventador-70102.jpg", // lamborghini aventador
    "9": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/30/1851/toyota-wigo-51298.jpg", // toyota wigo
    "10": "https://imgcdn.zigwheels.ph/medium/gallery/exterior/11/2012/honda-brio-2019-30836.jpg" // honda brio
};



function updateCarImage1() {
    var image = document.getElementById("carImage1");

    image.src = carImages[document.getElementById("carSelector1").value];
}


function updateCarImage2() {
    var image = document.getElementById("carImage2");

    image.src = carImages[document.getElementById("carSelector2").value];
}

//https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event





