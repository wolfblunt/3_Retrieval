import React from 'react'
import Header from './HomePageComponents/Header'
import Search from './HomePageComponents/Search'
import SearchAgain from './SearchAgain'
import APIService from './APIService'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useState } from 'react';

import ecommerce from '../Json/ECommerce JSON.json';
import articles from '../Json/Article JSON.json';
import movie from '../Json/Movie JSON.json';
import news from '../Json/News JSON.json';
import images from '../Json/Images JSON.json';
import videos from '../Json/Vidoes.json';

import Text_ECommerce from './Text/Text_ECommerce';
import Text_News from './Text/Text_News';
import Text_Article from './Text/Text_Article';
import Text_Movie from './Text/Text_Movie';
import Images from './Text/Images';
import Videos from './Text/Videos';
import APIService_image from './APIService_image'
import APIService_video from './APIService_video'


const HomePage = () => {

  const [data, setData] = useState("")

  const [displayComponent, setdisplayComponent] = useState(0)  
  const [searchTerm, setTerm] = useState("")
  const [searchType, setType] = useState("")
  const [searchDomain, setDomain] = useState("")
  const [showRadioButtons, setRadioButton] = useState(false)


  const reset = () =>{
    if(displayComponent != 0){
      setdisplayComponent(0)
      setTerm("")
      setType("")
      setDomain("")
      setRadioButton(false)
    }
  }

  const changeSearchTerm = (e) => {
    setTerm(e.target.value)
  }


  const changeSearchType = (e) => {
    setType(e.target.value)

    if (e.target.value === "text"){
      setRadioButton(true)
    }      
    else{ 
      setRadioButton(false)
      setDomain("")
    }

  }

  const changeSearchDomain = (e) => {
    setDomain(e.target.value)
  }


  const onSubmit = () => {

    var flag = true;

    if(searchTerm !== "" && searchType !== ""){
      if(searchType === "text" && searchDomain === "")
        flag = false;
    }
    else{
      flag = false;
    }
      
    if(!flag){
      toast.error('Incomplete search query !', {
        position: toast.POSITION.TOP_RIGHT
      });
    }
    else{
      toast.success('Getting results !', {
        position: toast.POSITION.TOP_RIGHT
      });
      
      if(searchType ==="image"){
        APIService_image.sendQuery_image({searchTerm, searchType, searchDomain})
      // .then((response) => console.log(response))
      .then((response) => {
        if(response == null){
          toast.error('Failed to connect.', {
            position: toast.POSITION.TOP_RIGHT
          });
        }
        else if (response["status"] != "OK"){
          toast.error('No results found.', {
            position: toast.POSITION.TOP_RIGHT
          });
        }
        else{
          // toast.success('Getting results !', {
          //   position: toast.POSITION.TOP_RIGHT
          // });
          selectPage(response)
        } 
      })
      .catch(error => console.log('error',error))
      }
      else if(searchType ==="video"){
        APIService_video.sendQuery_video({searchTerm, searchType, searchDomain})
        // .then((response) => console.log(response))
        .then((response) => {
          if(response == null){
            toast.error('Failed to connect', {
              position: toast.POSITION.TOP_RIGHT
            });
          }
          else if (response["status"] != "OK"){
            toast.error('No results found.', {
              position: toast.POSITION.TOP_RIGHT
            });
          }
          else{
            // toast.success('Getting results !', {
            //   position: toast.POSITION.TOP_RIGHT
            // });
            selectPage(response)
          }
        })
        .catch(error => console.log('error',error))
      }
      else{
        APIService.sendQuery({searchTerm, searchType, searchDomain})
        // .then((response) => console.log(response))
        .then((response) => {
          if(response == null){
            toast.error('Failed to connect', {
              position: toast.POSITION.TOP_RIGHT
            });
          }
          else if (response["status"] != "OK"){
            toast.error('No results found.', {
              position: toast.POSITION.TOP_RIGHT
            });
          }
          else{
            // toast.success('Getting results !', {
            //   position: toast.POSITION.TOP_RIGHT
            // });
            selectPage(response)
          }
        })
        .catch(error => console.log('error',error))
      }

     //selectPage(movie);

    }

  }

  const selectPage = (response) => {
    
    setData(response);

    if(searchType === "text"){
      
      if(searchDomain === "eCommerce")
        setdisplayComponent(1)
      else if(searchDomain === "news")
        setdisplayComponent(2)
      else if(searchDomain === "article")
        setdisplayComponent(3)
      else if(searchDomain === "movie")
        setdisplayComponent(4)

    }
    else if(searchType === "image")
      setdisplayComponent(5)
    else if(searchType === "video")
      setdisplayComponent(6)  
  }


  return (

    <div>

      <Header reset={reset}/>
    
      {(() => {

        if ( displayComponent === 0) {
          return (
            <Search changeSearchTerm={changeSearchTerm} changeSearchType={changeSearchType} changeSearchDomain={changeSearchDomain}  showRadioButtons={showRadioButtons} onSubmit={onSubmit}/>
          )
        } else if (displayComponent === 1) {
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">Search results for : {searchTerm} </h4>
                <Text_ECommerce data={data}/>
            </div>
          )
        } else if (displayComponent === 2) {
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">News results for : {searchTerm} </h4>
              <Text_News data={data}/>
            </div>
            
          )
        } else if (displayComponent === 3) {
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">Article results for : {searchTerm} </h4>
              <Text_Article data={data}/>
            </div>
            
          )
        } else if (displayComponent === 4) {
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">Movie results for : {searchTerm} </h4>
              <Text_Movie data={data}/>
            </div>
            
          )
        } else if (displayComponent === 5) {
          console.log("Inside images ");
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">Image results for : {searchTerm} </h4>
              <Images data={data}/>
            </div>
            
          )
        } else {
          return (
            <div>
              <SearchAgain reset={reset} data={data["message"].length}/>
              <h4 className="Search_results_text">Video results for : {searchTerm} </h4>
              <Videos data={data} />
            </div>
          )
        }

      })()}

      <ToastContainer autoClose={2000}/>

    </div>

  )
}

export default HomePage