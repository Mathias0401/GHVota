let votosTotales = 0;
let votos1 = 0;
let votos2 = 0;
let votos3 = 0;
let votos4 = 0;

function contVotos(card) {
  if (card == 1) {
    votos1++;
    votosTotales++;
    votos1 = (100 * votos1) / votosTotales;
    console.log(votos1);
  }
}
