import React from 'react'

const Text_ECommerce = ({data}) => {

  console.log(data)

  return (
    <div className="textEcommerce">
      {data.message && data.message.map(message =>{
        return (

          <div className='textContainer'>
            
            <img src={message["Product Image Url"]} alt="Product Image" className = "textEcommerce_Image  "/>

            <div className='floatLeft'>
            
              <h2 className="Ecommerce_productname"> { message["Product Name"]} </h2>
              {/* <h2 > { message["Product Name"]} </h2> */}
              <h5> Price : { message["Product Price"] } </h5>
              <h5> Rating : { message["Product Rating"] } </h5>
              <a target='_blank' href={ message["Product Url"] }><h5>Buy Now!</h5></a>
              <h5>{message["Source"]}</h5>
            
            </div>

            <div className='clear'></div>

          </div>
        )
      })}
    </div>
  )
}

export default Text_ECommerce