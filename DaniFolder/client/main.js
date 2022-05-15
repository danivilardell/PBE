
testTable = [{"Day":"Tue","Hour":"08:00:00","Subject":"TD","Room":"A4-105"},{"Day":"Mon","Hour":"10:00:00","Subject":"AST","Room":"A2-102"},{"Day":"Wed","Hour":"11:00:00","Subject":"ICOM","Room":"A1-102"},{"Day":"Mon","Hour":"08:00:00","Subject":"AST","Room":"A2-102"}];

function createTable(tableData) {
    if(tableData.length == 0) return;

    let table = document.getElementById('table');
    table.innerHTML = "";

    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    table.appendChild(thead);
    table.appendChild(tbody);

    console.log(tableData[0])
    let row = document.createElement('tr');
    for(const [key, value] of Object.entries(tableData[0])) {
        let tableValue = document.createElement('th');
        tableValue.innerHTML = key;
        row.appendChild(tableValue);
    }

    thead.appendChild(row);

    for(let i = 0; i < tableData.length; i++) {
        row = document.createElement('tr');

        for(const [key, value] of Object.entries(tableData[i])) {
            let tableValue = document.createElement('td');
            tableValue.innerHTML = value;
            row.appendChild(tableValue);
        }

        thead.appendChild(row);
    }
}

function handleQuery() {
    let text = document.getElementById('queryText').value;
    makeQuery(text)
}

function makeQuery(query) {
    //AQUI S'HA DE FER LA QUERY
    console.log(query);
    createTable(testTable);
}

let queryButton = document.getElementById('queryButton');
queryButton.addEventListener("click", handleQuery);
