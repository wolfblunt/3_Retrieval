import React from 'react'

const Images=({data})=> {
    return(
        <div className="Images">
            {data.message && data.message.map(message =>{
                return(
                    <div className="div_images">
                        <a target='_blank' href={message["link"]}>
                        <img src ={message["original"]} alt="Image" className = "image_thumbnail"/>
                        </a>
                        <p className='image_title'>{message["title"]}</p>
                        <p className='image_source'><b>Source :</b> {message["source"]}</p>
                        <div>


                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default Images