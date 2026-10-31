import React from "react";
import { Link } from "react-router-dom";
import { useCompany } from "../context/CompanyContext";
export default function Footer(){
 const c=useCompany()||{};
 return <footer><div className="container footerGrid">
  <div><div className="logo footerLogo"><span>CGK</span><small>ENGINEERS & CONSULTANTS</small></div><p>Professional HVAC, VRF, chiller, air-conditioning and lighting solutions for modern spaces.</p></div>
  <div><h4>Company</h4><Link to="/about">About</Link><Link to="/products">Products</Link><Link to="/services">Services</Link><Link to="/projects">Projects</Link><Link to="/gallery">Gallery</Link><Link to="/contact">Contact</Link></div>
  <div><h4>Products</h4><span>AC Systems</span><span>VRF Systems</span><span>Chillers</span><span>LED Lights</span><span>Street Lights</span><span>Solar Lighting</span></div>
  <div><h4>Contact</h4><span>{c.address||"Tatibandh, Raipur, Chhattisgarh - 492001, India"}</span><span>{c.phone||"Phone — Configure in Admin"}</span><span>{c.email||"Email — Configure in Admin"}</span></div>
 </div><div className="copyright">© 2026 CGK Engineers & Consultants. All Rights Reserved.</div></footer>
}
