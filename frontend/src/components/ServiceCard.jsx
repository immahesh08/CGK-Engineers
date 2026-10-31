import React from "react";
import { Link } from "react-router-dom";
export default function ServiceCard({s}){return <article className="card"><div className="iconBox">◆</div><h3>{s.title}</h3><p>{s.short_description||s.description}</p><Link className="textLink" to={`/services/${s.slug}`}>Learn More →</Link></article>}
