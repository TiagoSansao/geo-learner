const fs = require("fs");

let dataToBeScrapped = fs.readFileSync(`${__dirname}/Paises_por_ordem_alfabetica.txt`, "utf-8");

let flags = JSON.parse(fs.readFileSync(`${__dirname}/flags.json`, "utf-8"));

const dataToBeScrappedInitIndex = dataToBeScrapped.indexOf("<tbody>");
const dataToBeScrappedEndIndex = dataToBeScrapped.indexOf("</tbody>");

dataToBeScrapped = dataToBeScrapped.slice(dataToBeScrappedInitIndex, dataToBeScrappedEndIndex);

const regEx = /(?<=<td>)(.[^<>]*)(?=<\/td>)|(?<=<a.*?">)(.[^<>]*)(?=<\/a>)/gmi;
const matchs = dataToBeScrapped.match(regEx);
const countries = [];

while (matchs.length !== 0) {
  const obj = {name: matchs.shift(), capital: matchs.shift(), continent: matchs.shift()};
  countries.push(obj);
}

fs.writeFile(`${__dirname}/../data.json`, JSON.stringify(countries), (err) => {
  if (err) console.log(err);
  else console.log("data.json was successfully generated!");
});