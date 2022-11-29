import React from 'react'

const Text_Article = ({data}) => {
  return (
    <div className="textArticle">
      {data.message && data.message.map(message =>{  
        return (
          <div className="article_description">
            <img src={require('./article.jpeg')} className="article_image"/>
            <div className="article_description_2">  
              <h2 className="article_header"> { message["title"]} </h2>
              <p> { message["author"] } </p>
              <p> { message["publisher"] } </p>
              <p> { message["year"] } </p>
              <a target='_blank' href={ message["url"] }>Know More!</a> 
            </div>
          
          </div>
        )
      })}
    </div>
  )
}

export default Text_Article