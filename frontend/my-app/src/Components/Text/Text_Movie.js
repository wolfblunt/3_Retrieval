import React from 'react'

const Text_Movie = ({data}) => {
  return (
    <div className="textMovie">
      {data.message && data.message.map(message =>{
        return (
          <div className="div_Movie">
          
            <img src={message["imageURL"]} alt="Movie Image" className = "movie_thumbnail"/>
          
            <div className="movie_description">
              <h2 className="h2_movies_description"> { message["title"]} </h2>
              <br></br>
              <p> StarCast : { message["starCast"]==""? "N/A" : message["starCast"]} </p>
              <p> Rating :  { message["rating"] == "" ? "N/A"  : message["rating"] + "%" } </p>
              <p> { message["type"] } </p>
              <p> { message["year"] } </p>
              <a target='_blank' href={ message["url"] }>Know Now!</a>
              
            </div>
          
          
    
          </div>
        )
      })}
    </div>
  )
}

export default Text_Movie