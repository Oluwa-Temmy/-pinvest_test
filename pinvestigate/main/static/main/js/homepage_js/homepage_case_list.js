const testapi = "https://dummyjson.com/products";
const elemdiv = document.getElementById("case-list");
fetch(testapi)
  .then((res) => res.json())
  .then((tofo) => {
    tofo.forEach((post) => {
      case_container_box.innerHTML = `<h1>${post.title}</h1><p>${post.description}</p>`;
    });
  })
  .catch(console.error);
