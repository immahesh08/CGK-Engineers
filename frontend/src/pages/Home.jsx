import React from "react";
import { Link } from "react-router-dom";
import { ArrowRight, ShieldCheck, Wrench, Lightbulb, Snowflake, Building2, Settings } from "lucide-react";
import { useEffect,useState } from "react";
import api from "../services/api";
import ProductCard from "../components/ProductCard";
import ServiceCard from "../components/ServiceCard";
import "../styles/home.css";
export default function Home(){
 const [products,setProducts]=useState([]),[services,setServices]=useState([]);
 useEffect(()=>{Promise.all([api.get("/products/?page_size=4"),api.get("/services/?page_size=6")]).then(([p,s])=>{setProducts(p.data.results||p.data);setServices(s.data.results||s.data)}).catch(()=>{});},[]);
 return <><section className="hero"><div className="container heroInner"><div className="heroCopy"><span className="eyebrow">ENGINEERING • HVAC • ELECTRICAL</span><h1>Complete HVAC & Electrical Solutions for <em>Modern Spaces</em></h1><p>Reliable HVAC systems, VRF solutions, chillers, air conditioning, lighting and professional maintenance services for residential, commercial and industrial applications.</p><div className="heroBtns"><Link className="primary" to="/products">Explore Products <ArrowRight/></Link><Link className="secondary" to="/contact">Get a Quote</Link></div></div><div className="heroVisual"><div className="visualCard"><Snowflake size={56}/><b>HVAC</b><span>Engineered for performance</span></div></div></div></section>
 <section className="stats"><div className="container statGrid">{[["2012","Established"],["10+","Years Experience"],["100+","Projects"],["50+","Products"],["Pan India","Service"]].map(x=><div key={x[1]}><strong>{x[0]}</strong><span>{x[1]}</span></div>)}</div></section>
 <section className="section"><div className="container"><div className="sectionHead"><span className="eyebrow">OUR SOLUTIONS</span><h2>Products engineered around your requirements</h2><Link to="/products">View All <ArrowRight size={16}/></Link></div><div className="grid4">{products.map(p=><ProductCard key={p.id} p={p}/>)}</div></div></section>
 <section className="section light"><div className="container"><div className="sectionHead"><span className="eyebrow">WHAT WE DO</span><h2>Professional services from planning to support</h2></div><div className="grid3">{services.map(s=><ServiceCard key={s.id} s={s}/>)}</div></div></section>
 <section className="section"><div className="container why"><div><span className="eyebrow">WHY CGK</span><h2>Technical expertise you can rely on.</h2><p>We combine quality products, engineering capability and responsive support to deliver practical solutions for demanding spaces.</p><Link className="primary" to="/about">About Us <ArrowRight/></Link></div><div className="whyGrid">{[[ShieldCheck,"Quality Products"],[Wrench,"Reliable Support"],[Settings,"Technical Expertise"],[Building2,"Customized Solutions"],[Lightbulb,"Timely Service"],[Snowflake,"HVAC Specialists"]].map(([I,t])=><div key={t}><I/><b>{t}</b></div>)}</div></div></section>
 <section className="cta"><div className="container"><span className="eyebrow">START A PROJECT</span><h2>Need the right HVAC or lighting solution?</h2><p>Tell us your requirement and our team can help you plan the next step.</p><Link className="primary" to="/contact">Request a Quote <ArrowRight/></Link></div></section></>
}
