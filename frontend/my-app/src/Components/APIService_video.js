export default class APIService_video{
  
    static async sendQuery_video(body){
  
      console.log(body)
  
      try {
        const response = await fetch(`http://localhost:59004/seeker/VideoFetchQuery`, {
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
  