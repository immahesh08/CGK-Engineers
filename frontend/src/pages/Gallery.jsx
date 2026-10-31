import React from "react";
import{useEffect,useState}from"react";import api from"../services/api";
export default function Gallery(){const[g,setG]=useState([]);useEffect(()=>{api.get("/gallery/").then(r=>setG(r.data.results||r.data)).catch(()=>{});},[]);return <main className="page container"><div className="pageIntro"><span className="eyebrow">GALLERY</span><h1>Our work in focus</h1></div><div className="gallery">{g.map(x=><figure key={x.id}>{x.image&&<img src={x.image} alt={x.title}/>}<figcaption>{x.title}</figcaption></figure>)}</div></main>}
