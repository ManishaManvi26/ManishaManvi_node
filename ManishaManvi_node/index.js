const { equal } = require('assert');
const http = require('http');
const server = http.createServer((req,res)=>{
const fs = require('fs');
const path=require('path');
console.log("req.url")
    

    if (req.url == '/')
    {
        
        fs.readFile(path.join(__dirname,'public','index.html'),(err,data)=>{
            if (err) throw err;
            res.writeHead(200,{ 'context-Type':'text/html'});
            res.end(data)
        })

    }
    else if (req.url == '/api')
    {
        fs.readFile(path.join(__dirname,'public','db.json'),(err,data)=>{
            if (err) throw err;
            res.writeHead(200,{ 'context-Type':'application/json'});
            res.end(data);
        })
    }
    
    else 
    {
        res.end("<h1> 404 not found </h1> ")
    }
  
});

const PORT = process.env.PORT || 5959;
server.listen(PORT,()=>console.log('yayy running ${PORT}'));