import React from "react";
import { Link } from "react-router-dom";
export default function ProductCard({p}){return <article className="card productCard">
 <div className="productImage">{p.image?<img src={p.image} alt={p.name}/>:<span>HVAC</span>}</div>
 <div className="cardBody"><small>{p.category_name||"Engineering Solution"}</small><h3>{p.name}</h3><p>{p.short_description}</p><Link className="textLink" to={`/products/${p.slug}`}>View Details →</Link></div>
</article>}
