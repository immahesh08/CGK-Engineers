import React from "react";
import { useState } from "react";
import api from "../services/api";
export default function EnquiryForm({product,service}){
 const [form,setForm]=useState({name:"",company_name:"",email:"",phone:"",quantity:1,location:"",requirement:"",preferred_contact_method:"Phone",product:product?.id||"",service:service?.id||""});
 const [msg,setMsg]=useState("");
 const submit=async e=>{e.preventDefault();setMsg("Sending...");try{await api.post("/enquiries/",form);setMsg("Thank you. Your enquiry has been submitted.");setForm({...form,name:"",company_name:"",email:"",phone:"",location:"",requirement:""});}catch{setMsg("Unable to submit right now. Please try again.");}};
 return <form className="form" onSubmit={submit}><div className="formGrid"><input required placeholder="Name" value={form.name} onChange={e=>setForm({...form,name:e.target.value})}/><input placeholder="Company Name" value={form.company_name} onChange={e=>setForm({...form,company_name:e.target.value})}/><input type="email" placeholder="Email" value={form.email} onChange={e=>setForm({...form,email:e.target.value})}/><input required placeholder="Mobile Number" value={form.phone} onChange={e=>setForm({...form,phone:e.target.value})}/><input placeholder="Quantity" type="number" min="1" value={form.quantity} onChange={e=>setForm({...form,quantity:e.target.value})}/><input placeholder="Location" value={form.location} onChange={e=>setForm({...form,location:e.target.value})}/></div><textarea required placeholder="Requirement" value={form.requirement} onChange={e=>setForm({...form,requirement:e.target.value})}/><button className="primary" type="submit">Submit Enquiry</button>{msg&&<p className="formMsg">{msg}</p>}</form>
}
