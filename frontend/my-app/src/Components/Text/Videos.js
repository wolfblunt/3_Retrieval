import React from 'react'

const Videos=({data})=> {
    return(
        <div className="Videos">
            {data.message && data.message.map(message =>{
                return(
                    <div className='div_Videos'>
                        <a target='_blank' href={message["link"]}>
                        <img src ={message["thumbnail"]["static"]} onerror= "this.src=../../Images/default_thumbnail_video.jpg" alt="Video" className="video_thumbnail"/>
                        </a>
                        
                        <div className="div_Videos_description">
                            <a target='_blank' href={message["link"]} className="video_link">
                                <h2 className="primary-text">{ message["title"]}</h2> 
                            </a>
                           <br></br>
                           <p> <b> Description:</b> {message["description"]}</p>
                           <p><b>Length:</b>  {message["length"]} </p>
                           <p> <b>Date:</b> {message["published_date"]}</p>
                           <p> <b>Channel:</b> {message["channel"]["name"]}</p>
                           <p> <b>Views:</b> {message["views"]}</p>
                           
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default Videos