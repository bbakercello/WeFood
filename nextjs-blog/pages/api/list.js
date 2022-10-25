import fs from 'fs'
import path from 'path'

function buildListPath(){
    return path.join(process.cwd(), 'data', 'feedback.json');
}

function extractLinkData(){
    const filePath = buildListPath()
    const fileData = fs.readFileSync(filePath);
    return JSON.parse(fileData)
}

function handler(req,res){
    if(req.method === 'POST'){
        const email = req.body.email;
        const list = req.body.list
    
    const newList = {
        id: new Date().toISOString(),
        email: email,
        list: list
    };

    //store the deeback data in a file
    const filePath = buildListPath()
    const data = extractLinkData(filePath);
    data.push(newList);
    fs.writeFileSync(filePath, JSON.stringify(data));
    res.status(201).json({message: 'List logged', list: newList});

    }else{
    res.status(405).json({message: 'Not supported currently'})
    }
}