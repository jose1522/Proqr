//Funcion que permite filtrar en los User cards. Utiliza JS para obtener los componentes

function filterUserCards() {
    var input, filter, cards, cardContainer, h5, title, i;
    input = document.getElementById("userCardFilter");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("userCardList");
    cards = cardContainer.getElementsByClassName("card");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h5.card-title");
        subtitle = cards[i].querySelector(".card-body h6.card-subtitle");
        text = cards[i].querySelector(".card-body p.card-text");

        if (
            title.innerText.toUpperCase().indexOf(filter) > -1 ||
            subtitle.innerText.toUpperCase().indexOf(filter) > -1 ||
            text.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

//Funcion que permite filtrar en los Request cards. Utiliza JS para obtener los componentes

function filterRequestCards() {
    var input, filter, cards, cardContainer, h5, title, i;
    input = document.getElementById("purchaseCardFilter");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("purchaseCardList");
    cards = cardContainer.getElementsByClassName("card");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h5.card-title");
        subtitle = cards[i].querySelector(".card-body h6.card-subtitle");
        text = cards[i].querySelector(".card-body p.card-text");

        if (
            title.innerText.toUpperCase().indexOf(filter) > -1 ||
            subtitle.innerText.toUpperCase().indexOf(filter) > -1 ||
            text.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

//Permite crear un TimeLine chart de los Requests por medio de plotly
//Recibe la data que va a ser utilizada para alimentarla

function closedRequestsTimeline(data) {
    var trace1 = {
        x: data['x'],
        y: data['y'],
        type: 'scatter'
    };

    var data = [trace1]

    var layout = {
        title: 'Approved vs Rejected Requests Timeline',
        font: { size: 12 }
    };

    var config = { responsive: true, scrollZoom: true }

    Plotly.newPlot('closedTimelineChart', data, layout, config);
}
//Permite crear un Pie chart de los Requests por medio de plotly
//Recibe la data que va a ser utilizada para alimentarla


function closedRequestsPieChart(data) {
    var data = [{
        values: data['x'],
        labels: data['y'],
        type: 'pie'
    }];


    var layout = {
        title: 'Chart Title',
        font: { size: 12 }
    };

    var config = { responsive: true, scrollZoom: true }
    Plotly.newPlot('closedPieChart', data, layout, config);
}

//Permite crear un TimeLine chart de los Requests por medio de plotly
//Recibe la data que va a ser utilizada para alimentarla
//Por medio del key se accesa la data que se necesita en específico
//El id permite decirle a cuál gráfico se le quiere aplicar

function createBarChart(data, key, id ) {
    data = data[key];
    var layout;
    data = [
        {
            x: data['x'],
            y: data['y'],
            type: 'bar'
        }
    ];

    console.log(data);

    if (key === 'RejectedChart'){
        layout = {
            title: 'Rejected Chart',
            font: { size: 12 },
            xaxis: {
                title: {
                    text: 'Months',
                 font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                        }
                    },
            },
            yaxis: {
                title: {
                    text: 'Rejected Requests',
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                    }
                }
             }
        };
    }

    if (key === 'RecievedChart'){
        layout = {
            title: 'Received Chart',
            font: { size: 12 },
            xaxis: {
                title: {
                    text: 'Months',
                 font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                        }
                    },
            },
            yaxis: {
                title: {
                    text: 'Received Requests',
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                    }
                }
             }

        };
    }

    if (key === 'ApprovedChart'){
        layout = {
            title: 'Approved Chart',
            font: { size: 12 },
            xaxis: {
                title: {
                    text: 'Months',
                 font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                        }
                    },
            },
            yaxis: {
                title: {
                    text: 'Approved Requests',
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                    }
                }
             }
        };
    }

    var config = { responsive: true, scrollZoom: true }
    Plotly.newPlot(id, data, layout, config);

}

