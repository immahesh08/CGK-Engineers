import React from "react";
import { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { Menu, X, ArrowRight } from "lucide-react";
import "../styles/header.css";
const links = [["/","Home"],["/about","About"],["/products","Products"],["/services","Services"],["/projects","Projects"],["/gallery","Gallery"],["/contact","Contact"]];
export default function Header(){
 const [open,setOpen]=useState(false);
 return <header className="header"><div className="nav container">
  <Link className="logo" to="/" onClick={()=>setOpen(false)}><span>CGK</span><small>ENGINEERS & CONSULTANTS</small></Link>
  <button className="menuBtn" onClick={()=>setOpen(!open)}>{open?<X/>:<Menu/>}</button>
  <nav className={open?"navLinks open":"navLinks"}>{links.map(([to,label])=><NavLink key={to} to={to} onClick={()=>setOpen(false)}>{label}</NavLink>)}<Link className="quoteBtn" to="/contact" onClick={()=>setOpen(false)}>Get Quote <ArrowRight size={16}/></Link></nav>
 </div></header>
}
