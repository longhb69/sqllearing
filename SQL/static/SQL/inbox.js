document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".ws-btn").addEventListener('click', function() {
        const query = document.getElementById("textareaCodeSQL").value;
        fetch(`/query/${query}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Request failed with status " + response.status);
              }
              return response.json();
        })
        .then(data => {
            const columns = data.columns;
            const records = JSON.parse(data.data);
          
            for (let i = 0; i < columns.length; i++) {
              const column = columns[i];
              console.log(column);
            }

            const container = document.querySelector("#table-container")
            deletetable()
            const table = document.createElement("table");
            table.classList.add("ws-table-all", "notranslate");
            table.id = "querytable"
            const thead = document.createElement("thead");
            const tr = document.createElement("tr");
            for(let i=0;i<columns.length;i++) {
                const th = document.createElement("th");
                th.textContent = columns[i];
                tr.append(th)
            }
            thead.append(tr)
            table.append(thead)

            const tbody = document.createElement("tbody");
            for (let i = 0; i < records.length; i++) {
                const record = records[i];
                const row = document.createElement("tr");
                for (let j = 0; j < record.length; j++) {
                const value = record[j];
                const td = document.createElement("td");
                td.textContent = value;
                row.appendChild(td);
                }
                tbody.append(row);
            }
            table.append(tbody);

            container.append(table)
          })
          .catch(error => {
            console.error("Error:", error);
            deletetable()
          });
    })
});

function deletetable() {
    const table_exist = document.getElementById("querytable");
    if (table_exist) {
        const parent = table_exist.parentNode;
        parent.removeChild(table_exist);
    }
}