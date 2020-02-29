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