import React from 'react'

const Text_News = ({data}) => {

  console.log(data)

  return (

    <div className="textNews">
      {data.message && data.message.map(message =>{ 
        
        return (
        
        <div className='textContainer_news'>
            
            <img src={message["urlToImage"]} alt="News Image" className = "textNews_Image"/>
            <div className="news_description">
              <h2 className="news_title"> { message["title"]} </h2>
              {/* <p> { message["author"] } </p> */}
              <p className='textNews_paragraph'>Source : { message["publisher"] } </p>
              <p className='textNews_paragraph'>Published on :  { message["publishedAt"] } </p>
              <p className='textNews_paragraph'> { message["description"] } </p>
              <a target='_blank' href={ message["url"] }>Read More!</a>
            </div>
           

          </div>

        )
      })}
    </div>
  )
}

export default Text_News