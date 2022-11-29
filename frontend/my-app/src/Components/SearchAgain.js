import React from 'react'

const SearchAgain = ({reset, data}) => {
  return (
    <div>
        <p onClick={reset} className="search_again">Search Again</p>
        <p className="total_count">Total Results : {data}</p>
    </div>
  )
}

export default SearchAgain