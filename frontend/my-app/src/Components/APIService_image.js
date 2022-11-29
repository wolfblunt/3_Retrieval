export default class APIService_image{
  
    static async sendQuery_image(body){
  
      console.log(body)
  
      try {
        const response = await fetch(`http://localhost:59004/seeker/ImageFetchQuery`, {
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
  