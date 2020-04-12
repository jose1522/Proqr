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
            text.innerText.toUpperCase().indexOf(filter) > -1) 
        {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

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
            text.innerText.toUpperCase().indexOf(filter) > -1) 
        {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

function closedRequestsTimeline(){
    var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        type: 'scatter'
      };
      
      var trace2 = {
        x: [1, 2, 3, 4],
        y: [16, 5, 11, 9],
        type: 'scatter'
      };
      
      var data = [trace1, trace2];
      
      Plotly.newPlot('closedTimelineChart', data);
}  

function closedRequestsPieChart(){
    var data = [{
        values: [19, 26, 55],
        labels: ['Residential', 'Non-Residential', 'Utility'],
        type: 'pie'
      }];
      
      var layout = {
        height: 400,
        width: 500
      };
      
      Plotly.newPlot('closedPieChart', data, layout);
}  

function closedRequestsBarChart(){
    var data = [
        {
          x: ['giraffes', 'orangutans', 'monkeys'],
          y: [20, 14, 23],
          type: 'bar'
        }
      ];
      
      Plotly.newPlot('closedBarChart', data);
}  