let articles = [
    {
        id: 1,
        title: "JS",
        text: "Статья про JS",
        author: "Александр"
    },
    {
        id: 2,
        title: "PHP",
        text: "Статья про PHP",
        author: "Виталий"
    },
    {
        id: 3,
        title: "Базы Данных",
        text: "Статья про Базы Данных",
        author: "Евгения"
    },
    {
        id: 4,
        title: "HTML",
        text: "Статья про HTML",
        author: "Виталий"
    }
];

let goods = [
    {
        title: "Пианино",
        price: 3000,
        count: 25
    },
    {
        title: "Гитара",
        price: 1200,
        count: 40
    },
    {
        title: "Барабаны",
        price: 2700,
        count: 12
    },
    {
        title: "Флейта",
        price: 900,
        count: 50
    },
    {
        title: "Арфа",
        price: 3400,
        count: 5
    }
];
function createTable(nameTable, rows, cell, object) {
    let tableArea = document.getElementById("users-block");
    let table = document.createElement("table");
    table.setAttribute("border", 1);
    let caption = table.createCaption();
    caption.innerText = nameTable;
    for (let i = 0; i < object.length; i++) {
        let row = table.insertRow(i);
        for (let j = 0; j < cell; j++){
            let cell = row.insertCell(j);
            for (let a in object[i]) {
                cell.innerText = object[i][a];
            }
        }


    }

    tableArea.append(table);
}


createTable('Список статей', 4, 4, articles);
createTable('Список покупок', 5, 3, goods);
