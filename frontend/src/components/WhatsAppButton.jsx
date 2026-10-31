import React from "react";
import { MessageCircle } from "lucide-react";
import { useCompany } from "../context/CompanyContext";
export default function WhatsAppButton(){
 const c=useCompany()||{}; if(!c.whatsapp)return null;
 const text=encodeURIComponent("Hello CGK Engineers & Consultants, I would like to enquire about your HVAC / AC / VRF / Chiller products and services.");
 return <a className="whatsapp" href={`https://wa.me/${c.whatsapp.replace(/\D/g,"")}?text=${text}`} target="_blank" rel="noreferrer"><MessageCircle/></a>
}
