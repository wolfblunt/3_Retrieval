import React from 'react'
import seeker from '../../Images/Seeker.png'
import '../../index.css'
// import { useState } from 'react'

const Header = ({reset}) => {

  const current = new Date();

  // const [day, setDay] = useState()
 

  const day = (d) => {
    if (d === 0)
      return "Sunday";
    else if (d === 1)
      return "Monday";
    else if (d === 2)
      return "Tuesday";
    else if (d === 3)
      return "Wednesday";
    else if (d === 4)
      return "Thursday";
    else if (d === 5)
      return "Friday";
    else
      return "Saturday";
      
  }

  const date = (d) => {
    if (d === 1)
      return "1st";
    else if (d === 2)
      return "2nd";
    else if (d === 3)
      return "3rd";
    else  
      return d+"th";
  }

  const month = (d) =>{
    if (d === 0)
      return "January";
    else if (d === 1)
      return "Feburary";
    else if (d === 2)
      return "March";
    else if (d === 3)
      return "April";
    else if (d === 4)
      return "May";
    else if (d === 5)
      return "June";
    else if (d === 6)
      return "July";
    else if (d === 7)
      return "August";
    else if (d === 8)
      return "September";
    else if (d === 9)
      return "October";
    else if (d === 10)
      return "November";
    else
      return "December";
  }

  const completeDate = `${day(current.getDay())}, ${date(current.getDate())} ${month(current.getMonth())} ${current.getFullYear()}`;


  

  return (
    <div className="header_logo_and_date">
        <img src={seeker} alt="logo" className = "logoStyle" onClick={reset} />
        <h4 className = "headingStyle center" >{completeDate}</h4>
    </div>
  )
}


export default Header