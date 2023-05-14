//Script takes data from the json or database and formats it onto the document

const list_container = document.getElementById("case-list");

function h() {
  //fyi: Get json data from the link provided
  const testapi = "https://dummyjson.com/products";
  const elemdiv = document.getElementById("case-list");
  fetch(testapi)
    .then((res) => res.json())
    .then((tofo) => {
      tofo.forEach((post) => {
        for (const property in post) {
          const value = post[property];
          elemdiv.innerHTML += `<p>${property}: ${value}</p>`;
          //case_container_box.innerHTML = `<h1>${post.title}</h1><p>${post.description}</p>`;
        }
      });
    })
    .catch(console.error);
}
