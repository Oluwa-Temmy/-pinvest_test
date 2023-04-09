fetch("/static/main/json/case_list_data/case_block_data.json")
  .then((response) => response.json())
  .then((data) => {
    const list = document.getElementById("case-list-item");
    data.forEach((element) => {
      const li = document.createElement("p");
      li.textContent = element.name;
      list.appendChild(li);
    });
  })
  .catch((error) => console.error(error));
