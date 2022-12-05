
// const {MongoClient} = require('mongodb');


const {MongoClient} = require("mongodb");
const fs = require('fs');
const uri = "mongodb+srv://manisha:manisha123@finalcluster.ngionqn.mongodb.net/?retryWrites=true&w=majority";
const databasename = "manishatable"; // Database name


async function main(){
    const uri = "mongodb+srv://manisha:manisha123@finalcluster.ngionqn.mongodb.net/?retryWrites=true&w=majority";
    const client = new MongoClient(uri);

}

main().catch(console.error);


MongoClient.connect(uri).then((client) => {

	const connect = client.db(databasename);

	// Connect to collection
	const collection = connect
		.collection("manishacollection");
	
	// db.removeIdDemo.find({_id:0});

	// db.returnDocumentWithoutObjectId.find({},{_id:0});

	collection.find({}, {projection:{ _id: 0 }}).toArray().then((ans) => {
		console.log("----",ans[0]);


        var accountStr = JSON.stringify(ans[0]);
        console.log("--------",accountStr);
        
        let filedata= JSON.parse(accountStr);
        console.log("------------",filedata);

        let data = JSON.stringify(filedata);
        fs.writeFileSync('public/db.json', data);
	});
}).catch((err) => {

	// Printing the error message
	console.log(err.Message);
})




