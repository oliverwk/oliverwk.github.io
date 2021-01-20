const puppeteer = require('puppeteer');
const fetch = require('node-fetch');
const fs = require('fs');
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://www.heatmapper.ca/geocoordinate/');
  console.log("On the page");
  await page.waitForSelector('#file');
  await sleep(1000)
  const inputUploadHandle = await page.$('#file');
  let fileToUpload = 'weather.csv';
  console.log("Uploading");
  inputUploadHandle.uploadFile(fileToUpload);
  console.log("Uploaded");
  await page.waitForSelector('#plotDownload');
  await sleep(2500)
  const element = await page.$("#plotDownload");
  const url = await (await element.getProperty('href')).jsonValue();
  console.log("url:", url);
  let res = await fetch(url);
  let rHtml = await res.text()
  fs.writeFile('luchtdruk.html', rHtml, function (err) {
    if (err) return console.log(err);
      console.log('rHtml > luchtdruk.html');
  });
  //await page.screenshot({path: 'example.png', fullPage: true});
  await browser.close();
})();
