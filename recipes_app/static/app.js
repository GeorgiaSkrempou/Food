function search() {
    let input, filter, table, tr;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("recipe-list");
    tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {
        let tds = tr[i].getElementsByTagName("td");
        let flag = false;
        for (let j = 0; j < tds.length; j++) {
            let td = tds[j];
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                flag = true;
            }
        }
        if (flag) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}

