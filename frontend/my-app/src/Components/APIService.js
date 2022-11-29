export default class APIService{
  
  static async sendQuery(body){
    console.log(body)

    try {
      const response = await fetch(`http://localhost:59004/seeker/fetchQuery`, {
        'method': 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      });

      return await response.json();

    } catch (error) {  
      return console.log(error);
    }

  }

}
