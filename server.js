const http = require('http');
let fruits = ['Раз', 'Два', 'Три', 'Четыре', 'Пять'];
http.createServer((request, response) => {
  console.log("Сервер запущен!")
    if (request.method == 'GET') {
        console.log(JSON.stringify(fruits))
        response.end(JSON.stringify(fruits));
    }
    else
    if (request.method == 'POST') {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            console.log(body);
            fruits.push(body);
            fruits.splice(0,1);
            response.write("Ваша запись успешно добавлена"+" Измененный массив:"+JSON.stringify(fruits));
            response.end();
        });
    }
}).listen(5000);
