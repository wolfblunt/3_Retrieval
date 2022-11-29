import React from 'react'
import '../../index.css'
import RadioButtons from './RadioButtons';

export const Search = ({changeSearchTerm, changeSearchType, changeSearchDomain, showRadioButtons, onSubmit}) => {

    var radio;
    if (showRadioButtons) {
        radio = <RadioButtons changeSearchDomain={changeSearchDomain} />;
    }

  return (
    <div>   
        <img src ={require("../../Images/Seeker.png")} className="seeker_img"/>
        <input type="text" placeholder='What would you like to Search....?' className = "searchBar center"  onChange={changeSearchTerm}  />
        
        <select id="categories" className = "categoriesBar center" onChange={changeSearchType}>
            <option value="category" disabled selected>Select a category</option>
            <option value="text">Text</option>
            <option value="image">Images</option>
            <option value="video">Video</option>
        </select>

        {radio}

        <br />
        
        <button className='btn btn-primary center submitButton'  onClick={onSubmit}>Submit</button>

    </div>
  )
}

export default Search