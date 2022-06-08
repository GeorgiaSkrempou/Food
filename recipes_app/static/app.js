// new gridjs.Grid({
//   from: document.getElementById("recipe-list"),
//   search: true,
//   sort: true,
//   pagination: true,
//   style: {
//     th: {
//       "text-align": "center"
//     },
//     td: {
//       "text-align": "center"
//     },
//
//   },
// }).render(document.getElementById("pretty-table"));
//

function myFunction() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("recipe-list");
    tr = table.getElementsByTagName("tr");
    for (var i = 0; i < tr.length; i++) {
        var tds = tr[i].getElementsByTagName("td");
        var flag = false;
        for (var j = 0; j < tds.length; j++) {
            var td = tds[j];
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