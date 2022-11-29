import React from 'react'

const RadioButtons = ({changeSearchDomain}) => {
  return (
    <div id="radioButton">

            <input type="radio" value="eCommerce" onClick={changeSearchDomain} name="searchQuery" />
            <label>E-Commerce</label>
            
            <input type="radio" value="news" onClick={changeSearchDomain} name="searchQuery" />
            <label>News</label>
            
            <input type="radio" value="article" onClick={changeSearchDomain} name="searchQuery" />
            <label>Articles</label>
            
            <input type="radio" value="movie" onClick={changeSearchDomain} name="searchQuery" />
            <label>Movies</label>

        </div>
  )
}

export default RadioButtons